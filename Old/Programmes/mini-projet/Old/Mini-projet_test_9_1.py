#Importer les bibliothèques

from tkinter import *


################################################################### Les Fonctions ###################################################################


def move_up (event):
    global pjy1
    global pjy2
    global pjx1
    global pjx2
    pad = 0
    verify = False
    
    while pad != len(listblock):
        coordsX1 = blockX1CoordsList[pad]
        coordsY1 = blockY1CoordsList[pad]
        coordsX2 = blockX2CoordsList[pad]
        coordsY2 = blockY2CoordsList[pad]
        if coordsY1 <= pjy1-case < coordsY2 and coordsX1 <= pjx1 < coordsX2:
            verify = True
        pad += 1

    if verify == False:
        if pjy1-case < 0:
            pass
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
    while pad != len(listblock):
        coordsX1 = blockX1CoordsList[pad]
        coordsY1 = blockY1CoordsList[pad]
        coordsX2 = blockX2CoordsList[pad]
        coordsY2 = blockY2CoordsList[pad]
        if coordsY1 < pjy2+case <= coordsY2 and coordsX1 <= pjx1 < coordsX2:
            verify = True
        pad += 1

    if verify == False:
        if pjy2+case >= hauteur:
            pass
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
    while pad != len(listblock):
        coordsX1 = blockX1CoordsList[pad]
        coordsY1 = blockY1CoordsList[pad]
        coordsX2 = blockX2CoordsList[pad]
        coordsY2 = blockY2CoordsList[pad]
        if coordsX1 <= pjx1-case < coordsX2 and coordsY1 <= pjy1 < coordsY2:
            verify = True
        pad += 1

    if verify == False:
        if pjx1-case < 0:
            pass
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
    while pad != len(listblock):
        coordsX1 = blockX1CoordsList[pad]
        coordsY1 = blockY1CoordsList[pad]
        coordsX2 = blockX2CoordsList[pad]
        coordsY2 = blockY2CoordsList[pad]
        if coordsX1 < pjx2+case <= coordsX2 and coordsY1 <= pjy1 < coordsY2:
            verify = True
        pad += 1

    if verify == False:
        if pjx2+case >= largeur:
            pass
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
    global block
    global listblock


    


    xsouris,ysouris=event.x,event.y
    #xsouris -= case/2
    #ysouris -= case/2

    xsouris = (xsouris/case)
    xsouris = int(xsouris)
    xsouris = xsouris*case #+case/2
    #xsouris -= case/2


    ysouris = (ysouris/case)
    ysouris = int(ysouris)
    ysouris = ysouris*case #+case/2
    #ysouris += case/2
    #print(xsouris,ysouris)

    padsouris = 0
    verify = False
    while padsouris != len(listblock):
        coordsblockX1 = blockX1CoordsList[padsouris]
        coordsblockY1 = blockY1CoordsList[padsouris]

        if xsouris == coordsblockX1 and ysouris == coordsblockY1:
            verify = True
        padsouris += 1

    
    if edit == 1 and verify != True:

        block = canevas.create_rectangle(xsouris,ysouris,xsouris+case,ysouris+case, fill='black')
        listblock.append(block)
       # blockX1CoordsList.append(canevas.coords(block)[0])
       # blockY1CoordsList.append(canevas.coords(block)[1])
       # blockX2CoordsList.append(canevas.coords(block)[2])
       # blockY2CoordsList.append(canevas.coords(block)[3])
        blockX1CoordsList.append(xsouris)
        blockY1CoordsList.append(ysouris)
        blockX2CoordsList.append(xsouris+case)
        blockY2CoordsList.append(ysouris+case)
        print("liste des blocs : \n",listblock)
        print("Taille liste blocs : ", len(listblock))
        print("liste coords X1 : \n",blockX1CoordsList)
        print("liste coords Y1 : \n",blockY1CoordsList)
        print("liste coords X2 : \n",blockX2CoordsList)
        print("liste coords Y2 : \n",blockY2CoordsList)


def destroy_fenetre (event):
    fenetre.destroy()

def deleteblock (event):
    global listblock
    global blockX1CoordsList
    global blockX2CoordsList
    global blockY1CoordsList
    global blockY2CoordsList
    global a
    
    padblocklist = 0
    while padblocklist < len(listblock):
        canevas.delete(listblock[padblocklist])
        padblocklist += 1
    listblock.clear()
    blockX1CoordsList.clear()
    blockY1CoordsList.clear()
    blockX2CoordsList.clear()
    blockY2CoordsList.clear()
    print(listblock)

def deleteLastBlock (event):
    global listblock
    global blockX1CoordsList
    global blockX2CoordsList
    global blockY1CoordsList
    global blockY2CoordsList
    if len(listblock) > 0:
        canevas.delete(listblock[len(listblock)-1])
        del listblock[-1]
        del blockX1CoordsList[-1]
        del blockY1CoordsList[-1]
        del blockX2CoordsList[-1]
        del blockY2CoordsList[-1]
        print(listblock)

def loadTestZone (event):
    global listblock
    global blockX1CoordsList
    global blockY1CoordsList
    global blockX2CoordsList
    global blockY2CoordsList
    rang = 0

    padblocklist = 0
    while padblocklist < len(listblock):
        canevas.delete(listblock[padblocklist])
        padblocklist += 1
    listblock.clear()
    blockX1CoordsList.clear()
    blockY1CoordsList.clear()
    blockX2CoordsList.clear()
    blockY2CoordsList.clear()
    print(listblock)

    tailleListeBlocs = 222
    blockX1CoordsList = [0, 53, 106, 159, 212, 265, 318, 371, 424, 477, 530, 583, 636, 689, 742, 795, 848, 901, 954, 1007, 1060, 1113, 1166, 1219, 1272, 1325, 1378, 1431, 1484, 1537, 1590, 1643, 1696, 1749, 1802, 1855, 1908, 1961, 2014, 2067, 2120, 2173, 2226, 2279, 2332, 2385, 2438, 2491, 2544, 2544, 2491, 2491, 2544, 2544, 2491, 2491, 2544, 2544, 2491, 2491, 2544, 2544, 2491, 2491, 2544, 2544, 2491, 2491, 2544, 2544, 2491, 2491, 2544, 2491, 2491, 2544, 2544, 2491, 2544, 2544, 2491, 2491, 2544, 2544, 2491, 2491, 2544, 2544, 2491, 2491, 2544, 2544, 2491, 2491, 2544, 2491, 2544, 2544, 2491, 2491, 2544, 2544, 2491, 2438, 2438, 2385, 2385, 2332, 2279, 2226, 2173, 2120, 2067, 2014, 1961, 1908, 1855, 1802, 1749, 1696, 1643, 1590, 1537, 1484, 1431, 1378, 1325, 1272, 1219, 1166, 1113, 1060, 1060, 1007, 1007, 954, 901, 848, 795, 742, 689, 636, 583, 530, 477, 424, 371, 318, 265, 212, 159, 106, 53, 0, 0, 53, 106, 159, 212, 265, 318, 371, 424, 477, 530, 583, 636, 689, 742, 795, 848, 901, 954, 1113, 1166, 1219, 1272, 1325, 1378, 1431, 1484, 1537, 1590, 1643, 1696, 1749, 1802, 1855, 1908, 1961, 2014, 2067, 2120, 2173, 2226, 2279, 2332, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    blockY1CoordsList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 53, 53, 106, 106, 159, 159, 212, 212, 265, 265, 318, 318, 371, 371, 424, 424, 477, 477, 530, 530, 583, 583, 636, 636, 689, 742, 742, 689, 795, 795, 848, 848, 901, 901, 954, 954, 1007, 1007, 1060, 1060, 1113, 1113, 1166, 1166, 1219, 1219, 1272, 1272, 1325, 1325, 1378, 1378, 1431, 1431, 1431, 1378, 1378, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1378, 1378, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1378, 1325, 1272, 1219, 1166, 1113, 1060, 1007, 954, 901, 848, 795, 742, 689, 636, 583, 530, 477, 424, 371, 318, 265, 212, 159, 106, 53]
    blockX2CoordsList = [53, 106, 159, 212, 265, 318, 371, 424, 477, 530, 583, 636, 689, 742, 795, 848, 901, 954, 1007, 1060, 1113, 1166, 1219, 1272, 1325, 1378, 1431, 1484, 1537, 1590, 1643, 1696, 1749, 1802, 1855, 1908, 1961, 2014, 2067, 2120, 2173, 2226, 2279, 2332, 2385, 2438, 2491, 2544, 2597, 2597, 2544, 2544, 2597, 2597, 2544, 2544, 2597, 2597, 2544, 2544, 2597, 2597, 2544, 2544, 2597, 2597, 2544, 2544, 2597, 2597, 2544, 2544, 2597, 2544, 2544, 2597, 2597, 2544, 2597, 2597, 2544, 2544, 2597, 2597, 2544, 2544, 2597, 2597, 2544, 2544, 2597, 2597, 2544, 2544, 2597, 2544, 2597, 2597, 2544, 2544, 2597, 2597, 2544, 2491, 2491, 2438, 2438, 2385, 2332, 2279, 2226, 2173, 2120, 2067, 2014, 1961, 1908, 1855, 1802, 1749, 1696, 1643, 1590, 1537, 1484, 1431, 1378, 1325, 1272, 1219, 1166, 1113, 1113, 1060, 1060, 1007, 954, 901, 848, 795, 742, 689, 636, 583, 530, 477, 424, 371, 318, 265, 212, 159, 106, 53, 53, 106, 159, 212, 265, 318, 371, 424, 477, 530, 583, 636, 689, 742, 795, 848, 901, 954, 1007, 1166, 1219, 1272, 1325, 1378, 1431, 1484, 1537, 1590, 1643, 1696, 1749, 1802, 1855, 1908, 1961, 2014, 2067, 2120, 2173, 2226, 2279, 2332, 2385, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53]
    blockY2CoordsList = [53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 106, 106, 159, 159, 212, 212, 265, 265, 318, 318, 371, 371, 424, 424, 477, 477, 530, 530, 583, 583, 636, 636, 689, 689, 742, 795, 795, 742, 848, 848, 901, 901, 954, 954, 1007, 1007, 1060, 1060, 1113, 1113, 1166, 1166, 1219, 1219, 1272, 1272, 1325, 1325, 1378, 1378, 1431, 1431, 1484, 1484, 1484, 1431, 1431, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1431, 1431, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1484, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1431, 1378, 1325, 1272, 1219, 1166, 1113, 1060, 1007, 954, 901, 848, 795, 742, 689, 636, 583, 530, 477, 424, 371, 318, 265, 212, 159, 106]

    while rang < tailleListeBlocs:
        block = canevas.create_rectangle(blockX1CoordsList[rang], blockY1CoordsList[rang], blockX2CoordsList[rang], blockY2CoordsList[rang], fill='black')
        rang += 1
        listblock.append(block)
        print(rang)
        print(len(listblock))

    canevas.moveto(joueur,case, case)


################################################################### Mise en place de la fenetre ###################################################################

fenetre = Tk()

largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()

fenetre.title('Dessin d\'un rectangle')
#fenetre.geometry("%dx%d%+d%+d" % (largeur,hauteur,x_fenetre,y_fenetre))
fenetre.attributes('-fullscreen', True)
canevas = Canvas(fenetre, width=largeur, height=hauteur,bg='grey')



################################################################### Les Variables ###################################################################

case = int(largeur/48)
print("largeur ecran : ",largeur)
print("case : ",case)


#Edition

edit = 0
block = 0


#POUR TEST UN CODE DE NIVEAU IL FAUT LE METTRE DANS LES VARIABLES EN DESSOUS

blockX1CoordsList = []
blockY1CoordsList = []
blockX2CoordsList = []
blockY2CoordsList = []

listblock = []

tailleListeBlocs = 0

editionTEST = 0


if editionTEST == 1:
    for i in range(len(blockX1CoordsList)):
        listblock.append(canevas.create_rectangle(blockX1CoordsList[i],blockY1CoordsList[i],blockX2CoordsList[i],blockY2CoordsList[i], fill='black'))



################################################################### Le Cadriage ###################################################################


ligneCreer_x = case
ligneCreer_y = case

while ligneCreer_x <= largeur:
    canevas.create_line(ligneCreer_x, 0, ligneCreer_x, hauteur)
    ligneCreer_x += case

while ligneCreer_y <= hauteur:
    canevas.create_line(0, ligneCreer_y, largeur, ligneCreer_y)
    ligneCreer_y += case






################################################################### Le Joueur ###################################################################

#Position joueur initial

posjxstart = 0
posjystart = 0

joueur = canevas.create_rectangle(0, 0, case, case, fill='blue')

canevas.move(joueur,posjxstart, posjystart)


#Listes des positions du joueur

pjx1 = canevas.coords(joueur)[0]
pjy1 = canevas.coords(joueur)[1]
pjx2 = canevas.coords(joueur)[2]
pjy2 = canevas.coords(joueur)[3]






################################################################### Zone de Test ###################################################################












################################################################### Les Binds ###################################################################

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

fenetre.bind("<B1-Motion>", lambda event : plassage_de_block(event))
fenetre.bind("<Button-1>", lambda event : plassage_de_block(event))

fenetre.bind("<Escape>", lambda event : destroy_fenetre(event))

fenetre.bind("<Button-3>", lambda event : deleteblock(event))

fenetre.bind("<Button-2>", lambda event : deleteLastBlock(event))
fenetre.bind("<MouseWheel>", lambda event : deleteLastBlock(event))

fenetre.bind("<Key-t>", lambda event : loadTestZone(event))




#Autre

canevas.pack()
fenetre.mainloop()