import justpy as jp
from webapp import layout


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        web_layout = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=web_layout)
        mainDiv = jp.Div(a=container, classes="bg-gray-100 h-screen font-mono")

        jp.Div(a=mainDiv,
               text="This is the about page",
               classes="text-4xl mx-4")

        jp.Div(a=mainDiv,
               text="""Lorem Ipsum is simply dummy text of the printing and
                typesetting industry. Lorem Ipsum has been the industry's
                 standard dummy text ever since the 1500s, when an unknown
                  printer took a galley of type and scrambled it to make 
                  a type specimen book. It has survived not only five 
                  centuries, but also the leap into electronic typesetting, 
                  remaining essentially unchanged. It was popularised in the
                   1960s with the release of  sheets containing 
                   Lorem Ipsum passages, and more recently with desktop
                    publishing software like Aldus PageMaker including 
                    versions of Lorem Ipsum""",
               classes="text-lg m-4")
        return wp
