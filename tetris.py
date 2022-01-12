from microbit import *
import random

def selectionner_barre(liste_barre):
    result = random.choice(liste_barre)
    return result

def descente_barre(piece):
    """va chercher la hauteur de la barre,
    puis retourne de combien elle doit descendre"""
    if piece == barre:
        result = 1
    elif piece == barre_s | piece == barre_t | piece == barre_z:
        result = 2
    elif piece == carre:
        result = 3
    return result

# Définition des différentes barres
barre_s = Image("09000:"
                "99000:"
                "90000:"
                "00000:"
                "00000")

barre_z = Image("90000:"
                "99000:"
                "09000:"
                "00000:"
                "00000")

barre = Image("90000:"
              "90000:"
              "90000:"
              "90000:"
              "00000")

carre = Image("99000:"
              "99000:"
              "00000:"
              "00000:"
              "00000")

barre_t = Image("09000:"
                "99900:"
                "00000:"
                "00000:"
                "00000")


barres = [barre_s, barre_z, barre, barre_t, carre]
barre_selectionnee = selectionner_barre(barres)
descente = descente_barre(barre_selectionnee)

for i in range(0, descente):
    display.show(barre_selectionnee.shift_down(i))
    sleep(200)
