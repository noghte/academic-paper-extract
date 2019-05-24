import pdf

keep_layout=False
fpath = "pdf-files/0309816818759231.pdf"
textbody = pdf.convert_PDF_to_plaintext(fpath, keep_layout)
print(textbody)