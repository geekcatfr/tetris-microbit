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
    elif piece == barre_s or piece == barre_z:
        result = 2
    elif piece == carre or piece == barre_t:
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
barres_posees = []

for i in range(0, descente):
    display.show(barre_selectionnee.shift_down(i+1))
    sleep(200)

barres_posees.append(barre_selectionnee.shift_down(descente))
print(barres_posees)

clic_bouton_a = 0
clic_bouton_b = 0

while True:
    if button_b.was_pressed():
        clic_bouton_a += 1
        display.show(barres_posees[-1].shift_right(clic_bouton_a))
        print(clic_bouton_a)

    if button_a.was_pressed():
        clic_bouton_a -= 1
        display.show(barres_posees[-1].shift_right(clic_bouton_a))
        print(clic_bouton_a)
