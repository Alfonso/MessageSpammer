import pyautogui
import sys

filepath = sys.argv[1]

with open(filepath) as fp:
   for cnt, line in enumerate(fp):
        pyautogui.write(line,interval=0.05)
        pyautogui.press('return')
