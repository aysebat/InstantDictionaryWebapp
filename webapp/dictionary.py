import justpy as jp
import definition


class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout,
                            classses="bg-primary text-white font-mono")
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout,
                            show_if_above=True,
                            v_model="leftDrawerOpen",
                            side="left",
                            bordered=True)
        jp.QBtn(a=toolbar,
                flat=True,
                dense=True,
                round=True,
                icon="menu",
                click=cls.move_drawer,
                drawer=drawer)
        jp.QToolbarTitle(a=toolbar,
                         text="Instant Dictionary")
        container = jp.QPageContainer(a=layout)
        mainDiv = jp.Div(a=container, classes="bg-gray-100 h-screen font-mono")
        jp.Div(a=mainDiv,
               text="Instant English Dictionary",
               classes="text-4xl m-2 ")
        jp.Div(a=mainDiv,
               text="Get the definition of any English word instantly as you type...",
               clases="text-lg m-2")
        # input div
        inputDiv = jp.Div(a=mainDiv, classes="grid grid-cols-2 my-4")
        outputDiv = jp.Div(a=mainDiv,
                           classes="m-2 p-2 text-lg border-2 h-40 ")
        input_box = jp.Input(a=inputDiv,
                             placeholder="Type in any word here...",
                             classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 "
                                     "focus:outline-none focus:border-purple-500 focus:bg-white "
                                     "py-2 px-4 font-mono",
                             output_div=outputDiv)

        # when someone write on the input box
        input_box.on('input', cls.get_definition)

        # jp.Button(a=inputDiv,
        #           text="GetDefinition",
        #           classes="border-2 text-gray-s500",
        #           click=cls.get_definition,
        #           output_div=outputDiv,
        #           input_box=input_box
        #           )
        #           #you can use output and input variable in get_definition method

        print(cls, req)
        return wp

    @staticmethod
    def get_definition(widget, msg):
        """widget is the button
           msg is contain the data about the event"""

        defined = definition.Definition(widget.value).get()
        widget.output_div.text = " ".join(defined)

        # this can be used for teh button elemnt
        # defined = definition.Definition(widget.input.value).get()

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
