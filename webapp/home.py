import justpy as jp


class Home:
    path = "/"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        mainDiv = jp.Div(a=wp, classes="bg-gray-200 h-screen")

        jp.Div(a=mainDiv, text="This is the Home Page")
        return wp


