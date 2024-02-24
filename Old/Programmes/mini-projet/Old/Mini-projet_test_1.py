#Importer les bibliothèques
import time
from tkinter import *


#Les variables




#Pour la fenêtre

largeur = 900
hauteur = 600
x_fenetre = 10
y_fenetre = 10


#Taille du joueur (=50x50)

tjx = 0
tjy = 0
tjx1 = 50
tjy1 = 50


#Position joueur


jx = largeur/2
jy = hauteur/2


#Taille d'une case (=50x50)

case = 50


#Deplacement basique

def move_up (event):
    global jy,jx,joueur

    canevas.move(joueur, 0,-case)
    jy = jy - case
    
    if jy < 0:
        canevas.move(joueur, jx, 0)
        jy = 0

    print(jy)
    fenetre.update


def move_down (event):
    global jy,jx,joueur

    canevas.move(joueur, 0,case)
    jy = jy + case

    if jy > hauteur:
        canevas.move(joueur, jx, hauteur)
        jy = 0

    print(jy)
    fenetre.update


def move_left (event):
    global jx,jy,joueur

    canevas.move(joueur, -case,0)
    jx = jx - case

    if jx < 0:
        canevas.move(joueur, 0, jy)
        jy = 0

    print(jx)
    fenetre.update


def move_right (event):
    global jx,jy,joueur

    canevas.move(joueur, case,0)
    jx = jx + case

    if jx > largeur:
        canevas.move(joueur, largeur, jy)
        jy = 0

    print(jx)
    fenetre.update

#Mise en place de la fenetre

fenetre = Tk()

fenetre.title('Dessin d\'un rectangle')
fenetre.geometry("%dx%d%+d%+d" % (largeur,hauteur,x_fenetre,y_fenetre))

canevas = Canvas(fenetre, width=largeur, height=hauteur,bg='grey')


#Le joueur

joueur = canevas.create_rectangle(tjx, tjy, tjx1, tjy1, fill='blue')

canevas.move(joueur,largeur/2, hauteur/2)


if jx < 0:
    canevas.move(joueur, 0, jy)
    jx = 0
    print(jx)
    fenetre.update




canevas.pack()


#Binds

fenetre.bind("<Key-z>", lambda event : move_up(event))
fenetre.bind("<Key-s>", lambda event : move_down(event))
fenetre.bind("<Key-q>", lambda event : move_left(event))
fenetre.bind("<Key-d>", lambda event : move_right(event))

#Autre


fenetre.mainloop()