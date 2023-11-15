import os
import win32com.client

"""
pip install pywin32
"""

wdFormatPDF = 17

inputFile = os.path.abspath("test.docx")
outputFile = os.path.abspath("test.pdf")
word = win32com.client.Dispatch("Word.Application")
doc = word.Documents.Open(inputFile)
doc.SaveAs(outputFile, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()
