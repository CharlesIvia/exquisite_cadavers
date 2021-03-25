import requests
from bs4 import BeautifulSoup

adjs_list = []


def get_adjectives():
    URL = "https://www.paperrater.com/page/lists-of-adjectives"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    lis = soup.find_all("li")
    for tag in lis:
        adj = tag.text
        if len(adj) < 10 and len(adj) > 3:
            adjs_list.append(adj)
    return adjs_list[4:]
