# WANT: Creaate monte carlo generator that can construct sensible lines of poetry
# This idea is inspired by Fooled by Randomness, a book by Nasim Taleb

# "On a folded piece of paper, in turn, each one of them would write a predetermined
# part of a sentence, not knowing the others’ choice. The first
# would pick an adjective, the second a noun, the third a verb, the
# fourth an adjective, and the fifth a noun."

# Import required libraries
import random
from scrapper import (
    get_adjectives,
    get_verbs,
    get_un_nouns,
    get_abstract_nouns,
    get_collective_nouns,
)

adjectives = get_adjectives()
verbs = get_verbs()
linking_verbs = [
    "am",
    "is",
    "are",
    "was",
    "were",
    "has been",
    "are being",
    "might be",
    "has been",
    "could be",
    "was being",
    "has been",
    "shall",
]
collective_nouns = get_collective_nouns()
uncountable_nouns = get_un_nouns()
abstract_nouns = get_abstract_nouns()

nouns = uncountable_nouns + abstract_nouns
articles = ["A", "An", "The"]


def construct_poetry():
    random.shuffle(adjectives)
    selected_adjs = random.choices(adjectives, k=2)
    random.shuffle(nouns)
    selected_nouns = random.choices(nouns, k=2)
    random.shuffle(verbs)
    selected_verb = random.choice(verbs)
    random.shuffle(linking_verbs)
    selected_linking_verb = random.choice(linking_verbs)
    selected_article = random.choices(articles, k=2)

    print(
        selected_article[1]
        + " "
        + selected_adjs[0]
        + " "
        + selected_nouns[0]
        + " "
        + selected_linking_verb
        + " "
        + selected_verb
        + " "
        + selected_article[1]
        + " "
        + selected_adjs[1]
        + " "
        + selected_nouns[1]
        + "."
    )


construct_poetry()
