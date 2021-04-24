import pyautogui
import time

pyautogui.alert('O código vai começar. Não use nada do seu computador!')
pyautogui.PAUSE = 2

#abrir o google drive no computador

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')

#entrar na minha área de trabalho
pyautogui.hotkey('winleft', 'd')

#clicar no arquivo que irá arrastar
pyautogui.moveTo(1332, 439)
pyautogui.mouseDown()
pyautogui.moveTo(1102, 922)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.mouseUp()

time.sleep(5)

pyautogui.alert('O código acabou. Pode usar seu computador.')





