from pdf2docx import Converter

cv = Converter('file.pdf')
cv.convert('file_out.docx', start=0, end=None)
cv.close()