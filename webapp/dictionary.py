import justpy as jp


class Dictionary:
    path = "/dictionary"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        mainDiv = jp.Div(a=wp, classes="bg-gray-00 h-screen")
        jp.Div(a=mainDiv,
               text="Instant English Dictionary",
               classes="text-4xl m-2")
        jp.Div(a=mainDiv,
               text="Get the definition of any English word instantly as you type...",
               clases="text-lg")
        jp.Input(a=mainDiv,
                 placeholder="Type in any word here...",
                 classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 "
                         "focus:outline-none focus:border-purple-500 focus:bg-white "
                         "py-2 px-4")
        jp.Div(a=mainDiv,
               classes="m-2 p-2 text-lg border-2 h-40 ")
        return wp


