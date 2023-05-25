# _*_ coding: utf-8 _*_

import time
import searchstatus
import movearrow
import verifystatus
import verifyemail
import searchclick
import returnbacklog

user = "Carlos"
vezes = 3

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
    itemID = verifystatus.itemID
    status = verifystatus.status
    if status == True:
        print(itemID)
        verifyemail.VerifyEmail(itemID=itemID)
        ddspath = verifyemail.ddspath
        sendemail = verifyemail.sendemail
        returnbacklog.ReturnBackLog(itemID=itemID,ddspath=ddspath, sendemail=sendemail, user=user)
    else:
        print("Status Invalido, passando para o próximo")
