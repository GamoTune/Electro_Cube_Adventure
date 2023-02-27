#Importer les bibliothèques
import time
from tkinter import *
import random




#Les variables


#Pour la fenêtre

largeur = 1000
hauteur = 700
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


#Edition

edit = 0

blockXCoordsList = []
blockYCoordsList = []

#Deplacement basique



def move_up (event): 
    global jy
    pad = 0
    verite = False
    while pad != len(blockXCoordsList):
        coordsX = blockXCoordsList[pad]
        coordsY = blockYCoordsList[pad]
        if jy-case == coordsY and jx == coordsX:
            canevas.move(joueur, 0, 0)
            verite = True
        pad += 1
        
    
    if verite == False:
        if jy-50 < 0:
            canevas.move(joueur, 0, 0)
        else:
            canevas.move(joueur, 0, -case)
            jy += -case

    print(jy)

def move_down (event):
    global jy
    pad = 0
    verite = False
    while pad != len(blockXCoordsList):
        coordsX = blockXCoordsList[pad]
        coordsY = blockYCoordsList[pad]
        if jy+case == coordsY and jx == coordsX:
            canevas.move(joueur, 0, 0)
            verite = True
        pad += 1
        
    
    if verite == False:
        if jy+50 >= hauteur:
            canevas.move(joueur, 0, 0)
        else:
            canevas.move(joueur, 0, case)
            jy += case
    print(jy)

def move_left (event):
    global jx
    pad = 0
    verite = False
    while pad != len(blockXCoordsList):
        coordsX = blockXCoordsList[pad]
        coordsY = blockYCoordsList[pad]
        if jy == coordsY and jx-case == coordsX:
            canevas.move(joueur, 0, 0)
            verite = True
        pad += 1
        
    
    if verite == False:
        if jx-50 < 0:
            canevas.move(joueur, 0, 0)
        else:
            canevas.move(joueur, -case, 0)
            jx += -case
    print(jx)

def move_right (event):
    global jx
    pad = 0
    verite = False
    while pad != len(blockXCoordsList):
        coordsX = blockXCoordsList[pad]
        coordsY = blockYCoordsList[pad]
        if jy == coordsY and jx+case == coordsX:
            canevas.move(joueur, 0, 0)
            verite = True
        pad += 1
        
    
    if verite == False:
        if jx+50 >= largeur:
            canevas.move(joueur, 0, 0)
        else:
            canevas.move(joueur, case, 0)
            jx += case
    print(jx)


def edition (event):
    global edit

    if edit == 0:
        edit = 1
    else:
        edit = 0
    print(edit)


def plassage_de_block (event):
    global blockXCoordsList
    global blockYCoordsList
    xsouris,ysouris=event.x,event.y

    xsouris = (xsouris/case)
    xsouris = int(xsouris)
    xsouris = xsouris*case

    ysouris = (ysouris/case)
    ysouris = int(ysouris)
    ysouris = ysouris*case
    
    if edit == 1:
        block1 = canevas.create_rectangle(xsouris,ysouris,xsouris+50,ysouris+50, fill='black')
        blockXCoordsList.append(canevas.coords(block1)[0])
        blockYCoordsList.append(canevas.coords(block1)[1])
        print(xsouris,ysouris)
        print(blockYCoordsList)
        print(blockXCoordsList)



#Mise en place de la fenetre

fenetre = Tk()

fenetre.title('Dessin d\'un rectangle')
fenetre.geometry("%dx%d%+d%+d" % (largeur,hauteur,x_fenetre,y_fenetre))

canevas = Canvas(fenetre, width=largeur, height=hauteur,bg='grey')


#Le joueur

joueur = canevas.create_rectangle(tjx, tjy, tjx1, tjy1, fill='blue')

canevas.move(joueur,jx, jy)


#Position joueur

pjx1 = canevas.coords(joueur)[0]
pjy1 = canevas.coords(joueur)[1]
#pjx2 = canevas.coords(joueur)[2]
#pjy2 = canevas.coords(joueur)[3]


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

fenetre.bind("<Key-z>", lambda event : move_up(event))
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

fenetre.bind("<Key-e>", lambda event : edition(event))
fenetre.bind("<Key-E>", lambda event : edition(event))

fenetre.bind("<Button-1>", lambda event : plassage_de_block(event))


#Autre

canevas.pack()
fenetre.mainloop()