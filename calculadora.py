from kivy.app import App
from kivy.uix.label import Label

class calculadoraApp(App):
    def calcular(self):
        try:
            resultado = str(eval(self.root.ids.label.text))
            return resultado
        except Exception as e:
            return ""

    def actualizar_label(self, resultado):
        if resultado:
            self.root.ids.label.text = resultado
        else:
            self.root.ids.label.text = "Error"
            self.root.ids.label.color = 1, 0, 0, 1  # Color rojo en formato RGBA

if __name__ == '__main__':
    calculadoraApp().run()
