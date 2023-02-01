import justpy as jp


class Home:
    path = "/"

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
        mainDiv = jp.Div(a=container, classes="h-screen")

        jp.Div(a=mainDiv, text="This is the Home Page")
        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
