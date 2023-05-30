import pyautogui
import time
from src import searchclick, movearrow
from datetime import datetime
today = datetime.today()
todayright = today.strftime(f'%d/%m')


def ReturnBackLog(user, ddspath, sendemail, itemID):
    searchclick.SearchClick(image=".\images\sheetsico.png", confianca=0.7)
    time.sleep(1)
    searchclick.SearchClick(image="./images/id.png", confianca=0.8)
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
        pyautogui.write(f"{todayright} - {user}: O Email foi enviado com sucesso!! :D - ass: Lynbot", interval=0.1)
        searchclick.SearchClick(image=".\images\obsteste.png", confianca=0.7)
        movearrow.MoveArrow(times=6, side="left")
        img = pyautogui.locateCenterOnScreen("./images/status.png")
        pyautogui.moveTo(img.x, img.y+120)
        time.sleep(1)
        pyautogui.doubleClick(duration=0.1)
        time.sleep(1)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(1)
        pyautogui.write("7.1 Finalizado", interval=0.1)
        time.sleep(1)
        searchclick.SearchClick(image="./images/status.png", confianca=0.7)
        movearrow.MoveArrow(times=14, side="left")
    if sendemail == True and ddspath == True:
        pyautogui.write(f"{todayright} - {user}: O Email foi enviado para o email de suporte da DDS Verifique o motivo - ass: Lynbot", interval=0.1)
        searchclick.SearchClick(image=".\images\obsteste.png", confianca=0.7)
        movearrow.MoveArrow(times=20, side="left")
    elif sendemail == False:
        pyautogui.write(f"{todayright} - {user}: O Email nao foi enviado, foi criado um rascunho com assunto {itemID} no email de suporte da DDS, selecione o destinatário para enviar - ass: Lynbot", interval=0.1)
        searchclick.SearchClick(image=".\images\obsteste.png", confianca=0.7)
        movearrow.MoveArrow(times=20, side="left")