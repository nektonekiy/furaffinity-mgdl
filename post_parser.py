import requests
from bs4 import BeautifulSoup as BS

class PostParser:

    def __init__(self, url):
        r = requests.get(url)
        self.html = BS(r.content, "html.parser") 

    def get_pic_file_url(self):
        el = self.html.select(".submission-image")[0]
        pic_file_url = "https:" + el.select("img")[0]["data-fullview-src"]
        return pic_file_url
    def get_pic_title(self):
        el = self.html.select(".submission-title")[0]
        pic_title = el.select("p")[0].text
        return pic_title
    def get_pic_description(self):
        el = self.html.select(".submission-description")[0]
        pic_description = el.text.strip()
        return pic_description
