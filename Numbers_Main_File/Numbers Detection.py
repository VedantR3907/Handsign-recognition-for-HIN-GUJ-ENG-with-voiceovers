import math
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import cv2 as cv
import numpy as np
import time
from playsound import playsound

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
codec = 0x47504A4D  # MJPG
cap.set(cv.CAP_PROP_FPS, 30.0)
cap.set(cv.CAP_PROP_FOURCC, codec)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
Detector = HandDetector(maxHands=1)
classifer = Classifier("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Model/Numbers CNN Model/Sign Language Numbers Classifier_main1.h5","E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Model/Numbers CNN Model/labels.txt")

offset = 20
imgsize = 300
counter = 0
count = 0
labels = ["1","10","2","3","4","5","6","7","8","9"]

tutorial = cv.imread("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Images_Hand_Signs_Tutorials/Numbers_Hand_Signs_1.png",1)
while True:
    Success, img = cap.read()
    img = img.copy()
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
            prediction, index = classifer.getPrediction(imgextra)

        else:            #Width is greater
            k = imgsize / w
            hcal = math.ceil(k * h)
            imgResize = cv.resize(imgcrop, (imgsize, hcal))
            hgap = math.ceil((imgsize-hcal)/2)              #Put the image in the Middle
            imgextra[hgap:hcal+hgap, :] = imgResize         #Putting in the white Image
            prediction, index = classifer.getPrediction(imgextra)

        #Going Back to interface Options
        cv.rectangle(img, (0, 0), (90,90), (0, 0, 255), cv.FILLED)
        cv.putText(img, "X", (15,73),cv.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 5)
        lmList = hands[0]['lmList']
        x1,y1 = lmList[8][0:2]
        fingers = Detector.fingersUp(hands[0])
        if fingers[1] and fingers[2]:
            if 1170<=x1<=1280 and 0<=y1<=150:
                cv.destroyWindow("Image")
                cv.destroyWindow("Tutorial")
                img[:] = (0, 0, 0)
                cv.putText(img, 'Loading...', (300, 400), cv.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 5)
                cv.imshow("Image",img)
                cv.waitKey(1)
            if 1180<=x1<=1280 and 0<=y1<=100:
                print("Loading....")
                exec(open("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/InterFace/main.py").read())

        cv.putText(img, labels[index], (x, y-20), cv.FONT_HERSHEY_COMPLEX, 2, (255,0,255), 2)
        count += 1
        if count % 20 == 0:
            if labels[index] == "1":
                    playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/Numbers Sounds/1.mp3")
                    count = 0
            elif labels[index] == "2":
                    playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/Numbers Sounds/2.mp3")
                    count = 0
            elif labels[index] == "3":
                    playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/Numbers Sounds/3.mp3")
                    count = 0
            elif labels[index] == "4":
                    playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/Numbers Sounds/4.mp3")
                    count = 0
            elif labels[index] == "5":
                    playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/Numbers Sounds/5.mp3")
                    count = 0
            elif labels[index] == "6":
                    playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/Numbers Sounds/6.mp3")
                    count = 0
            elif labels[index] == "7":
                    playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/Numbers Sounds/7.mp3")
                    count = 0
            elif labels[index] == "8":
                    playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/Numbers Sounds/8.mp3")
                    count = 0
            elif labels[index] == "9":
                    playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/Numbers Sounds/9.mp3")
                    count = 0
            elif labels[index] == "10":
                    playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/Numbers Sounds/10.mp3")
                    count = 0
    cv.imshow("Image",img)
    cv.imshow("Tutorial", tutorial)
    cv.waitKey(1)
