# import required modules
import requests
from bs4 import BeautifulSoup

# Extract a list of adjectives from paperrater.com
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


# extract a list of verbs from englishstudyhere.com
verbs_list = []


def get_verbs():
    URL = "https://englishstudyhere.com/verbs/500-regular-verbs-english-regular-verbs-list/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    tds = soup.find_all("td")
    for td in tds:
        verb = td.text
        if len(verb) > 2:
            verbs_list.append(verb)
    return verbs_list
