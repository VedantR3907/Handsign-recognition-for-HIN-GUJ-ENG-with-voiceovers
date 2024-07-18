from turtle import back, shape
import cv2 as cv
import cvzone as cz
from cvzone.HandTrackingModule import *

######################################################################################
#Setting Window
cap = cv.VideoCapture(0, cv.CAP_DSHOW)
codec = 0x47504A4D  # MJPG
cap.set(cv.CAP_PROP_FPS, 30.0)
cap.set(cv.CAP_PROP_FOURCC, codec)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)

Detector = HandDetector(maxHands=1)

background_img = cv.imread("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/InterFace/welcome background/background_img.png")
background_img2 = cv.imread("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/InterFace/welcome background/background_img_2page.png")

count = 0
while True:
    SUCCESS, img = cap.read()
    img = cv.flip(img, 1)

    hand, img = Detector.findHands(img)

    img_first = cv.addWeighted(img, 0.12, background_img, 1, 0)



    ######################################################################################
    #Writing Text on the Screen
    cv.putText(img_first, 'Sign Language', (510, 360), 0, 1.4, (69, 68, 68), 3)
    cv.putText(img_first, 'Recognition', (510, 405), 0, 1.4, (69, 68, 68), 3)
    cv.putText(img_first, 'Wave your Hand to Start', (440, 650), 0, 1, (84, 82, 82), 3)
    cv.putText(img_first, 'Creator', (1165, 640), 0, 0.8, (115, 109, 109), 1)
    cv.line(img_first, (1165, 645), (1260,645), (115, 109, 109), 1)
    cv.putText(img_first, 'Vedant A. Rajpurohit', (1005, 680), 0, 0.8, (115, 109, 109), 2)
    cv.putText(img_first, 'Manan C. Patel', (1070, 712), 0, 0.8, (115, 109, 109), 2)
    ######################################################################################

    if hand:
        hand1 = hand[0]
        lmlist = hand1["lmList"]
        x1, y1 = lmlist[8][:2]
        fingers = Detector.fingersUp(hand1)

        if fingers == [1,1,1,1,1]:
            count += 1
            if count == 20:
                cv.destroyWindow("Image")
                img = background_img2
                recta = img.copy()
                cv.rectangle(recta, (0,0), (1280,720),(0,0,0),-1)
                img = cv.addWeighted(recta, 0.5, img, 0.5, 0)
                cv.putText(img, 'Loading...', (370, 350), 0, 4, (255, 255, 255), 4)
                cv.imshow("Image",img)
                cv.waitKey(1)
                print("Go to next Page")
                exec(open("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/InterFace/main.py").read())

    cv.imshow("Image",img_first)

    cv.waitKey(1)