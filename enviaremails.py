# coding=UTF-8

import pyautogui
import time
itemID = "124124"
solic = "Carlos"
refitem = "Alterar a exibição da grid entre operações First e Last Mile."
descitem = "descrição"


def SearchClick(image, confianca):
    img = pyautogui.locateCenterOnScreen(image, confidence=confianca)
    pyautogui.moveTo(img.x, img.y, duration=1)
    pyautogui.click()


print("tamo vindo")
if pyautogui.locateOnScreen(image=".\images\errorgmail.png"):
    SearchClick(image=".\images\composeemail.png", confianca=0.7)
    time.sleep(1)
    img = pyautogui.locateCenterOnScreen(image=".\images/newmessage.png", confidence=0.7)
    pyautogui.moveTo(img.x, img.y+110,duration=1)
    time.sleep(1)
    pyautogui.click()
    pyautogui.write(itemID, interval=0.1)
    pyautogui.move(yOffset=30, xOffset=0)
    pyautogui.click()
    pyautogui.write(f"Ola, {solic} O item \"{refitem}.\", foi testado e liberado para atualização.", interval=0.1)
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.write("Para voce conseguir verifica-lo, basta atualizar o sistema para a versao mais recente", interval=0.001)
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.write(f"Segue a descricao do que foi desenvolvido: {descitem}", interval=0.1)
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.write("Caso tenha alguma duvida, ou queira tratar sobre algum ponto especifico do item atualizado, nossa equipe de suporte esta a disposicao. \n\nAgradecemos a sua atencao, tenha um otimo dia! Atenciosamente")
    time.sleep(1)
    pyautogui.keyDown("ctrl")
    pyautogui.press("+")
    pyautogui.press("+")
    pyautogui.press("+")
    pyautogui.keyUp("ctrl")
    erro = pyautogui.locateOnScreen(image="./images/redsnake.png", confidence=0.7)
    while erro:
        pyautogui.moveTo(erro.x, erro.y)
        time.sleep(1)
        erro = pyautogui.locateOnScreen(image="./images/redsnake.png", confidence=0.7)