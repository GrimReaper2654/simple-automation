# -------------------------- Instructions --------------------------
# 
# Sometimes, you can't paste text into a field. This is a workaround.
#
# ------------------------------------------------------------------

from helper import *
import pyautogui
import time


phrase = 'AAAA'

time.sleep(1) # Adjust to suit your own reaction time
pyautogui.typewrite(phrase)
