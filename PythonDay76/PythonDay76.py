# Exercise 8: Merge The PDF

"""
Merge multiple PDF files using pyPDF module
Free to use more functionalities

"""

import os
import pypdf
from pypdf import PdfReader, PdfWriter

folderPath = r"C:\Users\MasterofAsh\Desktop\Python Course\PythonDay76"
# folderName = os.path.basename(folderPath)
folderContents = os.listdir(folderPath)
print(folderContents)

pdfMerger = PdfWriter()

for PDFs in folderContents:
    if PDFs.endswith(".pdf"):
        print("Succesfully Merging")
        fullPath = os.path.join(folderPath, PDFs)

        pdfMerger.append(PDFs)

pdfMerger.write("FinalKUMULALA.pdf")