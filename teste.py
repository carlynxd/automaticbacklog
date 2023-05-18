import pyautogui
import time

def SearchClick(image, confianca):
    img = pyautogui.locateCenterOnScreen(image, confidence=confianca)
    pyautogui.moveTo(img.x, img.y, duration=1)
    pyautogui.click()

img = pyautogui.locateCenterOnScreen(image=".\images/reference.png", confidence=0.9)
pyautogui.moveTo(img.x, img.y+120, duration=1)
time.sleep(2)
pyautogui.click
time.sleep(1)
pyautogui.doubleClick(interval=0.1)
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
pyautogui.move(xOffset=+350, yOffset=0, duration=1)
time.sleep(2)
pyautogui.click
time.sleep(1)
pyautogui.doubleClick(interval=0.1)
