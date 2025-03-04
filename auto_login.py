# -------------------------- Instructions --------------------------
# 
# Keep forgetting your password? Shitty application not letting you
# copy paste it? Passwords too secure, not enough vulnerabilities?
# 
# This is the solution.
#
# ------------------------------------------------------------------

from helper import *
import pyautogui
import time

class Credentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def login(credentials):
    time.sleep(1) # Adjust to suit your own reaction time
    pyautogui.typewrite(credentials.username)
    pyautogui.press("enter") # use tab instead of enter depending on what the login screen wants
    pyautogui.typewrite(credentials.password)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")

credentials = Credentials('Username', 'Password1')
login(credentials)