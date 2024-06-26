import cv2
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Inicializar variables globales
texture_background = None
video_frame = None
warp_matrix = None

# Función para configurar el entorno de OpenGL
def init_gl():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

def draw_cube():
    glBegin(GL_QUADS)

    # Front face
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)

    # Back face
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)

    # Top face
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)

    # Bottom face
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)

    # Right face
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)

    # Left face
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)

    glEnd()

def aruco_display(corners, ids, image):
    global warp_matrix

    if len(corners) > 0:
        ids = ids.flatten()
        markerCorner = corners[0].reshape((4, 2))
        (topLeft, topRight, bottomRight, bottomLeft) = markerCorner
        pts_dst = np.array([topLeft, topRight, bottomRight, bottomLeft])

        h, w = image.shape[:2]
        pts_src = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=float)
        warp_matrix, _ = cv2.findHomography(pts_src, pts_dst)
    return image

def detect_and_render():
    global texture_background, video_frame

    # Leer un cuadro del video
    ret, frame = video.read()
    if not ret:
        return

    # Detectar marcadores ArUco
    corners, ids, rejected = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)
    detected_markers = aruco_display(corners, ids, frame)

    # Configurar la textura de fondo
    frame_rgb = cv2.cvtColor(detected_markers, cv2.COLOR_BGR2RGB)
    frame_rgb = np.flip(frame_rgb, axis=0)

    glBindTexture(GL_TEXTURE_2D, texture_background)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, frame_rgb.shape[1], frame_rgb.shape[0], 0, GL_RGB, GL_UNSIGNED_BYTE, frame_rgb)

    # Limpiar buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Dibujar la textura de fondo
    glBindTexture(GL_TEXTURE_2D, texture_background)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex2f(-1.0, -1.0)
    glTexCoord2f(1.0, 0.0); glVertex2f(1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex2f(1.0, 1.0)
    glTexCoord2f(0.0, 1.0); glVertex2f(-1.0, 1.0)
    glEnd()

    # Dibujar el cubo si se ha detectado un marcador
    if warp_matrix is not None:
        glPushMatrix()
        glMultMatrixf(np.linalg.inv(warp_matrix).T)
        draw_cube()
        glPopMatrix()

    glutSwapBuffers()

def main():
    global video, arucoDict, arucoParams, texture_background

    # Configurar video y diccionario ArUco
    video = cv2.VideoCapture(0)
    arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_250)
    arucoParams = cv2.aruco.DetectorParameters()

    # Configurar OpenGL
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutCreateWindow(b"AR with OpenCV and OpenGL")
    init_gl()

    # Configurar la textura de fondo
    texture_background = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_background)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    glutDisplayFunc(detect_and_render)
    glutIdleFunc(detect_and_render)
    glutMainLoop()

    # Liberar recursos
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
