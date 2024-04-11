import os
import numpy as np
import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 200)

hand_detector = HandDetector(maxHands=1, detectionCon=0.6)
while True:

    success, img = cap.read()
    hands, img = hand_detector.findHands(img)

    if hands:
        hand1 = hands[0]
        finger1 = hand_detector.fingersUp(hand1)
        print(finger1)


    ###-------------------- Display image background ------------------------###
    # cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow('window', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()