import pyautogui
import time
from src import searchclick, movearrow
from datetime import datetime
today = datetime.today()
todayright = today.strftime(f'%d/%m')


def ReturnBackLog(user, ddspath, sendemail, itemID):
    global finalizado
    searchclick.SearchClick(image=".\images\sheetsico.png", confianca=0.7)
    time.sleep(1)
    searchclick.SearchClick(image="./images/id.png", confianca=0.7)
    time.sleep(1)
    movearrow.MoveArrow(times=20, side="right")
    img = pyautogui.locateCenterOnScreen(image=".\images\obsteste.png", confidence=0.7)
    pyautogui.moveTo(img.x, img.y+120)
    time.sleep(1)
    pyautogui.doubleClick(duration=0.1)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(1)
    movearrow.MoveArrow(times=1, side="left")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "enter")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "enter")
    time.sleep(1)
    movearrow.MoveArrow(times=2, side="up")
    if sendemail == True and ddspath == False:
        pyautogui.write(f"{todayright} - {user}: O Email foi enviado com sucesso!!", interval=0.1)
        searchclick.SearchClick(image=".\images\obsteste.png", confianca=0.7)
        movearrow.MoveArrow(times=6, side="left")
        img = pyautogui.locateCenterOnScreen("./images/status.png", confidence=0.8)
        pyautogui.moveTo(img.x, img.y+120)
        time.sleep(1)
        pyautogui.doubleClick(duration=0.1)
        time.sleep(1)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(1)
        pyautogui.write("7.1 Finalizado", interval=0.1)
        time.sleep(1)
        pyautogui.hotkey('shift', 'tab')
        pyautogui.press('enter')
        pyautogui.write(f"{todayright}")
        pyautogui.hotkey('shift', 'tab')
        movearrow.MoveArrow(times=14, side="left")
        finalizado = True
        return
    if sendemail == True and ddspath == True:
        pyautogui.write(f"{todayright} - {user}: O Email foi enviado para o email de suporte da DDS Verifique o motivo. Foi criado um rascunho com o ID do item no email de suporte.", interval=0.1)
        searchclick.SearchClick(image=".\images\obsteste.png", confianca=0.7)
        movearrow.MoveArrow(times=20, side="left")
        finalizado = False
        return
    elif sendemail == False:
        pyautogui.write(f"{todayright} - {user}: O Email nao foi enviado, foi criado um rascunho com assunto {itemID} no email de suporte da DDS, selecione o destinatário para enviar ", interval=0.1)
        searchclick.SearchClick(image=".\images\obsteste.png", confianca=0.7)
        movearrow.MoveArrow(times=20, side="left")
        finalizado = False
        return