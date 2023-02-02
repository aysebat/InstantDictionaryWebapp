import justpy as jp
import layout

class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        web_layout = layout.DefaultLayout(a=wp, view="hHh lpR fFf")
        container = jp.QPageContainer(a=web_layout)
        mainDiv = jp.Div(a=container, classes="h-screen")

        jp.Div(a=mainDiv, text="This is the Home Page")
        return wp


