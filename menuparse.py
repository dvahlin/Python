#!/usr/bin/python3
#Script to parse local pizza menu
#import pypdf
import PyPDF2


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        read_pdf = PyPDF2.PdfFileReader(pdf_path)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.getPage(0)
        page_content = page.extractText()
    print(page_content)

if __name__ == '__main__':
    path = '/root/menyparse/meny.pdf'
    extract_information(path)
