# WANT: Creaate monte carlo generator that can construct sensible lines of poetry
# This idea is inspired by Fooled by Randomness, a book by Nasim Taleb

# "On a folded piece of paper, in turn, each one of them would write a predetermined
# part of a sentence, not knowing the others’ choice. The first
# would pick an adjective, the second a noun, the third a verb, the
# fourth an adjective, and the fifth a noun."

# Import required libraries
import random
from adj_scrapper import get_adjectives

adjectives = get_adjectives()
random.shuffle(adjectives)

chosen_adj = random.choice(adjectives)
print(chosen_adj)