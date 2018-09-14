import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
        self.lists = []
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "https://" in url:
                self.lists.append(url)
        #print(self.lists)

    def save(self):
        with open("scraping.txt", "w") as f:
            for list in self.lists:
                f.write(list + "\n")

    def read(self):
        with open("scraping.txt", "r") as f:
            print(f.read())

news = "https://news.google.com/"
Scraper(news).save()
Scraper(news).read()
