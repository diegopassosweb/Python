import pyautogui
# import time
pyautogui.PAUSE = 2

pyautogui.press("win")
pyautogui.write("info.txt")
pyautogui.press("backspace")
pyautogui.press("enter")

pyautogui.click(x=500, y=186)
pyautogui.write("APRENDER")

pyautogui.click(x=511, y=225)
pyautogui.write("PYTHON")

# time.sleep(3)
# pyautogui.position()