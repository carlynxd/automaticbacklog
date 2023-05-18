# _*_ coding: utf-8 _*_

import time
import pyautogui
from datetime import datetime
import clipboard

User = "Willian"
itemID = ""
vezes = 1
sendemail = True
status = True
today = datetime.today()
todayright = today.strftime(f'%d/%m')
ddspath = False
reference = ""
desc = ""

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
    global status
    global itemID
    if pyautogui.locateOnScreen(image=".\images\pausadostatus.png"):
        status = True
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
        itemID = clipboard.paste()

    else:
        status = False
        print('Status diferente')
        MoveArrow(times=18, side="left")

def VerifyEmail():
    global ddspath
    global sendemail
    SearchClick(image=".\images\gmail.png", confianca=0.7)
    time.sleep(1)
    if pyautogui.locateOnScreen(image=".\images\searchico.png", confidence=0.8) or pyautogui.locateOnScreen(image=".\images\searchicowhite.png"):
        if pyautogui.locateOnScreen(image=".\images\searchico.png", confidence=0.8):
            SearchClick(image=".\images\searchico.png", confianca=0.7)
        elif pyautogui.locateOnScreen(image=".\images\searchicowhite.png"):
            SearchClick(image=".\images\searchicowhite.png", confianca=0.7)
        time.sleep(1)
        pyautogui.move(xOffset=60, yOffset=0)
        time.sleep(1)
        pyautogui.click(interval=0.1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(f"in:sent \"{itemID}\" ")
        pyautogui.press("ENTER")
        time.sleep(3)
        if pyautogui.locateOnScreen(image=".\images\errorgmail.png"):
            sendemail = False
            SearchClick(image=".\images\composedemail.png", confianca=0.7)
            print(f"Email não enviado para o item {itemID}")
        else: 
            sendemail = True
            SearchClick(image=".\images\searchico.png", confianca=0.7)
            pyautogui.move(xOffset=120, yOffset=150, duration=1)
            pyautogui.click()
            pyautogui.move(xOffset=-20, yOffset=40, duration=1)
            time.sleep(5)
            if pyautogui.locateOnScreen(image=".\images\emailddsinfo.png", confidence=0.7):
                ddspath = True
            else:
                ddspath = False

    else:
        print("Não foi possível encontrar o icone de lupa")


def ReturnBackLog():
    global sendemail
    SearchClick(image=".\images\sheetsico.png", confianca=0.7)
    time.sleep(1)
    SearchClick(image="./images/id.png", confianca=0.8)
    MoveArrow(times=20, side="right")
    img = pyautogui.locateCenterOnScreen(image=".\images\obsteste.png", confidence=0.7)
    pyautogui.moveTo(img.x, img.y+120)
    time.sleep(1)
    pyautogui.doubleClick(duration=0.1)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(1)
    MoveArrow(times=1, side="left")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "enter")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "enter")
    time.sleep(1)
    MoveArrow(times=2, side="up")
    if sendemail == True and ddspath == False:
        pyautogui.write(f"{todayright} - {User}: O Email foi enviado com sucesso!! :D - ass: Lynbot", interval=0.1)
        SearchClick(image=".\images\obsteste.png", confianca=0.7)
        MoveArrow(times=20, side="left")
    if sendemail == True and ddspath == True:
        pyautogui.write(f"{todayright} - {User}: O Email foi enviado para o email de suporte da DDS Verifique o motivo - ass: Lynbot", interval=0.1)
        SearchClick(image=".\images\obsteste.png", confianca=0.7)
        MoveArrow(times=20, side="left")
    elif sendemail == False:
        pyautogui.write(f"{todayright} - {User}: O Email nao foi enviado, deve ser enviado manualmente - ass: Lynbot", interval=0.1)
        SearchClick(image=".\images\obsteste.png", confianca=0.7)
        MoveArrow(times=20, side="left")

def EmailBase():
    global desc
    global reference
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
    reference = clipboard.paste()
    pyautogui.move(xOffset=+350, yOffset=0, duration=1)
    time.sleep(2)
    pyautogui.click
    time.sleep(1)
    pyautogui.doubleClick(interval=0.1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    desc = clipboard.paste()
    print(desc)
    print(reference)




# for i in range(vezes):
#     count = i+1
#     print("Iniciando processo de automatização")
#     time.sleep(2)
#     SearchClick(image="./images/id.png", confianca=0.8)
#     time.sleep(1)
#     MoveArrow(times=count, side="down")
#     MoveArrow(times=18, side="right")
#     SearchStatus()
#     time.sleep(2)
#     VerifyStatus()
#     if status == True:
#         print(itemID)
#         VerifyEmail()
#         ReturnBackLog()
#     else:
#         print("Status Invalido, passando para o próximo")
        
EmailBase()