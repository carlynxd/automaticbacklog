import main
import pyautogui
import time
import clipboard

def EmailBase():
    global itemID
    global solic
    global desc
    global reference
    global message
    main.SearchClick(image=".\images\sheetsico.png", confianca=0.7)
    time.sleep(2)
    img = pyautogui.locateCenterOnScreen(image=".\images/reference.png", confidence=0.9)
    pyautogui.moveTo(img.x, img.y+120, duration=1)
    time.sleep(2)
    pyautogui.click
    time.sleep(1)
    pyautogui.doubleClick(interval=0.1)
    time.sleep(1)
    #copiando referencia
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    reference = clipboard.paste()
    #copiando descrição
    pyautogui.move(xOffset=+350, yOffset=0, duration=1)
    time.sleep(2)
    pyautogui.click
    time.sleep(1)
    pyautogui.doubleClick(interval=0.1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    desc = clipboard.paste()
    #copiar solicitante
    pyautogui.move(xOffset=+450, yOffset=0, duration=1)
    time.sleep(2)
    pyautogui.click
    time.sleep(1)
    pyautogui.doubleClick(interval=0.1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    solic = clipboard.paste()
    print(desc)
    print(reference)
    message = clipboard.copy(f'Olá, {solic}\n\nO item \"{itemID} {reference}\", foi testado e liberado para atualização.\n\nPara você conseguir verificá-lo, basta atualizar o sistema para a versão mais recente.\nSegue a descrição do que foi desenvolvido:\n\n{desc}\n\nCaso tenha alguma dúvida, ou queira tratar sobre algum ponto específico do item atualizado, nossa equipe de suporte está à disposição.\n\nAgradecemos a sua atenção, tenha um ótimo dia!\n\nAtenciosamente,')
    time.sleep(1)
    main.SearchClick(image="./images/closerasc.png", confianca=0.7)
    time.sleep(1)
