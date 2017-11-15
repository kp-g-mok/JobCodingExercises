"""
Extract two strings
Service address: 6540 SCHMIDT LN UNIT D309, EL CERRITO, CA 94530-3271493
Rate name: E-1 Standard Residential Electric Service
"""


from html.parser import HTMLParser


class ExtractString(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.dataArray = {}
        self.lasttag = None
        self.saDivFound = False
        self.header2Found = False
        self.header3Found = False
        self.currentRate = False

    def handle_starttag(self, tag, attrs):
        self.header2Found = False
        self.header3Found = False
        if tag == 'h2':
            self.header2Found = True
        if tag == 'h3':
            self.header3Found = True
        if tag == 'a':
            for name, value in attrs:
                if name == 'onclick' and 'openGasPopup' in value:
                    addresses = value.split("(", 1)[1][:-1].replace("'", '').split(',')
                    # CA and dash added to zip code. CA is implied since the javascript code in the html file
                    # implies CA for the state as well
                    addresses[2] = 'CA ' + addresses[2][:5] + '-' + addresses[2][5:]
                    address = ', '.join(addresses)
                    self.dataArray['Service address'] = address

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if self.header2Found and data == 'My Current Rate':
            self.currentRate = True
        if self.currentRate and self.header3Found:
            self.dataArray['Rate name'] = data.strip()
            self.currentRate = False

if __name__ == '__main__':
    parser = ExtractString()
    with open('pge_meter_details.html', 'r') as file:
        parser.feed(file.read())
        print(parser.dataArray)
