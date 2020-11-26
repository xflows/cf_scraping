import requests
from goose3 import Goose
from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()


def scraping_strip_tags(input_dict):
    s = MLStripper()
    s.feed(input_dict['html'])
    return {'text': s.get_data()}


def scraping_download_page(input_dict):
    page = requests.get(input_dict['url'])
    return {'html': page.text}


def scraping_boilerplate_removal(input_dict):
    g = Goose()
    article = g.extract(raw_html=input_dict['html'])
    return {'text': article.cleaned_text}

