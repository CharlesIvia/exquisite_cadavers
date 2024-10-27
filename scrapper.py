import requests
from bs4 import BeautifulSoup
import time
import logging
from functools import wraps

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
URLS = {
    'adjectives': "https://www.paperrater.com/page/lists-of-adjectives",
    'verbs': "https://englishstudyhere.com/verbs/500-regular-verbs-english-regular-verbs-list/",
    'uncountable_nouns': "https://englishstudyhere.com/nouns/uncountable-noun-list-in-english/",
    'abstract_nouns': "https://englishstudyhere.com/nouns/abstract-nouns-list/",
    'collective_nouns': "https://englishstudyhere.com/nouns/200-examples-of-collective-nouns/"
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

def retry_with_backoff(func):
    """Retry the function with exponential backoff."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                return func(*args, **kwargs)
            except requests.RequestException as e:
                if attempt == max_attempts - 1:
                    logger.error(f"Failed after {max_attempts} attempts: {str(e)}")
                    return []
                time.sleep(2 ** attempt)  # Exponential backoff
        return []
    return wrapper

def fetch_page(url):
    """Fetch a webpage and return BeautifulSoup object."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")
    except requests.RequestException as e:
        logger.error(f"Error fetching {url}: {e}")
        return None

@retry_with_backoff
def get_adjectives():
    """Get adjectives list from paperrater.com."""
    soup = fetch_page(URLS['adjectives'])
    if not soup:
        return []
    
    adjectives = []
    for tag in soup.find_all("li"):
        adj = tag.text.strip()
        if 3 < len(adj) < 10:
            adjectives.append(adj.lower())
    
    return adjectives[4:]  # Skip header elements

@retry_with_backoff
def get_verbs():
    """Get verbs list from englishstudyhere.com."""
    soup = fetch_page(URLS['verbs'])
    if not soup:
        return []
    
    verbs = []
    for td in soup.find_all("td"):
        verb = td.text.strip()
        if len(verb) > 2:
            verbs.append(verb.lower())
    
    return verbs

@retry_with_backoff
def get_un_nouns():
    """Get uncountable nouns list."""
    soup = fetch_page(URLS['uncountable_nouns'])
    if not soup:
        return []
    
    nouns = []
    for p in soup.find_all("p"):
        noun = p.text.strip()
        if 3 < len(noun) < 10:
            nouns.append(noun.lower())
    
    return nouns

@retry_with_backoff
def get_abstract_nouns():
    """Get abstract nouns list."""
    soup = fetch_page(URLS['abstract_nouns'])
    if not soup:
        return []
    
    nouns = []
    for li in soup.find_all("li"):
        noun = li.text.strip()
        nouns.append(noun.lower())
    
    return nouns[88:-58]

@retry_with_backoff
def get_collective_nouns():
    """Get collective nouns list."""
    soup = fetch_page(URLS['collective_nouns'])
    if not soup:
        return []
    
    nouns = []
    for b in soup.find_all("b"):
        noun = f"a {b.text.strip()} of"
        nouns.append(noun.lower())
    
    return nouns

def get_all_words():
    """Get all word lists at once."""
    return {
        'adjectives': get_adjectives(),
        'verbs': get_verbs(),
        'uncountable_nouns': get_un_nouns(),
        'abstract_nouns': get_abstract_nouns(),
        'collective_nouns': get_collective_nouns()
    }

if __name__ == "__main__":
    # Test the scraper
    print("Testing scraper...")
    
    for category, word_list in get_all_words().items():
        print(f"\n{category}:")
        print(f"Found {len(word_list)} words")
        print(f"Sample: {word_list[:5]}")