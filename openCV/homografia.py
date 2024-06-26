import cv2
import numpy as np

def aruco_display(corners, ids, rejected, image, overlay):
    if len(corners) > 0:
        ids = ids.flatten()
        # Procesar solo el primer marcador detectado
        markerCorner, markerID = corners[0], ids[0]
        corners = markerCorner.reshape((4, 2))
        (topLeft, topRight, bottomRight, bottomLeft) = corners
        pts_dst = np.array([topLeft, topRight, bottomRight, bottomLeft])

        # Calcular la homografía y aplicar la transformación
        h, w, _ = overlay.shape
        pts_src = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=float)
        h_matrix, _ = cv2.findHomography(pts_src, pts_dst)
        warped_overlay = cv2.warpPerspective(overlay, h_matrix, (image.shape[1], image.shape[0]))

        # Crear una máscara para el área del overlay
        mask = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
        cv2.fillConvexPoly(mask, pts_dst.astype(int), 255)

        # Invertir la máscara para borrar el área del QR en la imagen original
        mask_inv = cv2.bitwise_not(mask)
        image_bg = cv2.bitwise_and(image, image, mask=mask_inv)
        overlay_fg = cv2.bitwise_and(warped_overlay, warped_overlay, mask=mask)

        # Sumar las dos imágenes
        image = cv2.add(image_bg, overlay_fg)

        # Dibuja el contorno del marcador
        cv2.polylines(image, [pts_dst.astype(int)], True, (0, 255, 0), 2)
        
        print("[Inference] arUco marker ID: {}".format(markerID))
    return image

video = cv2.VideoCapture(0)
arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_250)
arucoParams = cv2.aruco.DetectorParameters()

# Cargar la imagen que se quiere mostrar sobre el QR
overlay = cv2.imread(r'C:\Users\tomas\OneDrive\Escritorio\Facultad\Soporte 2024\openCV\messi.png')

# Verificar si la imagen se ha cargado correctamente
if overlay is None:
    raise FileNotFoundError("No se pudo cargar la imagen de superposición. Verifique la ruta del archivo.")

while True:
    ret, frame = video.read()
    if not ret:
        break

    h, w, _ = frame.shape
    width = 1000
    height = int((width / w) * h)
    frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_CUBIC)
    
    corners, ids, rejected = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)
    detected_markers = aruco_display(corners, ids, rejected, frame, overlay)
    
    cv2.imshow("Image", detected_markers)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
video.release()
