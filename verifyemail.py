import pyautogui
import time
import writeemail

def SearchClick(image, confianca):
    img = pyautogui.locateCenterOnScreen(image, confidence=confianca)
    pyautogui.moveTo(img.x, img.y, duration=1)
    pyautogui.click()

def VerifyEmail(itemID):
    global ddspath
    global sendemail
    SearchClick(image=".\images\gmail.png", confianca=0.7)
    time.sleep(3)
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
            ddspath = False
            time.sleep(1)
            time.sleep(1)
            writeemail.emailbase(itemID=itemID)
            writeemail.sendemail(itemID=itemID)
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
            if pyautogui.locateOnScreen(image=".\images\emailddsinfo.png", confidence=0.7):
                ddspath = True
                return 
            else:
                ddspath = False
                return 
    else:
        print("Não foi possível encontrar o icone de lupa")
