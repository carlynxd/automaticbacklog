import os
import time
import pyautogui
import main
from src import movearrow, searchclick, searchstatus, verifyemail, verifystatus, returnbacklog

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

fontsize()
main.main()
