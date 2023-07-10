import pyautogui
import time
#pyautogui.alert('não mexa em nada!')
pyautogui.PAUSE = 0.5
pyautogui.keyDown('winleft')
pyautogui.keyUp('winleft')
pyautogui.typewrite('edge')
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')
time.sleep(10)
pyautogui.typewrite('https://web.whatsapp.com/')