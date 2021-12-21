import fitz

pdffile = "back-panel-drawing.pdf"
doc = fitz.open(pdffile)
page = doc.load_page(0)  # number of page
pix = page.get_pixmap()
output = "back-panel-drawing.png"
pix.save(output)
