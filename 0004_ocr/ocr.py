import numpy as np
import pytesseract 
from PIL import Image

"""
pip install pytesseract
"""

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\computer\AppData\Local\Programs\Tesseract-OCR\tesseract'
image = 'test.png'

image_np = np.array(Image.open(image))
text = pytesseract.image_to_string(image_np, lang='kor')
print(text)

# 설치된 언어 종류  
langs = pytesseract.get_languages(config='')
print(langs)