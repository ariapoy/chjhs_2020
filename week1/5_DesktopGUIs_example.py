# conda install -c conda-forge pyautogui
# Ref: [PyAutoGUI Cheet Sheet](https://pyautogui.readthedocs.io/en/latest/quickstart.html)

import pyautogui

print(pyautogui.position())
# Point(x=754, y=1057) position of chrome link
x=800; y=1060
print(pyautogui.size())
print(pyautogui.onScreen(800, 1060))
pyautogui.moveTo(x, y, duration=3)
moveToX=831; moveToY=1048
pyautogui.click(x=moveToX, y=moveToY, clicks=1, button='left')
x=579; y=612
pyautogui.moveTo(x, y, duration=5)
moveToX=699; moveToY=74
pyautogui.click(x=moveToX, y=moveToY, clicks=1, button='left')
pyautogui.hotkey('shift')
pyautogui.typewrite('Python', interval=0.2)  # useful for entering text, newline is Enter
pyautogui.hotkey('shift')
pyautogui.typewrite('w94\ngp6\nx87\n\n', interval=0.2)
