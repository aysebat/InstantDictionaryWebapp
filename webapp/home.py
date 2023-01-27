import justpy as jp


@jp.SetRoute("/home")
def home():
    wp = jp.QuasarPage(tailwind=True)
    container = jp.Div(a=wp, classes="bg-gray-200 h-screen")

    jp.Div(a=container, text="Div Content")
    return wp



#to run the server
jp.justpy()