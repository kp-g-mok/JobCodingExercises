from html.parser import HTMLParser


class AllLanguages(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.inLink = False
        self.dataArray = []
        self.countLanguages = 0
        self.lasttag = None
        self.lastname = None
        self.lastvalue = None

    def handle_starttag(self, tag, attrs):
        self.inLink = False
        if tag == 'a':
            if any(name == 'class' and value == 'Vocabulary' for name, value in attrs):
                self.countLanguages += 1
                self.inLink = True
                self.lasttag = tag

    def handle_endtag(self, tag):
        if tag == "a":
            self.inLink = False

    def handle_data(self, data):
        if self.lasttag == 'a' and self.inLink and data.strip():
            print(data)


if __name__ == '__main__':
    parser = AllLanguages()
    with open('files/language.html', 'r') as file:
        parser.feed(file.read())
        print(parser.countLanguages)
