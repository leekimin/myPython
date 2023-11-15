from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter

"""
pip install aspose-words
"""

pdfmetrics.registerFont(TTFont("휴먼매직체", "HMKMMAG.TTF"))
pdf = canvas.Canvas("test.pdf", pagesize=letter)
pdf.setFont("휴먼매직체", 14)
pdf.drawString(80, 800, "## Sample Pdf 한글 ##")

pdf.save()