import cv2 


def aruco_display(corners, ids, rejected, image):
    if len(corners) > 0:
        ids = ids.flatten()
        for (markerCorner, markerID) in zip(corners, ids):
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            cv2.line(image, topLeft, topRight, (0, 255, 0),
                     2)
            cv2.line(image, topRight, bottomRight, (0, 255, 0
                                                    ), 2)
            cv2.line(image, bottomRight, bottomLeft, (0, 255, 0
                                                      ), 2)
            cv2.line(image, bottomLeft, topLeft, (0, 255, 0),
                     2)
            cx = int((topLeft[0] + bottomRight[0])/2.0)
            cy = int((topLeft[1] + bottomRight[1])/2.0)
            cv2.circle(image, (cx, cy), 4, (0, 0,255), -1)
            cv2.putText(image, str(markerID),
                        (topLeft[0], topLeft[1] - 15),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)
            print("[Inference] arUco marker ID: {}" .format(markerID))
    return image
        
video = cv2.VideoCapture(0)
arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_250)
arucoParams = cv2.aruco.DetectorParameters()

while True:
    ret, frame = video.read()
    if ret is False:
        break

    h,w,_ = frame.shape

    width = 1000
    height = int((width / w) * h)
    frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_CUBIC)
    corners, ids, rejected = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)
    detected_markers = aruco_display(corners, ids, rejected, frame)
    cv2.imshow("Image", detected_markers)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cv2.destroyAllWindows()
video.release()



