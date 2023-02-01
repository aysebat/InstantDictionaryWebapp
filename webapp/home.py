import justpy as jp


class Home:
    path = "/"

     @classmethod
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout,
                            classses="bg-primary text-white")
        toolbar = jp.QToolbar(a=header)
        jp.QBtn(a=toolbar,
                dense=True,
                flat=True,
                round=True,
                icon="menu",
                click=cls.move_draver, draver=draver
                )




        mainDiv = jp.Div(a=wp, classes="bg-gray-200 h-screen")

        jp.Div(a=mainDiv, text="This is the Home Page")
        return wp
@staticmethod
def move_draver(wigdet, msg):
    pass


