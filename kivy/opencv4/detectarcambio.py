import cv2 
import time 

camara = cv2.VideoCapture(r"C:\Users\capig\OneDrive\Documentos\frro-python-2024-04\kivy\opencv4\gol-messi.mp4")

fondo = None 

while True: 
    (grabbed, frame) = camara.read()
    if not grabbed: 
        break 
    gris= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    gris= cv2.GaussianBlur(gris,(21,21),0)

    if fondo is None: 
        fondo = gris
        continue   
    
    resta= cv2.absdiff(fondo,gris)

    umbral = cv2.threshold(resta, 25,255,cv2.THRESH_BINARY)[1]   
    umbral = cv2.dilate(umbral,None,iterations=20)

    contornosimg = umbral.copy() 
    contornos,hierarchy = cv2.findContours(contornosimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos: 
        if cv2.contourArea(c) < 200:
            continue 
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow("Camara", frame)
    cv2.imshow("umbral", umbral)
    cv2.imshow("Resta", resta)
    cv2.imshow("Contorno", contornosimg)

    key = cv2.waitKey(1) & 0xFF 
    
    time.sleep(0.015)
    
    if key == ord("s"):
        break 


camara.release() 

cv2.destroyAllWindows()