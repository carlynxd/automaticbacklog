import time, pyautogui
import re
from src import writeemail

def SearchClick(image, confianca):
    img = pyautogui.locateCenterOnScreen(image, confidence=confianca)
    pyautogui.moveTo(img.x, img.y, duration=0)
    pyautogui.click()

def VerifyEmail(itemID):
    global cliente
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
        if pyautogui.locateCenterOnScreen(image=".\images\errorgmail.png", confidence=0.8):
            sendemail = False
            ddspath = False
            time.sleep(1)
            time.sleep(1)
            writeemail.emailbase(itemID=itemID)
            cliente = writeemail.cliente
            writeemail.sendemail(itemID=itemID, cliente=cliente)
            time.sleep(1)
            print(f"Email não enviado para o item {itemID}")
            return 
        else: 
            sendemail = True
            SearchClick(image=".\images\searchico.png", confianca=0.7)
            pyautogui.move(xOffset=120, yOffset=150, duration=1)
            pyautogui.click()
            pyautogui.move(xOffset=-20, yOffset=40, duration=1)
            time.sleep(5)
            if pyautogui.locateCenterOnScreen(image=".\images\emailddsinfo.png", confidence=0.7):
                ddspath = True
                writeemail.emailbase(itemID=itemID)
                solic = writeemail.solic
                if "DDS" in solic and ddspath == True:
                    ddspath = False
                    return
                else:
                    cliente = writeemail.cliente
                    writeemail.sendemail(itemID=itemID, cliente=cliente)
                    return 

            else:
                ddspath = False
                return 
    else:
        print("Não foi possível encontrar o icone de lupa")
