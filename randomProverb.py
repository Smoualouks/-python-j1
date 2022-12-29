# data source:
from random import randint, choice
proverbs = [
    "Pierre qui roule n'amasse pas mousse",
    "Une hirondelle ne fait pas le printemps",
    "Tra il dire e il ",
    "Ad Astra",
    "Bsahtek"
]

# print (proverbs [randint(0,4)])
# print(choice(proverbs))
indexMax = len(proverbs) - 1
print(proverbs[randint(0, indexMax)])