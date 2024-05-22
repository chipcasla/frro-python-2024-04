import cv2  

captura = cv2.VideoCapture(0)
salida = cv2.VideoWriter("videosalida.avi", cv2.VideoWriter_fourcc(* 'XVID' ) ,20.0, (640,480) )

                         
while (captura.isOpened()):
    rest,imagen = captura.read() 
    if rest == True :
        cv2.imshow('Video', imagen)
        salida.write(imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break 
    else: break 

captura.release()
salida.release()
cv2.destroyAllWindows()