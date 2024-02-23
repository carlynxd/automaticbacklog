import pyautogui
from src import movearrow
import time
import clipboard

def VerifyStatus():
    global itemID
    global status
    if pyautogui.locateOnScreen(image=".\images\pausadostatus.png", confidence=0.7):
        status = True
        movearrow.MoveArrow(times=18, side="left")
        img = pyautogui.locateCenterOnScreen(image=".\images\id.png", confidence=0.7)
        pyautogui.moveTo(img.x, img.y+120)
        time.sleep(2)
        pyautogui.click
        time.sleep(1)
        pyautogui.doubleClick(interval=0.1)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        itemID = clipboard.paste()
        return
    else:
        status = False
        itemID = ""
        print('Status diferente')
        movearrow.MoveArrow(times=18, side="left")
        return
