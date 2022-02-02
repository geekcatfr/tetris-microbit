from microbit import *
import random


def selectionner_barre(liste_barre):
    result = random.choice(liste_barre)
    return result


class barre:
    """Une barre qui a sa position x et y"""

    # Définition des différentes barres
    barre_s = Image("00000:" "99000:" "00000:" "00000:" "00000")
    barre_z = Image("09000:" "99000:" "00000:" "00000:" "00000")
    barre = Image("90000:" "99000:" "00000:" "00000:" "00000")
    carre = Image("99000:" "99000:" "00000:" "00000:" "00000")
    barre_t = Image("9000:" "90000:" "90000:" "00000:" "00000")
    barres = [barre_s, barre_z, barre, barre_t, carre]

    def __init__(self):
        self.x = 0
        self.y = 0
        self.forme_barre = selectionner_barre(barre.barres)

    def stockerTab(self, ImagePieces=None):
        self.ImagePieces = ImagePieces

    def taille(self):
        if self.forme_barre == barre.barre_s:
            return 0
        elif self.forme_barre == barre.barre_t:
            return 3
        else:
            return 2

    def peutDescendre(self):
        """Si le pixel situé à la position X/Y est éteint,
        le descendre de tant de pixel (ici self.taille qui définit
        la descente."""
        try:
            if display.get_pixel(self.x, self.y+self.taille()) == 0:
                print(display.get_pixel(self.x, self.y+self.taille()))
                self.y += 1
                self.forme_barre = self.forme_barre.shift_down(1)
                return True
        except ValueError:
            pass

    def peutBouger(self):
        if self.x >= 0 and self.x <= 5:
            return True

    def allerADroite(self):
        self.forme_barre = self.forme_barre.shift_right(1)

    def allerAGauche(self):
        self.forme_barre = self.forme_barre.shift_left(1)


def additionnerBarres(tab_bars):
    result = Image("00000:" "00000:" "00000:" "00000:" "00000")
    for barre_dans_tab in barres_posees:
        result = result + barre_dans_tab
    print("Ajouter barre : {}".format(result))
    return result

def afficherBarre(barre, tab_bars):
    print(barre.forme_barre)
    display.show(barre.forme_barre + additionnerBarres(tab_bars))

barres_posees = []

for i in range(5):
    barre_courante = barre()
    while barre_courante.peutDescendre():
        if button_a.was_pressed():
            barre_courante.allerAGauche()
            afficherBarre(barre_courante, barres_posees)
        if button_b.was_pressed():
            barre_courante.allerADroite()
            afficherBarre(barre_courante, barres_posees)
        afficherBarre(barre_courante, barres_posees)
        sleep(300)

    barres_posees.append(barre_courante.forme_barre)
    display.show(additionnerBarres(barres_posees))
