import pyautogui

def SearchStatus():
    img = pyautogui.locateCenterOnScreen(image=".\images\status.png", confidence=0.8)
    if img:
        print("Aba \" Status \" encontrado")
    else:
        print("Status não encontrado")
        