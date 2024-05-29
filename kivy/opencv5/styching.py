import cv2

image_path=['im1.jpg','im2.jpg','im3.jpg','im4.jpg']

imgs=[]

for i in range(len(image_path)):
    imgs.append(cv2.imread(image_path[i]))
    imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.4,fy=0.4)

cv2.imshow('1', imgs[0])
cv2.imshow('2', imgs[1])
cv2.imshow('3', imgs[2])
cv2.imshow('4', imgs[3])

stitchy= cv2.Stitcher.create()
(dummy,output) = stitchy.stitch(imgs)

if dummy != cv2.STITCHER_OK:
    print("can't stitch images, error code = %d"%dummy)
else:
    print("stitching success")

cv2.imshow('final result', output)
cv2.waitKey(0)