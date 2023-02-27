#Importer les bibliothèques

from tkinter import *
import pickle


################################################################### Les Fonctions ###################################################################

def first_launch ():
    global coordsBlocs
    global listblock
    global dicoSave
    global id_level
    global lienfichier
    global direciton
    global edit
    global block
    global nombrePixel
    global nombreCaseX
    global nombreCaseY
    global imageBoutonSolo
    global imageBoutonEditeur
    global ligneX
    global ligneY

    coordsBlocs = [] #0 = x & 1 = y
    listblock = []
    dicoSave = {"coordsBlocs" : [], "tpJoueur" : []}
    id_level = [0,0]
    lienfichier = "assets\\data\\level_editeur.txt"
    direciton = ""
    edit = 0
    block = 0
    nombreCase = 48 #En largeur (default = 48)
    nombrePixel = largeur/nombreCase
    nombreCaseX = largeur/nombrePixel
    nombreCaseY = hauteur/nombrePixel
    imageBoutonSolo = PhotoImage(file = r"assets\\images\\bouton_solo.png")
    imageBoutonEditeur = PhotoImage(file = r"assets\\images\\bouton_editeur.png")
    ligneX = []
    ligneY = []
    menu()

def lancement_edition ():
    global edit
    global lienfichier
    global ligneX

######################################################################## Le cadirage
    ligneCreer_x = nombrePixel
    ligneCreer_y = nombrePixel


    while ligneCreer_x <= largeur:
        ligneX.append(canevas.create_line(ligneCreer_x, 0, ligneCreer_x, hauteur))
        ligneCreer_x += nombrePixel

    while ligneCreer_y <= hauteur:
        ligneY.append(canevas.create_line(0, ligneCreer_y, largeur, ligneCreer_y))
        ligneCreer_y += nombrePixel
######################################################################## L'édition
    edit = 1
    lienfichier = "assets\\data\\level_editeur.txt"
    close_menu()

def lancement_solo ():
    global joueur
    global positionJoueur
    global lienfichier

    lienfichier = "assets\\data\\level1.txt"
    loadTestZone()
    posjxstart = 10
    posjystart = 13
    joueur = canevas.create_rectangle(0, 0, nombrePixel, nombrePixel, fill='blue')
    canevas.move(joueur,posjxstart*nombrePixel, posjystart*nombrePixel)
    positionJoueur = [posjxstart, posjystart] #0 = x & 1 = y
    close_menu()

def menu ():
    global boutonSolo
    global boutonEditeur
    global boutonExit
    global backMenu
    backMenu = canevas.create_rectangle(largeur/2-largeur/6, hauteur/2-hauteur/6,largeur/2+largeur/6, hauteur/2+hauteur/6,fill='black')
    boutonSolo = Button(fenetre, bd='1', image=imageBoutonSolo, command=lancement_solo)
    boutonSolo.place(x=largeur/2-largeur/6+50, y=hauteur/2)

    boutonEditeur = Button(fenetre, bd='1', image=imageBoutonEditeur, command=lancement_edition)
    boutonEditeur.place(x=largeur/2+largeur/6-103-50, y=hauteur/2)

    boutonExit = Button(fenetre, bd='1', text="Exit", command=fenetre.destroy)
    boutonExit.place(x=largeur/2-20, y=hauteur/2)

def close_menu ():
    boutonSolo.destroy()
    boutonEditeur.destroy()
    boutonExit.destroy()
    canevas.delete(backMenu)
################################################################### Fonction en jeu ###################################################################

def move_up (event):
    global positionJoueur
    global coordsBlocs
    global direciton

    pad = 0
    verify = False
    
    while pad != len(listblock):
        if  positionJoueur[0] == coordsBlocs[pad*2] and positionJoueur[1]-1 == coordsBlocs[pad*2+1]:
            verify = True
        pad += 1

    if verify == False:
        if positionJoueur[1] <= 0:
            direciton = "down"
            level_search()
            loadTestZone()
            positionJoueur[1] = nombreCaseY-1
            canevas.moveto(joueur, positionJoueur[0]*nombrePixel-1, positionJoueur[1]*nombrePixel-1)
        else:
            canevas.move(joueur, 0, -nombrePixel)
            positionJoueur[1] = positionJoueur[1]-1
    print(positionJoueur)

def move_down (event):
    global positionJoueur
    global coordsBlocs
    global direciton

    pad = 0
    verify = False
    
    while pad != len(listblock):
        if  positionJoueur[0] == coordsBlocs[pad*2] and positionJoueur[1]+1 == coordsBlocs[pad*2+1]:
            verify = True
        pad += 1

    if verify == False:
        if positionJoueur[1] >= nombreCaseY-1:
            direciton = "down"
            level_search()
            loadTestZone()
            positionJoueur[1] = 0
            canevas.moveto(joueur, positionJoueur[0]*nombrePixel-1, -positionJoueur[1]*nombrePixel-1)
        else:
            canevas.move(joueur, 0, nombrePixel)
            positionJoueur[1] = positionJoueur[1]+1
    print(positionJoueur)

def move_left (event):
    global positionJoueur
    global coordsBlocs

    global direciton

    pad = 0
    verify = False
    
    while pad != len(listblock):
        if  positionJoueur[0]-1 == coordsBlocs[pad*2] and positionJoueur[1] == coordsBlocs[pad*2+1]:
            verify = True
        pad += 1

    if verify == False:
        if positionJoueur[0] <= 0:
            direciton = "Left"
            level_search()
            loadTestZone()
            positionJoueur[0] = nombreCaseX-1
            canevas.moveto(joueur, positionJoueur[0]*nombrePixel-1, positionJoueur[1]*nombrePixel-1)
            
        else:
            canevas.move(joueur, -nombrePixel, 0)
            positionJoueur[0] = positionJoueur[0]-1
    print(positionJoueur)

def move_right (event):
    global positionJoueur
    global coordsBlocs
    global direciton

    pad = 0
    verify = False
    
    while pad != len(listblock):
        if  positionJoueur[0]+1 == coordsBlocs[pad*2] and positionJoueur[1] == coordsBlocs[pad*2+1]:
            verify = True
        pad += 1

    if verify == False:
        if positionJoueur[0] >= nombreCaseX-1:
            direciton = "Right"
            level_search()
            loadTestZone()
            positionJoueur[0] = 0
            canevas.moveto(joueur, -positionJoueur[0]*nombrePixel-1, positionJoueur[1]*nombrePixel-1)
            
        else:
            canevas.move(joueur, nombrePixel, 0)
            positionJoueur[0] = positionJoueur[0]+1
    print(positionJoueur)


################################################################### Fonction en édition ###################################################################

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

def deleteblock (event=0):
    global listblock
    global coordsBlocs
    
    padblocklist = 0
    while padblocklist < len(listblock) and edit == 1:
        canevas.delete(listblock[padblocklist])
        padblocklist += 1
    listblock.clear()
    coordsBlocs.clear()

def deleteLastBlock (event):
    global listblock
    global coordsBlocs

    if len(listblock) > 0 and edit == 1:
        canevas.delete(listblock[len(listblock)-1])
        del listblock[-1]
        del coordsBlocs[-1]
        del coordsBlocs[-1]

def save_level (event=0):
    if edit == 1:
        dicoSave["coordsBlocs"].append(coordsBlocs)
        with open("assets\\data\\level_editeur.txt", "wb") as fichierNiveau:
            pickle.dump(dicoSave, fichierNiveau)
        dicoSave["coordsBlocs"].clear()


################################################################### Fonction fonctionnement du programme ###################################################################

def retour_menu (event=0):
    global lienfichier
    global edit
    global ligneX
    global ligneY
    global joueur
    padblocklist = 0
    lienfichier = "assets\\data\\menu.txt"
    if edit == 1:
        edit = 0
        while padblocklist < len(ligneX):
            canevas.delete(ligneX[padblocklist])
            padblocklist += 1
        ligneX.clear()
        padblocklist = 0
        while padblocklist < len(ligneY):
            canevas.delete(ligneY[padblocklist])
            padblocklist += 1
        ligneY.clear()
    else:
        canevas.delete(joueur)
        positionJoueur.clear()
    loadTestZone()
    menu()

def loadTestZone (event=0):
    global listblock
    global coordsBlocs
    global dicoSave

    padblocklist = 0
    while padblocklist < len(listblock):
        canevas.delete(listblock[padblocklist])
        padblocklist += 1
    listblock.clear()
    coordsBlocs.clear()


    with open(lienfichier, "rb") as fichier:
        dicoSave = pickle.load(fichier)
    coordsBlocs = dicoSave["coordsBlocs"].pop(0)

    rang = 0
    while rang < len(coordsBlocs)/2:
        block = canevas.create_rectangle(coordsBlocs[(rang*2)]*nombrePixel, coordsBlocs[(rang*2+1)]*nombrePixel, coordsBlocs[(rang*2)]*nombrePixel+nombrePixel, coordsBlocs[(rang*2+1)]*nombrePixel+nombrePixel, fill='black')
        rang += 1
        listblock.append(block)
        print(rang)
        print(len(listblock))

def level_search ():
    global id_level
    global lienfichier
    if direciton == "Up":
        id_level[0] += 1
    if direciton == "Down":
        id_level[0] -= 1
    if direciton == "Left":
        id_level[0] += 1
    if direciton == "Right":
        id_level[0] += 1
    lienfichier = "assets\\data\\level"+str()+".txt"




################################################################### Mise en place de la fenetre ###################################################################

fenetre = Tk()

largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()

fenetre.title('Dessin d\'un rectangle')
#fenetre.geometry("%dx%d%+d%+d" % (largeur,hauteur,x_fenetre,y_fenetre))
fenetre.attributes('-fullscreen', True)
canevas = Canvas(fenetre, width=largeur, height=hauteur,bg='grey')


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

fenetre.bind("<B1-Motion>", lambda event : plassage_de_block(event))
fenetre.bind("<Button-1>", lambda event : plassage_de_block(event))

fenetre.bind("<Escape>", lambda event : retour_menu(event))

fenetre.bind("<Button-3>", lambda event : deleteblock(event))

fenetre.bind("<Button-2>", lambda event : deleteLastBlock(event))
fenetre.bind("<MouseWheel>", lambda event : deleteLastBlock(event))

fenetre.bind("<Key-t>", lambda event : loadTestZone(event))
fenetre.bind("<Key-g>", lambda event : save_level(event))

first_launch()


#Autre

canevas.pack()
fenetre.mainloop()