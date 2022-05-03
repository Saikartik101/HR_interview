import time
import cv2

import mj
from threading import Thread

def speak():
    mj.stt("Before starting the interview,we need a quick picture of yours,please look at camera")
    mj.stt("three")
    time.sleep(0.5)
    mj.stt("two")
    time.sleep(0.5)
    mj.stt("one")

    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame = videoCaptureObject.read()
        cv2.imwrite("cand.jpg", frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def hello():
    return "karthik"


t13 = Thread(target=speak)
t13.start()