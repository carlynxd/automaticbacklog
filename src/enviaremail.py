import pyautogui
import time
import searchclick

def sendemail(itemID):
    if pyautogui.locateOnScreen(image=".\images\errorgmail.png"):
        searchclick.SearchClick(image=".\images\composeemail.png", confianca=0.7)
        time.sleep(1)
        img = pyautogui.locateCenterOnScreen(image=".\images/newmessage.png", confidence=0.7)
        pyautogui.moveTo(img.x, img.y+110,duration=1)
        time.sleep(1)
        pyautogui.click()
        pyautogui.write(itemID, interval=0.1)
        pyautogui.move(yOffset=30, xOffset=0)
        pyautogui.click()
        time.sleep(1)
        pyautogui.hotkey("CTRL", "v")
        time.sleep(1)
