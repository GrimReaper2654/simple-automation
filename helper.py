import pyautogui
import time
import pytesseract
import platform
import subprocess
from PIL import ImageOps

# update according to your installation
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

def copy(text):
    process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    process.communicate(input=text.encode('utf-8'))

def ocr(pos1, pos2):
    upperLeftX, upperLeftY = pos1
    x = pos2[0] - upperLeftX
    y = pos2[1] - upperLeftY
    img = pyautogui.screenshot('image.png', region=(int(upperLeftX), int(upperLeftY), int(x), int(y)))
    time.sleep(0.25)

    # Convert image to grayscale and then apply a threshold to make it black and white
    img = ImageOps.grayscale(img)
    img = img.point(lambda p: p > 150 and 255)  # Thresholding to make the text white

    time.sleep(0.25)
    txt = pytesseract.image_to_string(img)
    return txt.lower()

def left_click(coords):
    pyautogui.click(coords[0], coords[1]) 
    time.sleep(0.1)

def command(key):
    # Detect the operating system
    os_name = platform.system()

    if os_name == 'Windows' or os_name == 'Linux':
        # For Windows/Linux, use Ctrl
        pyautogui.hotkey('ctrl', key)
    elif os_name == 'Darwin': 
        # For macOS, use Cmd
        pyautogui.hotkey('command', key)
    else:
        raise NotImplementedError(f"Unsupported OS: {os_name}")
    time.sleep(0.1)
    