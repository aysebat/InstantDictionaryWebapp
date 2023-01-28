import justpy as jp



class Home:
    path ='/home'
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        mainDiv = jp.Div(a=wp, classes="bg-gray-200 h-screen")

        jp.Div(a=mainDiv, text="Div Content")
        return wp


