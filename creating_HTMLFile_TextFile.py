import string
import html2text
from html.parser import HTMLParser


html = open("mscaninsert-0511-msandpain-en(pdf)_DF_ENG-FRA_BT.htm", encoding='utf-8').read()



class MyHTMLParser(HTMLParser):

    def handle_data(self, data):
        line = "".join(c for c in data if c not in string.punctuation and c not in ('“', '«', '”', '»', '–'))

        for line in line:
            f = open('datas.txt', 'a', encoding='utf-8')
            f.write(line)
            f.close()
        

    def get_pages(self):
        return self.pages                
        


parser = MyHTMLParser()
parser.feed(html)


