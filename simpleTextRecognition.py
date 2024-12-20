import pytesseract
from PIL import ImageOps, Image

pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

# Convert image to grayscale and then apply a threshold to make it black and white
img = Image.open('img.jpg')
img = ImageOps.grayscale(img)

txt = pytesseract.image_to_string(img)
print(txt)