import justpy as jp


class Dictionary:
    path = '/dictionary'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        mainDiv = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=mainDiv,
               text="This is the dictioany page",
               classes="text-4xl m-2")
