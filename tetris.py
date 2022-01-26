from microbit import *
import random


def selectionner_barre(liste_barre):
    result = random.choice(liste_barre)
    return result


class barre:
    """Une barre qui a sa position x et y"""

    # Définition des différentes barres
    barre_s = Image("99000:" "00000:" "00000:" "00000:" "00000")
    barre_z = Image("09000:" "99000:" "00000:" "00000:" "00000")
    barre = Image("90000:" "99000:" "00000:" "00000:" "00000")
    carre = Image("99000:" "99000:" "00000:" "00000:" "00000")
    barre_t = Image("9000:" "90000:" "90000:" "00000:" "00000")
    barres = [barre_s, barre_z, barre, barre_t, carre]

    def __init__(self):
        self.x = 0
        self.y = 0
        self.forme_barre = selectionner_barre(barre.barres)

    def peutDescendre(self):
        """va chercher la hauteur de la barre,
        puis retourne de combien elle doit descendre"""
        if display.get_pixel(2, self.y) == 0 and self.x < 3:
            self.x += 1
            self.afficherBarre(self.x, self.y)
            return True

    def allerADroite(self):
        self.y += 1
        print(self.y)
        self.afficherBarre(self.x, self.y)

    def allerAGauche(self):
        self.y -= 1
        print(self.y)
        self.afficherBarre(self.x, self.y)

    def afficherBarre(self, pos_x=0, pos_y=0):
        display.show(self.forme_barre.shift_down(pos_x).shift_right(pos_y))


barre_courante = barre()
barres_posees = []

barres_posees.append(barre_courante)
barre_courante.afficherBarre()

while barre_courante.peutDescendre():

    if button_b.was_pressed():
        barre_courante.allerADroite()

    if button_a.was_pressed():
        barre_courante.allerAGauche()

    sleep(300)
