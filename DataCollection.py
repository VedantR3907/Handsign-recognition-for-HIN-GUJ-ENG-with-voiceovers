import math
from cvzone.HandTrackingModule import HandDetector
import cv2 as cv
import numpy as np
import time

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
codec = 0x47504A4D  # MJPG
cap.set(cv.CAP_PROP_FPS, 30.0)
cap.set(cv.CAP_PROP_FOURCC, codec)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
Detector = HandDetector(maxHands=1)


offset = 20
imgsize = 300
counter = 0

folder = "E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Data/ISL DATA/asd"

while True:
    Success, img = cap.read()
    hands, img = Detector.findHands(img)
    img = cv.flip(img, 1)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        x = 1280 - x
        x = x - w

        imgextra = np.ones((imgsize,imgsize,3), np.uint8)*255
        imgcrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        ratiohw = h/w # if the value is > 1 height is greater else Width is greater

        if ratiohw > 1: #Height is greater
            k = imgsize / h
            wcal = math.ceil(k * w)
            imgResize = cv.resize(imgcrop, (wcal, imgsize))
            wgap = math.ceil((imgsize-wcal)/2)              #Put the image in the Middle
            imgextra[:, wgap:wcal+wgap] = imgResize         #Putting in the white Image
        else:            #Width is greater
            k = imgsize / w
            hcal = math.ceil(k * h)
            imgResize = cv.resize(imgcrop, (imgsize, hcal))
            hgap = math.ceil((imgsize-hcal)/2)              #Put the image in the Middle
            imgextra[hgap:hcal+hgap, :] = imgResize         #Putting in the white Image

        cv.imshow("ImageCropWhite", imgextra)
    cv.imshow("Image",img)

    key = cv.waitKey(1)
    if key == ord("s"):
        counter += 1
        cv.imwrite(f'{folder}/Image_{time.time()}.jpg',imgextra)
        print("Number of images Saved :- ",counter)
