import pdf
import os
from shutil import which

CFG_PATH_PDFTOTEXT = r"C:\Users\saber\workspace\xpdf-tools-win-4.01.01\bin64\pdftotext.exe" #For Windows
fpath = "pdf-files/0309816818759231.pdf"
keep_layout=False


if os.name != 'nt': #not windows
    CFG_PATH_PDFTOTEXT = os.environ.get('CFG_PATH_PDFTOTEXT', which('pdftotext')) #/usr/bin/pdftotext

textbody = pdf.convert_PDF_to_plaintext(fpath, CFG_PATH_PDFTOTEXT, keep_layout)
print(textbody)