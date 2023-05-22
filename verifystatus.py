import pyautogui
import movearrow
import time
import clipboard

def VerifyStatus():
    if pyautogui.locateOnScreen(image=".\images\pausadostatus.png"):
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
        return itemID, status
    else:
        status = False
        print('Status diferente')
        movearrow.MoveArrow(times=18, side="left")
