#Importer les bibliothèques
import time
from tkinter import *
import random

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


#Position joueur initial


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


    #pour l'ennemi
    #Direction ennemi

    directionE1 = random.choice([-50,0,50])
    directionE2 = random.choice([-50,0,50])
    canevas.move(ennemi,directionE1, directionE2)

    print(jy)
    fenetre.update


def move_down (event):
    global jy

    canevas.move(joueur, 0, case)
    jy = jy + case

    if jy+case > hauteur:
        canevas.move(joueur, 0, -case)
        jy = jy -case


    #pour l'ennemi
    #Direction ennemi

    directionE1 = random.choice([-50,0,50])
    directionE2 = random.choice([-50,0,50])
    canevas.move(ennemi,directionE1, directionE2)

    print(jy)
    fenetre.update


def move_left (event):
    global jx

    canevas.move(joueur, -case, 0)
    jx = jx - case

    if jx < 0:
        canevas.move(joueur, case, 0)
        jx = jx + case


    #pour l'ennemi
    #Direction ennemi

    directionE1 = random.choice([-50,0,50])
    directionE2 = random.choice([-50,0,50])
    canevas.move(ennemi,directionE1, directionE2)

    print(jx)
    fenetre.update


def move_right (event):
    global jx

    canevas.move(joueur, case, 0)
    jx = jx + case

    if jx+case > largeur:
        canevas.move(joueur, -case, 0)
        jx = jx -case
    
    
    #pour l'ennemi
    #Direction ennemi

    directionE1 = random.choice([-50,0,50])
    directionE2 = random.choice([-50,0,50])
    canevas.move(ennemi,directionE1, directionE2)

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

#Position joueur

pjx1 = canevas.coords(joueur)[1]
pjy1 = canevas.coords(joueur)[1]
#pjx2 = canevas.coords(joueur)[2]
#pjy2 = canevas.coords(joueur)[3]







#L'ennemi

ennemi = canevas.create_rectangle(tjx, tjy, tjx1, tjy1, fill='red')


#Position Ennemi

pEx1 = canevas.coords(ennemi)[0]
pEy1 = canevas.coords(ennemi)[1]
#pEx2 = canevas.coords(ennemi)[2]
#pEy2 = canevas.coords(ennemi)[3]








#Cadriage

ligneCreer_x = 50
ligneCreer_y = 50

while ligneCreer_x < largeur:
    canevas.create_line(ligneCreer_x, 0, ligneCreer_x, hauteur)
    ligneCreer_x = ligneCreer_x + case

while ligneCreer_y < hauteur:
    canevas.create_line(0, ligneCreer_y, largeur, ligneCreer_y)
    ligneCreer_y = ligneCreer_y + case





#Zone de test























#Binds des touches de directions

fenetre.bind("<Key->", lambda event : move_up(event))
fenetre.bind("<Key-s>", lambda event : move_down(event))
fenetre.bind("<Key-q>", lambda event : move_left(event))
fenetre.bind("<Key-d>", lambda event : move_right(event))

fenetre.bind("<Key-Z>", lambda event : move_up(event))
fenetre.bind("<Key-S>", lambda event : move_down(event))
fenetre.bind("<Key-Q>", lambda event : move_left(event))
fenetre.bind("<Key-D>", lambda event : move_right(event))

fenetre.bind("<Key-Up>", lambda event : move_up(event))
fenetre.bind("<Key-Down>", lambda event : move_down(event))
fenetre.bind("<Key-Left>", lambda event : move_left(event))
fenetre.bind("<Key-Right>", lambda event : move_right(event))


#Autre

canevas.pack()
fenetre.mainloop()