"""
Extract two strings
Electric meter number 06067013
Electric Tax total amount: -1.41
"""

import io

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    with open(path, 'rb') as fp:
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                      password=password,
                                      caching=caching,
                                      check_extractable=True):
            interpreter.process_page(page)

        text = retstr.getvalue()

    device.close()
    retstr.close()
    return text

if __name__ == '__main__':
    text = convert_pdf_to_txt('sdge_bill.pdf')
    taxValue = text.split('Total Taxes & Fees on Electric Charges  -', 1)[1].split('Total')[0].strip()
    stringDict = {
        'Electric Meter Number': text.split('Meter Number: ', 1)[1].split('(', 1)[0].strip(),
        'Electric Tax Total': '-' + taxValue[1:]
    }
    print(stringDict)
