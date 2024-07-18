import cvzone as cz
import cv2 as cv
from cvzone.HandTrackingModule import *
Detector = HandDetector(maxHands=1)

asl_img = cv.imread("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/InterFace/welcome background/ASL_back.png")
isl_img = cv.imread("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/InterFace/welcome background/ISL_back.png")
num_img = cv.imread("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/InterFace/welcome background/numbers_back.png")
######################################################################################
#Setting Window
cap = cv.VideoCapture(0, cv.CAP_DSHOW)
codec = 0x47504A4D  # MJPG
cap.set(cv.CAP_PROP_FPS, 30.0)
cap.set(cv.CAP_PROP_FOURCC, codec)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
flag = 0

while True:
    SUCCESS, img = cap.read()
    img = cv.flip(img, 1)

    hand, img = Detector.findHands(img)
    if hand:
        hand1 = hand[0]
        lmlist = hand1["lmList"]
        x1, y1 = lmlist[8][:2]
        fingers = Detector.fingersUp(hand1)
        if fingers[1] and fingers[2]:  #Both Fingers UP

            #ASL Game
            if 115<=x1<=415 and 60<=y1<=360:
                flag = 1
                cv.destroyWindow("Image")
                img[:] = (0, 0, 0)
                cv.putText(img, 'Loading...', (300, 400), cv.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 5)
                cv.imshow("Image",img)
                cv.waitKey(1)
                print("Go to next Page")
            if 100<=x1<=400 and 50<=y1<=350:
                exec(open("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/ASL_Main_File/ASL Detection.py").read())
            
            #ISL Game
            if 850<=x1<=1160 and 90<=y1<=430:
                flag = 1
                cv.destroyWindow("Image")
                img[:] = (0, 0, 0)
                cv.putText(img, 'Loading...', (300, 400), cv.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 5)
                cv.imshow("Image",img)
                cv.waitKey(1)
                print("Go to next Page")
            if 885<=x1<=1140 and 130<=y1<=380:
                exec(open("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/ISL_Main_File/ISL Detection.py").read())
            
            #Numbers Game
            if 450<=x1<=750 and 90<=y1<=420:
                flag = 1
                cv.destroyWindow("Image")
                img[:] = (0, 0, 0)
                cv.putText(img, 'Loading...', (300, 400), cv.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 5)
                cv.imshow("Image",img)
                cv.waitKey(1)
                print("Go to next Page")
            if 490<=x1<=720 and 130<=y1<=380:
                exec(open("E:/Extra Codes/Python/Python Projects/Hand Sign Recognition/Numbers_Main_File/Numbers Detection.py").read())
            
    if flag == 0:
        img[100:400, 50:350] = asl_img
        img[100:400, 450:750] = num_img
        img[100:400, 850:1150] = isl_img
    cv.putText(img, 'Select Any from the 3', (img.shape[0]//2-150, 600), 0, 2.4, (255, 255, 255), 3)
    cv.imshow("Image", img)
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyWindow("Image")
        break