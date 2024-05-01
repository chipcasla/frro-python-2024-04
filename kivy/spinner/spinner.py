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

    def update_labels(self):
        selected_receta = self.root.ids.receta_spinner.text
        if selected_receta == "Pollo al disco":
            self.root.ids.nombre_label.text = "Nombre: Pollo al disco"
            self.root.ids.ingredientes_label.text = (
                "Ingredientes: 2 kg de piezas de pollo \n5 zanahorias grandes\n"
            )
            self.root.ids.paso_a_paso_label.text = "\nPaso a paso: Lo primero que tenemos que hacer es calentar el disco en leña, o carbón. Lo que tengas. El disco debe estar bien caliente.\nUna vez que esté caliente (tengan cuidado y usen trapos secos para tocar el disco por favor se los pido) agregar un chorro de aceite desde afuera del disco hacia adentro."
            self.root.ids.porciones_label.text = "\nPorciones: 6 a 8"
            self.root.ids.duracion_label.text = "\nDuracion: 55 min"


if __name__ == "__main__":
    spinnerApp().run()
