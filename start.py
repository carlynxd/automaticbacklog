import string
import webbrowser as wb
import time
import main
import pyautogui
import os as os
from src import movearrow, searchclick, searchstatus, verifyemail, verifystatus, returnbacklog

def openchrome():
    os.startfile('chrome.exe')
    wb.open("https://mail.google.com/mail/u/1/#inbox")
    wb.open("https://docs.google.com/spreadsheets/d/10PZjvFe79Ud1nG8d7oky2zOUVNvfqm8NIknAW06jqHA/edit#gid=0&fvid=1002099704")

def confirmuser():
    while True:
            img = pyautogui.locateCenterOnScreen(image="okbtn.png", confidence=0.7)
            if img:
                pyautogui.moveTo(img.x, img.y, duration=1)
                time.sleep(1)
                pyautogui.click()
                break
            else:
                print("procurando ok")
                time.sleep(5)


def fontsize():
    time.sleep(5)
    searchclick.SearchClick(image="./images/id.png", confianca=0.7)
    time.sleep(1)
    movearrow.MoveArrow(times=1, side="down")
    movearrow.MoveArrow(times=18, side="right")
    time.sleep(3)
    searchclick.SearchClick(image="./images/status.png", confianca=0.8)
    searchclick.SearchClick(image="./images/fontname.png", confianca=0.7)
    pyautogui.write("10")
    pyautogui.press("ENTER")



openchrome()
time.sleep(2)
confirmuser()
time.sleep(75)
pyautogui.hotkey("CTRL", "+")
pyautogui.hotkey("CTRL", "+")
fontsize()
time.sleep(2)
try:
    main.main()
    pyautogui.hotkey("CTRL", "-")
    pyautogui.hotkey("CTRL", "-")
    time.sleep(3)
    os.system("shutdown /s /t 1")
except:
    print('não foi encontrado o filtro de pendencia na tela, tentando novamente')
    time.sleep(60)
    main.main()
    pyautogui.hotkey("CTRL", "-")
    pyautogui.hotkey("CTRL", "-")
    time.sleep(3)
    os.system("shutdown /s /t 1")
