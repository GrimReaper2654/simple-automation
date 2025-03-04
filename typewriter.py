# -------------------------- Description ---------------------------
# 
# Run the program, it will write stuff. Edit the phrase to suit 
# your needs.
#
# ------------------------------------------------------------------

from helper import *
import pyautogui
import random
import time

phrase = 'hello world'

time.sleep(1) # Adjust to suit your own reaction time
pyautogui.typewrite(phrase)
