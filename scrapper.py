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


# uncountable noun

uncountable_nouns = []


def get_un_nouns():
    URL = "https://englishstudyhere.com/nouns/uncountable-noun-list-in-english/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    ps = soup.find_all("p")
    for p in ps:
        noun = p.text
        if len(noun) < 10 and len(noun) > 3:
            uncountable_nouns.append(noun)
    return uncountable_nouns


# abstract nouns

abstract_nouns = []


def get_abstract_nouns():
    URL = "https://englishstudyhere.com/nouns/abstract-nouns-list/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    lis = soup.find_all("li")
    for li in lis:
        noun = li.text
        abstract_nouns.append(noun)
    return abstract_nouns[88:-58]
