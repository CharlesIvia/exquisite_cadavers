import random
from typing import List, Tuple
import re
from scrapper import (
    get_adjectives, 
    get_verbs, 
    get_un_nouns, 
    get_abstract_nouns
)

# Configuration
LINKING_VERBS = ["is", "might", "could", "will", "shall", "can"]
ARTICLES = ["a", "the"]
VOWELS = ["a", "e", "i", "o", "u"]
PREPOSITIONS = ["in", "through", "beneath", "beyond", "within", "among"]

def read_backup_words(filename: str = "notes.md") -> Tuple[List[str], List[str], List[str]]:
    """Read backup word lists from notes.md file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            
            # Extract verbs list
            verbs_match = re.search(r"verbs list = \[(.*?)\]", content, re.DOTALL)
            verbs = [word.strip("' ") for word in verbs_match.group(1).split(',')] if verbs_match else []
            
            # Extract adjectives list
            adj_match = re.search(r"adjectives = \[(.*?)\]", content, re.DOTALL)
            adjectives = [word.strip("' ") for word in adj_match.group(1).split(',')] if adj_match else []
            
            # Extract nouns list
            nouns_match = re.search(r"nouns = \[(.*?)\]", content, re.DOTALL)
            nouns = [word.strip("' ") for word in nouns_match.group(1).split(',')] if nouns_match else []
            
            return adjectives, verbs, nouns
    except Exception as e:
        print(f"Error reading backup words from {filename}: {e}")
        return [], [], []

def get_wordbank(use_backup: bool = True) -> Tuple[List[str], List[str], List[str]]:
    """Get words either from web scraping or backup lists."""
    if not use_backup:
        try:
            return (
                get_adjectives(),
                get_verbs(),
                get_un_nouns() + get_abstract_nouns()
            )
        except Exception as e:
            print(f"Failed to scrape words: {e}. Using backup word lists...")
            use_backup = True
            
    # Read backup lists from notes.md
    return read_backup_words()

def get_article(word: str) -> str:
    """Return appropriate article based on word's first letter."""
    return "an" if word[0].lower() in VOWELS else random.choice(ARTICLES)

def generate_basic_line(adjectives: List[str], verbs: List[str], nouns: List[str]) -> str:
    """Generate a line using the basic pattern."""
    adj1, adj2 = random.sample(adjectives, 2)
    noun1, noun2 = random.sample(nouns, 2)
    verb = random.choice(verbs)
    linking_verb = random.choice(LINKING_VERBS)
    
    article1 = get_article(adj1)
    article2 = random.choice(ARTICLES)
    
    return f"{article1} {adj1} {noun1} {linking_verb} {verb} {article2} {adj2} {noun2}"

def generate_compound_line(adjectives: List[str], verbs: List[str], nouns: List[str]) -> str:
    """Generate a line with compound structure."""
    adj1, adj2, adj3 = random.sample(adjectives, 3)
    noun1, noun2 = random.sample(nouns, 2)
    verb = random.choice(verbs)
    
    article1 = get_article(adj1)
    
    return f"{article1} {adj1} and {adj2} {noun1} {verb} like {adj3} {noun2}"

def generate_preposition_line(adjectives: List[str], verbs: List[str], nouns: List[str]) -> str:
    """Generate a line using prepositions."""
    adj1, adj2 = random.sample(adjectives, 2)
    noun1, noun2 = random.sample(nouns, 2)
    verb = random.choice(verbs)
    prep = random.choice(PREPOSITIONS)
    
    article1 = get_article(adj1)
    article2 = get_article(adj2)
    
    return f"{article1} {adj1} {noun1} {verb} {prep} {article2} {adj2} {noun2}"

def generate_metaphor_line(adjectives: List[str], verbs: List[str], nouns: List[str]) -> str:
    """Generate a metaphorical line."""
    adj1, adj2 = random.sample(adjectives, 2)
    noun1, noun2 = random.sample(nouns, 2)
    
    article1 = get_article(adj1)
    
    return f"{article1} {adj1} {noun1} is {adj2} {noun2}"

def generate_poetry(num_lines: int = 1, pattern: str = "random", use_backup: bool = True) -> List[str]:
    """
    Generate specified number of poetry lines.
    
    Args:
        num_lines: Number of lines to generate
        pattern: Type of pattern to use ('random', 'basic', 'compound', 'preposition', 'metaphor')
        use_backup: Whether to use backup word lists instead of web scraping
    """
    # Get word lists
    adjectives, verbs, nouns = get_wordbank(use_backup=use_backup)
    
    if not all([adjectives, verbs, nouns]):
        raise ValueError("Failed to get word lists. Please check the backup file or internet connection.")
    
    # Available patterns
    patterns = {
        "basic": generate_basic_line,
        "compound": generate_compound_line,
        "preposition": generate_preposition_line,
        "metaphor": generate_metaphor_line
    }
    
    lines = []
    for _ in range(num_lines):
        if pattern == "random":
            line_generator = random.choice(list(patterns.values()))
        else:
            line_generator = patterns.get(pattern, generate_basic_line)
            
        line = line_generator(adjectives, verbs, nouns)
        lines.append(line.capitalize() + ".")
        
    return lines

def main():
    # Test if backup words are available
    backup_adj, backup_verbs, backup_nouns = read_backup_words()
    if not all([backup_adj, backup_verbs, backup_nouns]):
        print("Warning: Backup words not available. Will attempt web scraping.")
        use_backup = False
    else:
        use_backup = input("Use backup word lists? (y/n): ").lower() == 'y'
    
    try:
        print("\nRandom Pattern Poem (5 lines):")
        for line in generate_poetry(num_lines=5, use_backup=use_backup):
            print(line)
            
        print("\nMetaphor Pattern Poem (3 lines):")
        for line in generate_poetry(num_lines=3, pattern="metaphor", use_backup=use_backup):
            print(line)
            
        print("\nCompound Pattern Poem (3 lines):")
        for line in generate_poetry(num_lines=3, pattern="compound", use_backup=use_backup):
            print(line)
            
        print("\nPreposition Pattern Poem (3 lines):")
        for line in generate_poetry(num_lines=3, pattern="preposition", use_backup=use_backup):
            print(line)
            
    except Exception as e:
        print(f"Error generating poetry: {e}")

if __name__ == "__main__":
    main()