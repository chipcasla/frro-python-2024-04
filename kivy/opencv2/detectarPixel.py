import numpy as np 
import cv2 

cap = cv2.VideoCapture(0)  
_, img = cap.read()
averageValue1 = np.float32(img)

while(1): 
    _, img = cap.read()
    
    cv2.accumulateWeighted(img,averageValue1,0.05)

    resultingFrames1 = cv2.convertScaleAbs(averageValue1)

    cv2.imshow ("imputWindows", img)
    cv2.imshow ("Averaged Frames", resultingFrames1)    

    k = cv2.waitKey(30) & 0xff 
    if k == 27:
        break 

cap.release() 

cv2.destroyAllWindows()