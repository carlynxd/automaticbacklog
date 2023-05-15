# _*_ coding: utf-8 _*_

import pyautogui
import time
nao = "não"
def SearchClick(image, confianca):
    img = pyautogui.locateCenterOnScreen(image, confidence=confianca)
    pyautogui.moveTo(img.x, img.y, duration=1)
    pyautogui.click()

SearchClick(image=".\images\searchico.png", confianca=0.7)
pyautogui.move(xOffset=120, yOffset=150, duration=1)
pyautogui.click()
pyautogui.move(xOffset=0, yOffset=40, duration=1)
time.sleep(3)
if pyautogui.locateOnScreen(image=".\images\emailddsinfo.png", confidence=0.7):
    print("É a DDS")
    time.sleep(2)
else:
    print("não é a dds")