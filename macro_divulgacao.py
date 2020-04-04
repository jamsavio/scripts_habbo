import clipboard
import pyautogui
import time

while True: 
    pyautogui.doubleClick(600, 650)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter")
    time.sleep(60)