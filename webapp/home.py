import justpy as jp
from webapp import layout
from webapp import page

#Home page is Page object types.
class Home(page.Page):
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        web_layout = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=web_layout)
        mainDiv = jp.Div(a=container,
                         classes="bg-gray-100 h-screen font-mono")

        jp.Div(a=mainDiv,
               text="This is the Home Page",
               classes="text-4xl mx-4")
        return wp


