import math
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import cv2 as cv
import numpy as np
from playsound import playsound
from PIL import ImageFont, ImageDraw, Image


cap = cv.VideoCapture(0, cv.CAP_DSHOW)
codec = 0x47504A4D  # MJPG
cap.set(cv.CAP_PROP_FPS, 30.0)
cap.set(cv.CAP_PROP_FOURCC, codec)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
Detector = HandDetector(maxHands=1)
classifer = Classifier("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Model/ISL CNN Model/Sign Language ISL Classifier_main1.h5","E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Model/ISL CNN Model/labels.txt")
fontpath = "E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Data/ISL DATA/kurti-dev-040-bold.ttf"
font = ImageFont.truetype(fontpath, 54)

offset = 20
imgsize = 300
counter = 0
count = 0
labels = ["d","[k","x","|","M","p","N","t",">","_","V","B","<",".k","r","Fk","n","u","i","Q","c","Hk","e",";","j","y","o","l","g"]

tutorial = cv.imread("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Images_Hand_Signs_Tutorials/ISL_Hand_Signs_1.png",1)
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

        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        draw.text((x, y-65),  labels[index], font = font, fill = (255,0,255))
        img = np.array(img_pil)
#["d","[k","x","|","M","p","N","t",">","_","V","B","<",".k","r","Fk","n","u","i","Q","c","Hk","e",";","j","y","o","l","g"]
        count += 1
        if count % 20 == 0:
            if labels[index] == "d":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/A.mp3")
                count = 0
            elif labels[index] == "[k":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/B.mp3")
                count = 0
            elif labels[index] == "x":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/C.mp3")
                count = 0
            elif labels[index] == "|":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/D.mp3")
                count = 0
            elif labels[index] == "M":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/E.mp3")
                count = 0
            elif labels[index] == "p":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/F.mp3")
                count = 0
            elif labels[index] == "N":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/G.mp3")
                count = 0
            elif labels[index] == "t":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/H.mp3")
                count = 0
            elif labels[index] == ">":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/I.mp3")
                count = 0
            elif labels[index] == "_":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/J.mp3")
                count = 0
            elif labels[index] == "V":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/K.mp3")
                count = 0
            elif labels[index] == "B":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/L.mp3")
                count = 0
            elif labels[index] == "<":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/M.mp3")
                count = 0
            elif labels[index] == ".k":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/N.mp3")
                count = 0
            elif labels[index] == "r":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/O.mp3")
                count = 0
            elif labels[index] == "Fk":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/P.mp3")
                count = 0
            elif labels[index] == "n":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/Q.mp3")
                count = 0
            elif labels[index] == "u":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/R.mp3")
                count = 0
            elif labels[index] == "i":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/S.mp3")
                count = 0
            elif labels[index] == "Q":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/T.mp3")
                count = 0
            elif labels[index] == "c":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/U.mp3")
                count = 0
            elif labels[index] == "Hk":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/V.mp3")
                count = 0
            elif labels[index] == "e":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/W.mp3")
                count = 0
            elif labels[index] == ";":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/X.mp3")
                count = 0
            elif labels[index] == "j":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/Y.mp3")
                count = 0
            elif labels[index] == "y":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/Z.mp3")
                count = 0
            elif labels[index] == "o":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/Z1.mp3")
                count = 0
            elif labels[index] == "l":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/Z2.mp3")
                count = 0
            elif labels[index] == "g":
                playsound("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Sounds/ISL Sounds/Z3.mp3")
                count = 0

    cv.imshow("Image",img)
    cv.imshow("Tutorial", tutorial)
    cv.waitKey(1)
