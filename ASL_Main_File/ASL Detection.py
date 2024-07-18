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
classifer = Classifier("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Model/ASL CNN Model/Sign Language ASL Classifier_main1.h5","E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Model/ASL CNN Model/labels.txt")

offset = 20
imgsize = 300
counter = 0
count = 0
labels = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

tutorial = cv.imread("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Images_Hand_Signs_Tutorials/ASL_Hand_Signs_1.png",1)
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
                if labels[index] == "A":
                    playsound('../Sounds/ASL Sounds/A.mp3')
                    count = 0
                elif labels[index] == "B":
                    playsound("../Sounds/ASL Sounds/B.mp3")
                    count = 0
                elif labels[index] == "C":
                    playsound("../Sounds/ASL Sounds/C.mp3")
                    count = 0
                elif labels[index] == "D":
                    playsound("../Sounds/ASL Sounds/D.mp3")
                    count = 0
                elif labels[index] == "E":
                    playsound("../Sounds/ASL Sounds/E.mp3")
                    count = 0
                elif labels[index] == "F":
                    playsound("../Sounds/ASL Sounds/F.mp3")
                    count = 0
                elif labels[index] == "G":
                    playsound("../Sounds/ASL Sounds/G.mp3")
                    count = 0
                elif labels[index] == "H":
                    playsound("../Sounds/ASL Sounds/H.mp3")
                    count = 0
                elif labels[index] == "I":
                    playsound("../Sounds/ASL Sounds/I.mp3")
                    count = 0
                elif labels[index] == "J":
                    playsound("../Sounds/ASL Sounds/J.mp3")
                    count = 0
                elif labels[index] == "K":
                    playsound("../Sounds/ASL Sounds/K.mp3")
                    count = 0
                elif labels[index] == "L":
                    playsound("../Sounds/ASL Sounds/L.mp3")
                    count = 0
                elif labels[index] == "M":
                    playsound("../Sounds/ASL Sounds/M.mp3")
                    count = 0
                elif labels[index] == "N":
                    playsound("../Sounds/ASL Sounds/N.mp3")
                    count = 0
                elif labels[index] == "O":
                    playsound("../Sounds/ASL Sounds/O.mp3")
                    count = 0
                elif labels[index] == "P":
                    playsound("../Sounds/ASL Sounds/P.mp3")
                    count = 0
                elif labels[index] == "Q":
                    playsound("../Sounds/ASL Sounds/Q.mp3")
                    count = 0
                elif labels[index] == "R":
                    playsound("../Sounds/ASL Sounds/R.mp3")
                    count = 0
                elif labels[index] == "S":
                    playsound("../Sounds/ASL Sounds/S.mp3")
                    count = 0
                elif labels[index] == "T":
                    playsound("../Sounds/ASL Sounds/T.mp3")
                    count = 0
                elif labels[index] == "U":
                    playsound("../Sounds/ASL Sounds/U.mp3")
                    count = 0
                elif labels[index] == "V":
                    playsound("../Sounds/ASL Sounds/V.mp3")
                    count = 0
                elif labels[index] == "W":
                    playsound("../Sounds/ASL Sounds/W.mp3")
                    count = 0
                elif labels[index] == "X":
                    playsound("../Sounds/ASL Sounds/X.mp3")
                    count = 0
                elif labels[index] == "Y":
                    playsound("../Sounds/ASL Sounds/Y.mp3")
                    count = 0
                elif labels[index] == "Z":
                    playsound("../Sounds/ASL Sounds/Z.mp3")
                    count = 0

    cv.imshow("Image",img)
    cv.imshow("Tutorial", tutorial)
    cv.waitKey(1)
