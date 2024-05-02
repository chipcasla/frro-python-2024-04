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
            self.root.ids.paso_a_paso_label.text = "\nPaso a paso: Lo primero que tenemos que hacer es calentar el disco en leña, o carbón. Lo que tengas. El disco debe estar bien caliente. Una vez que esté caliente (tengan cuidado y usen trapos secos para tocar el disco por favor se los pido) agregar un chorro de aceite desde afuera del disco hacia adentro."
            self.root.ids.porciones_label.text = "\nPorciones: 6 a 8"
            self.root.ids.duracion_label.text = "\nDuracion: 55 min"
        elif selected_receta == "Pizza casera":
            self.root.ids.nombre_label.text = "Nombre: Pizza casera"
            self.root.ids.ingredientes_label.text = "Ingredientes: Masa de pizza, Salsa de tomate, Queso mozzarella \nIngredientes adicionales (opcional): pepperoni, champiñones, jamón, etc."
            self.root.ids.paso_a_paso_label.text = "\nPaso a paso: Extiende la masa de pizza sobre una bandeja para hornear. Agrega la salsa de tomate y los ingredientes deseados. Cubre con queso mozzarella rallado. Hornea en un horno precalentado a 220°C durante 12-15 minutos o hasta que la masa esté dorada y el queso esté derretido."
            self.root.ids.porciones_label.text = "\nPorciones: 4 a 6"
            self.root.ids.duracion_label.text = "\nDuracion: 30 min"
        elif selected_receta == "Milanesas con pure":
            self.root.ids.nombre_label.text = "Nombre: Milanesas con puré"
            self.root.ids.ingredientes_label.text = "Ingredientes: Milanesas de carne, Pan rallado, Huevos, Puré de papas \nLeche, Manteca"
            self.root.ids.paso_a_paso_label.text = "\nPaso a paso: Pasa las milanesas por huevo batido y luego por pan rallado. Fríelas en aceite caliente hasta que estén doradas. Para el puré de papas, hierve las papas hasta que estén tiernas, luego haz puré con un poco de leche y manteca. Sirve las milanesas con el puré de papas."
            self.root.ids.porciones_label.text = "\nPorciones: 4"
            self.root.ids.duracion_label.text = "\nDuracion: 40 min"
        elif selected_receta == "Tallarines caseros":
            self.root.ids.nombre_label.text = "Nombre: Tallarines caseros"
            self.root.ids.ingredientes_label.text = "Ingredientes: Harina, Huevos, Sal"
            self.root.ids.paso_a_paso_label.text = "\nPaso a paso: Haz un volcán con la harina sobre una superficie limpia. Rompe los huevos en el centro del volcán y añade una pizca de sal. Mezcla gradualmente la harina con los huevos hasta formar una masa. Amasa la masa durante unos minutos hasta que esté suave. Deja reposar la masa durante 30 minutos. Luego, estira la masa y córtala en tiras para hacer los tallarines. Cocina en agua hirviendo con sal durante 2-3 minutos."
            self.root.ids.porciones_label.text = "\nPorciones: 4"
            self.root.ids.duracion_label.text = "\nDuracion: 60 min"


if __name__ == "__main__":
    spinnerApp().run()
