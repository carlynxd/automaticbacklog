import time
import pyautogui
from datetime import datetime
import clipboard

User = "Carlos"
itemID = ""
vezes = 5

def SearchClick(image, confianca):
    img = pyautogui.locateCenterOnScreen(image, confidence=confianca)
    pyautogui.moveTo(img.x, img.y, duration=1)
    pyautogui.click()

def MoveArrow(side, times):
    count = 0
    while count < times:
        pyautogui.press(side, interval=0)
        count+=1

def SearchStatus():
    img = pyautogui.locateCenterOnScreen(image=".\images\status.png", confidence=0.8)
    if img:
        print("Aba \" Status \" encontrado")
    else:
        print("Status não encontrado")
        

def VerifyStatus():
    if pyautogui.locateOnScreen(image=".\images\pausadostatus.png"):
        MoveArrow(times=18, side="left")
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

    else:
        print('Status diferente')
        MoveArrow(times=1, side="down")
        MoveArrow(times=18, side="left")
        print("Iniciando processo de automatização")
        time.sleep(2)
        SearchClick(image="./images/id.png", confianca=0.8)
        time.sleep(1)
        MoveArrow(times=1, side="down")
        MoveArrow(times=18, side="right")
        SearchStatus()
        time.sleep(2)
        VerifyStatus()
        itemID = clipboard.paste()
        print(itemID)
        VerifyEmail()
        ReturnBackLog()
        

def VerifyEmail():
    SearchClick(image=".\images\gmail.png", confianca=0.7)
    time.sleep(1)
    if pyautogui.locateOnScreen(image=".\images\searchico.png", confidence=0.8):
        SearchClick(image=".\images\searchico.png", confianca=0.7)
        time.sleep(1)
        pyautogui.move(xOffset=60, yOffset=0)
        time.sleep(1)
        pyautogui.click(interval=0.1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(f"in:sent \"{itemID}\" ")
        pyautogui.press("ENTER")
    elif pyautogui.locateOnScreen(image=".\images\searchicowhite.png"):
        SearchClick(image=".\images\searchicowhite.png", confianca=0.7)
        time.sleep(1)
        pyautogui.move(xOffset=60, yOffset=0)
        time.sleep(1)
        pyautogui.click(interval=0.1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(f"in:sent \"{itemID}\" ")
        pyautogui.press("ENTER")
    else:
        print("Não foi possível encontrar o icone de lupa")


def ReturnBackLog():
    SearchClick(image=".\images\sheetsico.png", confianca=0.7)
    time.sleep(1)
    SearchClick(image="./images/id.png", confianca=0.8)
    MoveArrow(times=37, side="right")
    img = pyautogui.locateCenterOnScreen(image=".\images\obsteste.png", confidence=0.7)
    pyautogui.moveTo(img.x, img.y+120)
    time.sleep(1)
    pyautogui.doubleClick(duration=0.1)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(1)
    MoveArrow(times=1, side="left")
    pyautogui.hotkey("ctrl", "enter")
    pyautogui.write(f"{User}: O Email foi enviado com sucesso", interval=0.1)
    SearchClick(image=".\images\obsteste.png", confianca=0.7)
    MoveArrow(times=37, side="left")


for i in range(vezes):
    count = i+1
    print("Iniciando processo de automatização")
    time.sleep(2)
    SearchClick(image="./images/id.png", confianca=0.8)
    time.sleep(1)
    if count == 2:
        MoveArrow(times=2, side="down")
        MoveArrow(times=18, side="right")
        SearchStatus()
        time.sleep(2)
        VerifyStatus()
        itemID = clipboard.paste()
        print(itemID)
        VerifyEmail()
        ReturnBackLog()
    else:
        MoveArrow(times=1, side="down")
        MoveArrow(times=18, side="right")
        SearchStatus()
        time.sleep(2)
        VerifyStatus()
        itemID = clipboard.paste()
        print(itemID)
        VerifyEmail()
        ReturnBackLog()
