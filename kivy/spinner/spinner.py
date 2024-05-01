from kivy.app import App
from kivy.uix.screenmanager import Screen

class spinnerApp(App):
    def update_labels(self):
        selected_receta = self.root.ids.receta_spinner.text
        if selected_receta == "Pollo al disco":
            self.root.ids.nombre_label.text = "Nombre: Pollo al disco"
            self.root.ids.ingredientes_label.text = "Ingredientes: 2 kg de piezas de pollo \n5 zanahorias grandes\n2 kilos de papa\n5 choclos\n2 cebollas blancas\n2 cebollas de verdeo\n1 puerro"
            self.root.ids.paso_a_paso_label.text = "Paso a paso: Lo primero que tenemos que hacer es calentar el disco en leña, o carbón. Lo que tengas. El disco debe estar bien caliente.\nUna vez que esté caliente (tengan cuidado y usen trapos secos para tocar el disco por favor se los pido) agregar un chorro de aceite desde afuera del disco hacia adentro.\nDorar las piezas de pollo, aproximadamente 5 minutos de cada lado. Sacarlas y reservarlas a un costado. Tiren el aceite que les quedó de más en el disco.\nPelar y cortar chiquito la cebolla y los dientes de ajo. La zanahoria en rodajas al igual que el puerro y la cebolla de verdeo. Poner las verduras en el disco y saltear por 5 minutos.\nAgregar el vino blanco y la pimienta y lo dejamos reducir.\nCuando evaporó el alcohol (te vas a dar cuenta porque no larga olor a alcohol etílico) le agregamos una taza del caldo y remuevan. Sumamos el pollo que teníamos a un costado y cocinamos unos 10 minutos más o hasta que las zanahorias estén medianamente tiernas.\nCuando estén a media cocción le agregamos las papas peladas y cortadas en rodajas de 1 cm de espesor, el choclo cortado en tercios y agregamos el caldo que faltaba  y la crema. Tapamos y dejamos cocinar unos 15 o 20 minutos más.\nCondimentamos el pollo al disco con el ají, el pimentón, el orégano y la sal 5 minutos antes de que termine la cocción."
            self.root.ids.porciones_label.text = "Porciones: 6 a 8"
            self.root.ids.duracion_label.text = "Duracion: 55 min"

if  __name__ == '__main__':
    spinnerApp().run()