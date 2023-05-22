# _*_ coding: utf-8 _*_

import time
import pyautogui
from datetime import datetime
import clipboard
import searchstatus
import movearrow
import verifystatus
import verifyemail
import searchclick
import returnbacklog

User = "Carlos"

itemID = ""
vezes = 3
sendemail = True
status = True
today = datetime.today()
todayright = today.strftime(f'%d/%m')
ddspath = False
reference = ""
desc = ""
solic = ""
message = ""

for i in range(vezes):
    count = i+1
    print("Iniciando processo de automatização")
    time.sleep(2)
    searchclick.SearchClick(image="./images/id.png", confianca=0.8)
    time.sleep(1)
    movearrow.MoveArrow(times=count, side="down")
    movearrow.MoveArrow(times=18, side="right")
    searchstatus.SearchStatus()
    time.sleep(2)
    verifystatus.VerifyStatus()
    if status == True:
        print(itemID)
        verifyemail.VerifyEmail(itemID=itemID)
        returnbacklog.ReturnBackLog()
    else:
        print("Status Invalido, passando para o próximo")
