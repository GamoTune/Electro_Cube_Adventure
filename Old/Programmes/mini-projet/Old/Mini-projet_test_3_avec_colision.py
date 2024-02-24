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
    global jy

    canevas.move(joueur, 0, -case)
    jy = jy - case

    if jy < 0:
        canevas.move(joueur, 0, case)
        jy = jy + case


    print(jy)
    fenetre.update


def move_down (event):
    global jy

    canevas.move(joueur, 0, case)
    jy = jy + case

    if jy+case > hauteur:
        canevas.move(joueur, 0, -case)
        jy = jy -case

    print(jy)
    fenetre.update


def move_left (event):
    global jx

    canevas.move(joueur, -case, 0)
    jx = jx - case

    if jx < 0:
        canevas.move(joueur, case, 0)
        jx = jx + case

    print(jx)
    fenetre.update


def move_right (event):
    global jx

    canevas.move(joueur, case, 0)
    jx = jx + case

    if jx+case > largeur:
        canevas.move(joueur, -case, 0)
        jx = jx -case

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



#Zone de test













canevas.pack()


#Binds

fenetre.bind("<Key-z>", lambda event : move_up(event))
fenetre.bind("<Key-s>", lambda event : move_down(event))
fenetre.bind("<Key-q>", lambda event : move_left(event))
fenetre.bind("<Key-d>", lambda event : move_right(event))

fenetre.bind("<Key-Z>", lambda event : move_up(event))
fenetre.bind("<Key-S>", lambda event : move_down(event))
fenetre.bind("<Key-Q>", lambda event : move_left(event))
fenetre.bind("<Key-D>", lambda event : move_right(event))

#Autre


fenetre.mainloop()