# PDF 문자열 추출
import fitz, pprint
path = "kpi.pdf"
doc = fitz.open(path)
for page in doc:
    text = page.get_textpage()
    pprint.pprint(text)


print("*" * 50)

from PyPDF2 import PdfReader
reader = PdfReader(path)
pages = reader.pages
text = ""
for page in pages:
    sub = page.extract_text()
    text += sub

print(text)


import numpy as np
import pytesseract 
from PIL import Image
# pip install pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\STS240118A\AppData\Local\Programs\Tesseract-OCR\tesseract'
image = 'test.png'

# image_np = np.array(Image.open(image))
# text = pytesseract.image_to_string(image_np, lang='kor')
# print(text)

# 설치된 언어 종류  
# langs = pytesseract.get_languages(config='')
# print(langs)


