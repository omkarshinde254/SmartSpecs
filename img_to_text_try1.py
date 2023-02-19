import PIL
import pytesseract
import cv2

from PIL import Image

im = Image.open('IMAGES/sample3.jpg')
im.show()

#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


text = pytesseract.image_to_string(im)

print(text)
