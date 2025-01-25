import requests
from bs4 import BeautifulSoup as BS

class GalleryParser:

    def __init__(self, url: str, page_type: str):
        self.url = url
        self.page_type = page_type

    def get_submissions_urls(self):
        submissions_urls = []
        if self.page_type == "favorites":
            print("Sorry. Favorites downloading functionaltiy is under development")
            return submissions_urls
        def get_page(url):
            r = requests.get(url)
            return BS(r.content, "html.parser")

        def parse_gallery_for_submissions_urls(html):
            submissions_urls = []
            if self.page_type == "gallery":
                for el in html.select("#gallery-gallery > .r-general"):
                    a = el.select("u > a")[0]
                    submissions_urls.append("https://www.furaffinity.net" + a["href"])
            if self.page_type == "favorites":
                pass
            return submissions_urls

        page = 1
        while True:
            url = self.url + "/" + str(page)
            submissions_urls_found = parse_gallery_for_submissions_urls(get_page(url))
            if submissions_urls_found != []:
                submissions_urls += submissions_urls_found
                page += 1
            else:
                break
        return submissions_urls
