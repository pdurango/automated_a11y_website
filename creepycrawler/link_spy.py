# AutomatedA11y
# link_spy.py
# Purpose: Given html(string) for a web page, it traverses it, puts all links into a set, and returns the set
#
# @author Lucas Silvestri
# @version 2.0

from html.parser import HTMLParser
from urllib import parse


class LinkSpy(HTMLParser):
    def __init__(self, home_url, page_url):
        super().__init__()
        self.home_url = home_url
        self.page_url = page_url
        self.link_set = set()

    def handle_starttag(self, tag, attributes):
        if tag == "a":
            for (attribute, value) in attributes:
                if attribute == "href":
                    url = parse.urljoin(self.home_url, value)
                    self.link_set.add(url)
                    # print ("LINK_SPY PARSING URL")

    def page_link_set(self):
        return self.link_set

    def error(self, message):
        pass
