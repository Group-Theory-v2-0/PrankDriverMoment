import pyautogui
import random

print(pyautogui.size())
#pyautogui.click(random.randrange(0, 1000), random.randrange(0,1000))
pyautogui.moveTo(random.randrange(0,1000), random.randrange(0,1000), duration = 2)
pyautogui.moveRel(0, 1000)  # move mouse 10 pixels down
pyautogui.dragTo(100, 150)
pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down

pyautogui.scroll(random.random(), x=random.random(), y=random.random())


