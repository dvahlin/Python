#!/usr/bin/python3
#Script to parse local pizza menu
#import pypdf
import PyPDF2

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        read_pdf = PyPDF2.PdfFileReader(pdf_path)
        number_of_pages = read_pdf.getNumPages()

        for page_number in range(number_of_pages):
            page = read_pdf.getPage(page_number)
            page_content = page.extractText()
        print(page_content)

if __name__ == '__main__':
    path = '/PATH/TO/FILE.pdf'
    extract_information(path)
