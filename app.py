import pdf
from shutil import which

CFG_PATH_PDFTOTEXT = "C:\Users\saber\workspace\xpdf-tools-win-4.01.01\bin64\pdftotext.exe" #For Windows
pdfile = "pdf-files/0309816818759231.pdf"
keep_layout=False


if os.name != 'nt': #not windows
    CFG_PATH_PDFTOTEXT = os.environ.get('CFG_PATH_PDFTOTEXT', which('pdftotext')) #/usr/bin/pdftotext

textbody = pdf.convert_PDF_to_plaintext(pdfile, keep_layout,CFG_PATH_PDFTOTEXT)
print(textbody)