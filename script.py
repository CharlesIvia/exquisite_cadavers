# WANT: Creaate monte carlo generator that can construct sensible lines of poetry
# This idea is inspired by Fooled by Randomness, a book by Nasim Taleb

# "On a folded piece of paper, in turn, each of the five people would write a predetermined
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
    "is",
    "might",
    "could",
    "will",
    "shall",
    "can",
]
collective_nouns = get_collective_nouns()
uncountable_nouns = get_un_nouns()
abstract_nouns = get_abstract_nouns()

nouns = uncountable_nouns + abstract_nouns
articles = ["a", "the"]
vowels = ["a", "e", "i", "o", "u"]


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

    if selected_adjs[0][0] in vowels:
        article = "an"
    else:
        article = random.choice(articles)

    return (
        article
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


for _ in range(100):
    poem = construct_poetry()
    print(poem.capitalize())

# Some of the interesting lines of poetry formed:

# A whining customer service can crash a flaky happiness.
# A tight law can squash the happy riches.
# The helpful childhood might handle the sweet warmth.
# The mango warmth could wriggle the worried time.
# The weak wealth shall program the elegant adventure.
# An alive pleasure will vanish a scary silver.
# A deafening loss was tease a raspy awe.
# A shrilling love can preach the vast luck.
# The flat silver will lighten the fancy time.
# A massive tolerance can seal the eager surprise.
# A tight compassion has found a deep tiredness.
# The helpful shopping might pat a calm artisty.
# The melodic relaxation shall grip a ashy ability.
# An agreeable pasta might confuse the quiet talent.
# A loose power can melt the noisy courage.
# A scruffy bread might screw the careful pasta.
# The most disquiet shall tremble a deep fascination.
# The yellow gold shall sprout a modern awe.
# The prickly amazement will sail a greasy strictness.
