# -------------------------- Instructions --------------------------
# 
# Spam page reload, useful for botting views on dumb sites.
#
# ------------------------------------------------------------------

import time
import random
from helper import *

time.sleep(1)
while 1:
    command('r')
    time.sleep(0.5 + random.randint(0,0)) # change frequency of reloads, supports randomization