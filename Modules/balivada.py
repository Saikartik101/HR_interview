import time
from threading import Thread
import pyautogui as pg

def rmna():
    time.sleep(11)
    pg.press('esc',presses = 1)


krm = Thread(target=rmna)
krm.start()