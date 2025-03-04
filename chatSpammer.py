# -------------------------- Description ---------------------------
# 
# Run the program, then switch to the window with the chat.
# Click on the text input and the program will automatically copy 
# and paste random phrases from the list into the chat and press
# enter to send them. Can be used to annoy friends on discord.
# There isn't a good way to stop it so just kill the terminal.
#
# ------------------------------------------------------------------

from helper import *
import pyautogui
import random
import time

phrases = [ # Customise with your own
    'https://github.com/GrimReaper2654',
    'subscribe to GrimReaper2654',
    'GrimReaper2654 is cool',
]

time.sleep(3) # Adjust to suit your own reaction time
while 1:
    copy(random.choice(phrases))
    command('v')
    pyautogui.press('enter')
    time.sleep(0.25) # Adjust delay as needed

