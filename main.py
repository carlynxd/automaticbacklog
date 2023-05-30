# _*_ coding: utf-8 _*_

import time
import sys

from src import movearrow, searchclick, searchstatus, verifyemail, verifystatus, returnbacklog

user = "Carlos"
run = True
controller = 0
dif = 0

while run:
    controller +=1
    print("Iniciando processo de automatização")
    time.sleep(2)
    searchclick.SearchClick(image="./images/id.png", confianca=0.8)
    time.sleep(1)
    movearrow.MoveArrow(times=controller, side="down")
    movearrow.MoveArrow(times=18, side="right")
    searchstatus.SearchStatus()
    time.sleep(2)
    verifystatus.VerifyStatus()
    itemID = verifystatus.itemID
    status = verifystatus.status
    if status == True:
        print(itemID)
        verifyemail.VerifyEmail(itemID=itemID)
        ddspath = verifyemail.ddspath
        sendemail = verifyemail.sendemail
        returnbacklog.ReturnBackLog(itemID=itemID,ddspath=ddspath, sendemail=sendemail, user=user)
    else:
        dif +=1
        print("Status Invalido, passando para o próximo")
        if dif > 3:
            run = False
