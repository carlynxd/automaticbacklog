import string
import webbrowser as wb
import time
import main
import pyautogui
import os as os

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
openchrome()
time.sleep(2)
confirmuser()
time.sleep(60)
pyautogui.hotkey("CTRL", "+")
pyautogui.hotkey("CTRL", "+")
pyautogui.hotkey("CTRL", "+")
time.sleep(2)
try:
    main.main()
    pyautogui.hotkey("CTRL", "-")
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
    pyautogui.hotkey("CTRL", "-")
    time.sleep(3)
    os.system("shutdown /s /t 1")
