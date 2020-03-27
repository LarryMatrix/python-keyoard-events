from pyautogui import hotkey
import time


for i in range(1, 36000):
    print("Hello world, this is a test")
    time.sleep(10)
    hotkey('ctrl', 'c')
