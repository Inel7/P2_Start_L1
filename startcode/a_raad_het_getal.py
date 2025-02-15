# Schrijf een functie is_getal_geraden die op basis van een gok en een geheim_nummer controleert of de gok correct was.
# Print hier een boodschap, en return de juiste waarde.
# Schrijf een functie raad_het_getal, die op basis van een bovengrens het raadspel zal spelen.

import random
from random import randint


def is_getal_geraden(gok,geheim_getal):
    if gok == geheim_getal:
        print("Proficiat, je hebt het getal geraden")
        return True
    else:
        print("fout")
        return False

def raad_het_getal(bovengrens):
    geheim_getal = randint(1,bovengrens)
    geraden = False

    while not geraden:
        gok = int(input(f"geef een getal tussen 1 en {bovengrens} "))
        geraden = is_getal_geraden(gok,geheim_getal)

raad_het_getal(10)
