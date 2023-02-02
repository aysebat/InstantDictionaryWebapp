import justpy as jp
class DefaultLayout(jp.QLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #This is the self(layout) we are goint to use that
        #when we initialize the class
        #layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=self,
                            classses="bg-primary text-white font-mono")
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=self,
                            show_if_above=True,
                            v_model="leftDrawerOpen",
                            side="left",
                            bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller)
        a_classes = 'p-2 n-2 text-lg text-blue-400 hover:text-blue-700'
        jp.A(a=qlist, text="Home", href="/", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about" , classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="\dictionary" , classes=a_classes)
        jp.Br(a=qlist)

        jp.QBtn(a=toolbar,
                flat=True,
                dense=True,
                round=True,
                icon="menu",
                click=self.move_drawer,
                drawer=drawer)
        jp.QToolbarTitle(a=toolbar,
                         text="Instant Dictionary")

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
