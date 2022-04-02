import keyboard
import time
import winsound

def google_search_removal():
    keyboard.block_key('enter')
    while True:
        if keyboard.is_pressed('enter'):
            keyboard.send('ctrl+a')
            time.sleep(0.4)
            keyboard.send('backspace')
            keyboard.write("Why I will always be single")
            keyboard.send('enter')
            break
    keyboard.unblock_key('enter')


def minesweep_keys():
    while True:
        if keyboard.is_pressed('f'):
            winsound.Beep(2000, 3000)
            break
        elif keyboard.is_pressed('g') or keyboard.is_pressed('t') or keyboard.is_pressed('r') or keyboard.is_pressed('d') or keyboard.is_pressed('c') or keyboard.is_pressed('v'):
            winsound.Beep(5000, 200)
        elif keyboard.is_pressed('b') or keyboard.is_pressed('h') or keyboard.is_pressed('y') or keyboard.is_pressed('e') or keyboard.is_pressed('s') or keyboard.is_pressed('x'):
            winsound.Beep(4500, 200)
        elif keyboard.is_pressed('z') or keyboard.is_pressed('a') or keyboard.is_pressed('w') or keyboard.is_pressed('u') or keyboard.is_pressed('j') or keyboard.is_pressed('n'):
            winsound.Beep(4000, 200)


google_search_removal()

minesweep_keys()