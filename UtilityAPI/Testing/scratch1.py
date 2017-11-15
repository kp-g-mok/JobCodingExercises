# import PyPDF2
#
# if __name__ == '__main__':
#     with open('files/automate_online-materials/meetingminutes.pdf', 'rb') as pdfFileObj:
#         pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#         print(pdfReader.numPages)
#         pageObj = pdfReader.getPage(2)
#         fulltext = pageObj.extractText()
#         print(fulltext)
#         searchstring='Agenda'
#         index = fulltext.find(searchstring)
#         while index != -1:
#             print(index)
#             index = fulltext.find(searchstring, index+len(searchstring))

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
    pdftext = convert_pdf_to_txt('files/automate_online-materials/meetingminutes.pdf')
    splittext = pdftext.split("Agenda")
    print(pdftext)
