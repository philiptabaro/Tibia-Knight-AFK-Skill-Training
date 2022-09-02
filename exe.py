import pyautogui
import time
import random

time.sleep(5)

while True:

    textos = ['to on', 'to aqui', 'n mata a sheep pf']
    aleatorio = str(random.choice(textos))

    print(aleatorio)

    pyautogui.typewrite(str(aleatorio))
    pyautogui.press('enter')

    set1 = 1

    while set1 < 13:
        pyautogui.keyDown('ctrl')
        pyautogui.press('up')
        pyautogui.press('down')
        pyautogui.press('left')
        pyautogui.press('right')
        pyautogui.press('down')
        pyautogui.keyUp('ctrl')

        time.sleep(20)
        set1 += 1

    pyautogui.press('F3')

    time.sleep(40)

    set2 = 1

    while set2 < 10:
        pyautogui.press('F4')
        set2 += 1
        time.sleep(2)


