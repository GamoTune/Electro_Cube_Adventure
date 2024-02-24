#Importer les bibliothèques

from tkinter import *
import pickle


################################################################### Les Fonctions ###################################################################


def move_up (event):
    global positionJoueur
    global coordsBlocs

    pad = 0
    verify = False
    
    while pad != len(listblock):
        if  positionJoueur[0] == coordsBlocs[pad*2] and positionJoueur[1]-1 == coordsBlocs[pad*2+1]:
            verify = True
        pad += 1

    if verify == False:
        if positionJoueur[1] <= 0:
            pass
        else:
            canevas.move(joueur, 0, -nombrePixel)
            positionJoueur[1] = positionJoueur[1]-1
    print(positionJoueur)
    print(coordsBlocs)

def move_down (event):
    global positionJoueur
    global coordsBlocs

    pad = 0
    verify = False
    
    while pad != len(listblock):
        if  positionJoueur[0] == coordsBlocs[pad*2] and positionJoueur[1]+1 == coordsBlocs[pad*2+1]:
            verify = True
        pad += 1

    if verify == False:
        if positionJoueur[1] >= nombreCaseY-1:
            pass
        else:
            canevas.move(joueur, 0, nombrePixel)
            positionJoueur[1] = positionJoueur[1]+1
    print(positionJoueur)
    print(coordsBlocs)

def move_left (event):
    global positionJoueur
    global coordsBlocs

    pad = 0
    verify = False
    
    while pad != len(listblock):
        if  positionJoueur[0]-1 == coordsBlocs[pad*2] and positionJoueur[1] == coordsBlocs[pad*2+1]:
            verify = True
        pad += 1

    if verify == False:
        if positionJoueur[0] <= 0:
            pass
        else:
            canevas.move(joueur, -nombrePixel, 0)
            positionJoueur[0] = positionJoueur[0]-1
    print(positionJoueur)
    print(coordsBlocs)

def move_right (event):
    global positionJoueur
    global coordsBlocs

    pad = 0
    verify = False
    
    while pad != len(listblock):
        if  positionJoueur[0]+1 == coordsBlocs[pad*2] and positionJoueur[1] == coordsBlocs[pad*2+1]:
            verify = True
        pad += 1

    if verify == False:
        if positionJoueur[0] >= nombreCaseX-1:
            pass
        else:
            canevas.move(joueur, nombrePixel, 0)
            positionJoueur[0] = positionJoueur[0]+1
    print(positionJoueur)
    print(coordsBlocs)


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
    global coordsBlocs

    xSourisCase,ySourisCase=event.x,event.y

    xSourisCase = (xSourisCase/nombrePixel)
    xSourisCase = int(xSourisCase)

    ySourisCase = (ySourisCase/nombrePixel)
    ySourisCase = int(ySourisCase)

    padsouris = 0
    verify = False
    while padsouris != len(listblock):
        if xSourisCase == coordsBlocs[padsouris*2] and ySourisCase == coordsBlocs[padsouris*2+1]:
            verify = True
        padsouris += 1



    
    if edit == 1 and verify == False:

        block = canevas.create_rectangle(xSourisCase*nombrePixel,ySourisCase*nombrePixel,xSourisCase*nombrePixel+nombrePixel,ySourisCase*nombrePixel+nombrePixel, fill='black')
        listblock.append(block)
        coordsBlocs.append(xSourisCase)
        coordsBlocs.append(ySourisCase)
    print(coordsBlocs)


def destroy_fenetre (event):
    fenetre.destroy()

def deleteblock (event):
    global listblock
    global coordsBlocs
    
    padblocklist = 0
    while padblocklist < len(listblock):
        canevas.delete(listblock[padblocklist])
        padblocklist += 1
    listblock.clear()
    coordsBlocs.clear()


def deleteLastBlock (event):
    global listblock
    global coordsBlocs

    if len(listblock) > 0:
        canevas.delete(listblock[len(listblock)-1])
        del listblock[-1]
        del coordsBlocs[-1]
        del coordsBlocs[-1]


def loadTestZone (event):
    global listblock
    global coordsBlocs
    global dicoSave
    global positionJoueur

    padblocklist = 0
    while padblocklist < len(listblock):
        canevas.delete(listblock[padblocklist])
        padblocklist += 1
    listblock.clear()
    coordsBlocs.clear()
    positionJoueur.clear()

    with open("E:\\Programmes\\data\\level_test1.txt", "rb") as fichier:
        dicoSave = pickle.load(fichier)
    
    coordsBlocs = dicoSave["coordsBlocs"].pop(0)
    positionJoueur = dicoSave["tpJoueur"].pop(0)

    rang = 0
    while rang < len(coordsBlocs)/2:
        block = canevas.create_rectangle(coordsBlocs[(rang*2)]*nombrePixel, coordsBlocs[(rang*2+1)]*nombrePixel, coordsBlocs[(rang*2)]*nombrePixel+nombrePixel, coordsBlocs[(rang*2+1)]*nombrePixel+nombrePixel, fill='black')
        rang += 1
        listblock.append(block)
        print(rang)
        print(len(listblock))

    canevas.moveto(joueur, positionJoueur[0]*nombrePixel, positionJoueur[1]*nombrePixel)

def save_level (event):
    dicoSave["coordsBlocs"].append(coordsBlocs)
    dicoSave["tpJoueur"].append(positionJoueur)
    with open("E:\\Programmes\\data\\level_test1.txt", "wb") as fichierNiveau:
        pickle.dump(dicoSave, fichierNiveau)
    dicoSave["coordsBlocs"].clear()
    dicoSave["tpJoueur"].clear()



################################################################### Mise en place de la fenetre ###################################################################

fenetre = Tk()

largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()

fenetre.title('Dessin d\'un rectangle')
#fenetre.geometry("%dx%d%+d%+d" % (largeur,hauteur,x_fenetre,y_fenetre))
fenetre.attributes('-fullscreen', True)
canevas = Canvas(fenetre, width=largeur, height=hauteur,bg='grey')



################################################################### Les Variables ###################################################################

nombreCase = 48 #En largeur (default = 48)

nombrePixel = int(largeur/nombreCase)
print("largeur ecran : ",largeur)
print("nombrePixel : ",nombrePixel)

nombreCaseX = largeur/nombrePixel
nombreCaseY = hauteur/nombrePixel


################################################################### Edition ###################################################################

edit = 0
block = 0

coordsBlocs = [] #0 = x & 1 = y

listblock = []

dicoSave = {"coordsBlocs" : [], "tpJoueur" : []}

################################################################### Le Cadriage ###################################################################


ligneCreer_x = nombrePixel
ligneCreer_y = nombrePixel

while ligneCreer_x <= largeur:
    canevas.create_line(ligneCreer_x, 0, ligneCreer_x, hauteur)
    ligneCreer_x += nombrePixel

while ligneCreer_y <= hauteur:
    canevas.create_line(0, ligneCreer_y, largeur, ligneCreer_y)
    ligneCreer_y += nombrePixel






################################################################### Le Joueur ###################################################################

#Position joueur initial

posjxstart = 2
posjystart = 2

#Creation

joueur = canevas.create_rectangle(0, 0, nombrePixel, nombrePixel, fill='blue')

canevas.move(joueur,posjxstart*nombrePixel, posjystart*nombrePixel)


#Liste des positions du joueur

positionJoueur = [posjxstart, posjystart] #0 = x & 1 = y
print(positionJoueur)

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
fenetre.bind("<Key-g>", lambda event : save_level(event))




#Autre

canevas.pack()
fenetre.mainloop()