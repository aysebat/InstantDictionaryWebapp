import justpy as jp


class Navbar:

    def server(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        navDiv = jp.Div(a=wp,
                        classes="bg-gray-100 h-screen font-mono")

        return wp
