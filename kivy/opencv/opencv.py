import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

def capture_image():
    cap = cv2.VideoCapture(0)  

    ret, frame = cap.read()  
    if ret:
        cv2.imwrite('captured2_image.jpg', frame)  
    
    cap.release()  
    cv2.destroyAllWindows() 

class CameraBoxLayout(BoxLayout):
    def capture(self):
        capture_image()

class opencvApp(App):
    def build(self):
        return CameraBoxLayout()

if __name__ == '__main__':
    opencvApp().run()
