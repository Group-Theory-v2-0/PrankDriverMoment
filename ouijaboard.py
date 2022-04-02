import keyboard

import time

def google_search_removal(replace):
    keyboard.block_key('enter')
    while True:
        if keyboard.is_pressed('enter'):
            keyboard.send('ctrl+a')
            time.sleep(0.4)
            keyboard.send('backspace')
            keyboard.write(replace)
            keyboard.send('enter')
            break
    keyboard.unblock_key('enter')

def minesweep_keys():
    while True:
        if keyboard.is_pressed('f'):
            print("Thank you for paying respects.")
            break
        
            

string1 = "Why I will always be single"

google_search_removal(string1)

minesweep_keys()