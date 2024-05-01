from kivy.app import App


class spinnerApp(App):

    info_futbol = {
        "San Lorenzo": {
            "Fundación": "1908",
            "Apodo": "Ciclón, Cuervo",
            "Estadio": "Pedro Bidegain",
        },
        "Independiente": {
            "Fundación": "1904",
            "Apodo": "Rojo, Rey de copas",
            "Estadio": "Libertadores de América",
        },
        "River": {
            "Fundación": "1901",
            "Apodo": "Millonario",
            "Estadio": "Mâs Monumental",
        },
    }


if __name__ == "__main__":
    spinnerApp().run()