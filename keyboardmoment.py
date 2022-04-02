import keyboard
import time

keyboard.add_hotkey('space', lambda: keyboard.send('f'))

keyboard.wait('escape')


