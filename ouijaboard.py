import keyboard
import time

def google_search_removal(replace):
    keyboard.block_key('Enter')
    while True:
        if keyboard.is_pressed('Enter'):
            keyboard.send('ctrl+a')
            time.sleep(0.4)
            keyboard.send('backspace')
            keyboard.write(replace)
            keyboard.send('enter')
            break

string1 = "Why I will always be single"

google_search_removal(string1)