import PyPDF2

if __name__ == '__main__':
    with open('files/automate_online-materials/meetingminutes.pdf', 'rb') as pdfFileObj:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        print(pdfReader.numPages)
        pageObj = pdfReader.getPage(2)
        fulltext = pageObj.extractText()
        print(fulltext)
        searchstring='Agenda'
        index = fulltext.find(searchstring)
        while index != -1:
            print(index)
            index = fulltext.find(searchstring, index+len(searchstring))
