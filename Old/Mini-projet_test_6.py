#Importer les bibliothèques

from tkinter import *





#Les variables

#Taille d'une case (=50x50)

case = 50


#Pour la fenêtre

largeur = 1900
hauteur = 1100
x_fenetre = 0
y_fenetre = 0


#Taille du joueur (=50x50)

Taille = 50

tjx = 0
tjy = 0
tjx1 = Taille
tjy1 = Taille


#Position joueur initial


posjxstart = largeur/2
posjystart = hauteur/2


#Edition

edit = 0

blockX1CoordsList = []
blockY1CoordsList = []
blockX2CoordsList = []
blockY2CoordsList = []

nombreBlock = 0


#Animation de changement

tempo = 0
paddutempo = 1.75
validationCreationBlockTransi = 0
block = 0



#Deplacement basique



def move_up (event):
    global pjy1
    global pjy2
    global pjx1
    global pjx2
    pad = 0
    verify = False
    while pad != nombreBlock:
        coordsX1 = blockX1CoordsList[pad]
        coordsY1 = blockY1CoordsList[pad]
        coordsX2 = blockX2CoordsList[pad]
        coordsY2 = blockY2CoordsList[pad]
        if coordsY1 <= pjy1-case < coordsY2 and coordsX1 <= pjx1 < coordsX2:
            canevas.move(joueur, 0, 0)
            verify = True
        pad += 1

    if verify == False:
        if pjy1-case < 0:
            canevas.move(joueur, 0, 0)
        else:
            canevas.move(joueur, 0, -case)
    
    pjx1 = canevas.coords(joueur)[0]
    pjy1 = canevas.coords(joueur)[1]
    pjx2 = canevas.coords(joueur)[2]
    pjy2 = canevas.coords(joueur)[3]
    print(pjy1)

def move_down (event):
    global pjy1
    global pjy2
    global pjx1
    global pjx2
    pad = 0
    verify = False
    while pad != nombreBlock:
        coordsX1 = blockX1CoordsList[pad]
        coordsY1 = blockY1CoordsList[pad]
        coordsX2 = blockX2CoordsList[pad]
        coordsY2 = blockY2CoordsList[pad]
        if coordsY1 < pjy2+case <= coordsY2 and coordsX1 <= pjx1 < coordsX2:
            canevas.move(joueur, 0, 0)
            verify = True
        pad += 1

    if verify == False:
        if pjy1+case >= hauteur:
            canevas.move(joueur, 0, 0)
        else:
            canevas.move(joueur, 0, case)
    
    pjx1 = canevas.coords(joueur)[0]
    pjy1 = canevas.coords(joueur)[1]
    pjx2 = canevas.coords(joueur)[2]
    pjy2 = canevas.coords(joueur)[3]
    print(pjy1)

def move_left (event):
    global pjy1
    global pjy2
    global pjx1
    global pjx2
    pad = 0
    verify = False
    while pad != nombreBlock:
        coordsX1 = blockX1CoordsList[pad]
        coordsY1 = blockY1CoordsList[pad]
        coordsX2 = blockX2CoordsList[pad]
        coordsY2 = blockY2CoordsList[pad]
        if coordsX1 <= pjx1-case < coordsX2 and coordsY1 <= pjy1 < coordsY2:
            canevas.move(joueur, 0, 0)
            verify = True
        pad += 1

    if verify == False:
        if pjy1-case < 0:
            canevas.move(joueur, 0, 0)
        else:
            canevas.move(joueur, -case, 0)
    
    pjx1 = canevas.coords(joueur)[0]
    pjy1 = canevas.coords(joueur)[1]
    pjx2 = canevas.coords(joueur)[2]
    pjy2 = canevas.coords(joueur)[3]
    print(pjx1)

def move_right (event):
    global pjy1
    global pjy2
    global pjx1
    global pjx2
    pad = 0
    verify = False
    while pad != nombreBlock:
        coordsX1 = blockX1CoordsList[pad]
        coordsY1 = blockY1CoordsList[pad]
        coordsX2 = blockX2CoordsList[pad]
        coordsY2 = blockY2CoordsList[pad]
        if coordsX1 < pjx2+case <= coordsX2 and coordsY1 <= pjy1 < coordsY2:
            canevas.move(joueur, 0, 0)
            verify = True
        pad += 1

    if verify == False:
        if pjy1+case >= largeur:
            canevas.move(joueur, 0, 0)
        else:
            canevas.move(joueur, case, 0)
    
    pjx1 = canevas.coords(joueur)[0]
    pjy1 = canevas.coords(joueur)[1]
    pjx2 = canevas.coords(joueur)[2]
    pjy2 = canevas.coords(joueur)[3]
    print(pjx1)


def edition (event):
    global edit

    if edit == 0:
        edit = 1
    else:
        edit = 0
    print(edit)

def plassage_de_block (event):
    global nombreBlock

    xsouris,ysouris=event.x,event.y

    xsouris = (xsouris/case)
    xsouris = int(xsouris)
    xsouris = xsouris*case

    ysouris = (ysouris/case)
    ysouris = int(ysouris)
    ysouris = ysouris*case
    print(xsouris,ysouris)

    padsouris = 0
    verify = False
    while padsouris != nombreBlock:
        coordsblockX1 = blockX1CoordsList[padsouris]
        coordsblockY1 = blockY1CoordsList[padsouris]

        if xsouris == coordsblockX1 and ysouris == coordsblockY1:
            verify = True
        padsouris += 1

    
    if edit == 1 and verify != True:
        block1 = canevas.create_rectangle(xsouris,ysouris,xsouris+50,ysouris+50, fill='black')
        blockX1CoordsList.append(canevas.coords(block1)[0])
        blockY1CoordsList.append(canevas.coords(block1)[1])
        blockX2CoordsList.append(canevas.coords(block1)[2])
        blockY2CoordsList.append(canevas.coords(block1)[3])
        nombreBlock = nombreBlock + 1
        print(xsouris,ysouris,xsouris+case,ysouris+case)
        print(blockX1CoordsList)
        print(blockY1CoordsList)
        print(blockX2CoordsList)
        print(blockY2CoordsList)

def animation (event):
    global tempo
    global paddutempo
    global validationCreationBlockTransi
    global block

    if validationCreationBlockTransi == 0:
        validationCreationBlockTransi = 1
        block = canevas.create_rectangle(0,0,largeur,hauteur,fill='green')
        canevas.moveto(block,0,-hauteur)

    if tempo >= hauteur*2:
        canevas.delete(block)
        validationCreationBlockTransi = 0

    if tempo < hauteur*2:
        fenetre.after(1,animation(event))

    canevas.move(block,0,paddutempo)
    tempo += paddutempo
        
def destroid_fenetre (event):
    fenetre.destroy()
    

#Mise en place de la fenetre

fenetre = Tk()

fenetre.title('Dessin d\'un rectangle')
fenetre.geometry("%dx%d%+d%+d" % (largeur,hauteur,x_fenetre,y_fenetre))
fenetre.attributes('-fullscreen', True)
canevas = Canvas(fenetre, width=largeur*2, height=hauteur*2,bg='grey')


#Le joueur

joueur = canevas.create_rectangle(tjx, tjy, tjx1, tjy1, fill='blue')

canevas.move(joueur,posjxstart, posjystart)


#4 listes des position du joueur

pjx1 = canevas.coords(joueur)[0]
pjy1 = canevas.coords(joueur)[1]
pjx2 = canevas.coords(joueur)[2]
pjy2 = canevas.coords(joueur)[3]


#Cadriage

ligneCreer_x = case
ligneCreer_y = case

while ligneCreer_x < largeur:
    canevas.create_line(ligneCreer_x, 0, ligneCreer_x, hauteur)
    ligneCreer_x += case

while ligneCreer_y < hauteur:
    canevas.create_line(0, ligneCreer_y, largeur, ligneCreer_y)
    ligneCreer_y += case







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

fenetre.bind("<Key-a>", lambda event : animation(event))
fenetre.bind("<Escape>", lambda event : destroid_fenetre(event))


#Autre

canevas.pack()
fenetre.mainloop()