import pyautogui

def MoveArrow(side, times):
    count = 0
    while count < times:
        pyautogui.press(side, interval=0)
        count+=1
