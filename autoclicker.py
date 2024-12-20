# -------------------------- Instructions --------------------------
# 
# There is no autoclicker on mac so I made one
#
# ------------------------------------------------------------------

from Quartz.CoreGraphics import (
    CGEventCreateMouseEvent,
    CGEventPost,
    CGEventGetLocation,
    kCGHIDEventTap,
    kCGMouseButtonLeft,
    kCGEventLeftMouseDown,
    kCGEventLeftMouseUp,
    kCGEventMouseMoved,
)
import time
import random
from helper import *

def left_click2(x, y):
    # Create a left mouse down event
    event_down = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, (x, y), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, event_down)

    # Create a left mouse up event
    event_up = CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, (x, y), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, event_up)

time.sleep(1)
for i in range(1000):
    left_click(900, 500)
    time.sleep(2)