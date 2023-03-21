#Importer les bibliothèques

from tkinter import *
import tkinter as tk
import pickle
import os


################################################################### Les Fonctions ###################################################################

def first_launch (): #La fonction "first_launch" permet de déclaré la plus part des variable global
    global listblock, dicoNiveau, id_level, lienfichier, edit, nombrePixel, nombreCaseX, nombreCaseY, imageBoutonSolo, imageBoutonEditeur, ligneX, ligneY, imageBoutonEditeurNiveauHaut, imageBoutonEditeurNiveauBas, imageBoutonEditeurNiveauGauche, imageBoutonEditeurNiveauDroite, imageBoutonEditeurSave, imageBoutonEditeurRetour, imageWIP, imageBoutonEditeurPoubelle, imageBoutonEditeurExit, imageBoutonEditeurInfos, fenetreinfosTest, id_level_editeur, imageBoutonEditeurBlocSolide, couleurBloc, typeDuBloc, imageBoutonEditeurBlocSpawn, delonespebloc, dicoMonde, id_monde, solo

    #Les coordonnées virtuel sont des coordonnées d'un matrice créer en fonction du nombre de case à l'écran (défini avec "nombreCase")
    listblock = [] #Liste des ID des blocs créés [default : []]
    dicoNiveau = {
        "coordsBloc" : [],
        "listBloc" : [],
        "typeBloc" : [],
        "color" : []

         }
    dicoMonde = {
        "keyPorte" : []
    }
          #Dictionnaire des informations d'un niveau (comme les coordonnées des blocs) qui sont enregistrer
    id_level = [0,0] #Numéro du niveau dans le quel on est (quand on change de niveau on ajoute ou retire 1 ) [default : [0,0]]
    id_monde = 0
    lienfichier = "assets/data/menu.txt" #Lien a utiliser pour charger ou sauvegarder un niveau [default : "assets/data/menu.txt"]
    edit = False #Permet de vérifier si le mode d'édition est activer [default : False]
    nombreCase = 48 #En largeur (default = 48)
    nombrePixel = largeur/nombreCase #nombrePixel = nombre de pixels par case sur l'écran (en fonction de la résolution de l'écran, le nombre de pixel change pour toujours avoir le même nombre de case à l'écran)
    nombreCaseX = largeur/nombrePixel #Le nombre de case en X permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en X
    nombreCaseY = hauteur/nombrePixel #Le nombre de case en Y permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en Y
    imageBoutonSolo = PhotoImage(file = r"assets/images/bouton_solo.png") #Image du bouton du solo sur le menu principal
    imageBoutonEditeur = PhotoImage(file = r"assets/images/bouton_editeur.png") #Image du bouton de l'éditeur sur le menu principal
    ligneX = [] #Liste des ID des lignes X crées
    ligneY = [] #Liste des ID des lignes X crées    
    fenetreinfosTest = 0 #Permet de vérifier si la fenetre d'info de l'éditeur est déjà créer
    id_level_editeur = [0,0]
    couleurBloc = 'black'
    typeDuBloc = 0
    delonespebloc = False
    solo = False
    imageBoutonEditeurNiveauHaut = PhotoImage(file = r"assets/images/fleche_haut.png")
    imageBoutonEditeurNiveauBas = PhotoImage(file = r"assets/images/fleche_bas.png")
    imageBoutonEditeurNiveauGauche = PhotoImage(file = r"assets/images/fleche_gauche.png")
    imageBoutonEditeurNiveauDroite = PhotoImage(file = r"assets/images/fleche_droite.png")
    imageBoutonEditeurSave = PhotoImage(file = r"assets/images/save.png")
    imageBoutonEditeurRetour = PhotoImage(file = r"assets/images/retour.png")
    imageWIP = PhotoImage(file = r"assets/images/WIP.png")
    imageBoutonEditeurPoubelle = PhotoImage(file = r"assets/images/bouton_poubelle.png")
    imageBoutonEditeurExit = PhotoImage(file = r"assets/images/exit.png")
    imageBoutonEditeurInfos = PhotoImage(file = r"assets/images/Menu_infos.png")
    imageBoutonEditeurBlocSolide = PhotoImage(file = r"assets/images/bouton_bloc_solide.png")
    imageBoutonEditeurBlocSpawn = PhotoImage(file= r"assets/images/bouton_bloc_spawn.png")
    menu()

def lancement_edition (): #La fonction "lancement_edition" permet de mettre en place tout le système de la création de niveau
    global edit
    global lienfichier
    global ligneX
    global fenetre_bouton
    global id_level
    global numeroNiveau
    
    close_menu() #Ferme le menu

######################################################################## Le cadirage
    ligneCreer_x = nombrePixel
    ligneCreer_y = nombrePixel

#Création des ligne de l'éditeur (le cadriage dans le fond qui permet de mieux savoir où les blocs seront placer)
    while ligneCreer_x <= largeur: 
        ligneX.append(canevas.create_line(ligneCreer_x, 0, ligneCreer_x, hauteur))
        ligneCreer_x += nombrePixel

    while ligneCreer_y <= hauteur:
        ligneY.append(canevas.create_line(0, ligneCreer_y, largeur, ligneCreer_y))
        ligneCreer_y += nombrePixel

######################################################################## L'édition
    edit = True #Indication au programme que l'éditeur est lancer et que les fonction de l'édition peuvent maintement fonctionnner
    if id_level != id_level_editeur:
        id_level = id_level_editeur

    lienfichier = "assets/data/editeur//level_editeur"+str(id_level[0])+str(id_level[1])+".txt" #Changement du niveau à charger
    loadTestZone() #Appel de la fonction qui charge les niveau

    #Fenetre des infos / boutons
    fenetre_bouton = tk.Toplevel() #Création de la fenetre des fonction/boutons de l'éditeur
    fenetre_bouton.geometry('312x538') #taille 1 bouton = taille que tu veux + 3
    fenetre_bouton.resizable(False,False) #Fenetre non redimentionable
    fenetre_bouton.attributes('-topmost',1)
    
    bouton_save = Button(fenetre_bouton, image=imageBoutonEditeurSave, bg='white')
    bouton_save.place(x=0,y=0)

    bouton_retour = Button(fenetre_bouton, image=imageBoutonEditeurRetour, bg='white', command=deleteLastBlock)
    bouton_retour.place(x=103,y=0)

    boutonEditeurPoubelle = Button(fenetre_bouton, image=imageBoutonEditeurPoubelle, bg='white', command=deleteblock)
    boutonEditeurPoubelle.place(x=206,y=0)

    bouton_niveau_up = Button(fenetre_bouton, image=imageBoutonEditeurNiveauHaut, bg='white', command=lambda:level_search("up"))
    bouton_niveau_up.place(x=103,y=103)

    bouton_niveau_down = Button(fenetre_bouton, image=imageBoutonEditeurNiveauBas, bg='white', command=lambda:level_search("down"))
    bouton_niveau_down.place(x=103,y=309)
    
    bouton_niveau_left = Button(fenetre_bouton, image=imageBoutonEditeurNiveauGauche, bg='white', command=lambda:level_search("left"))
    bouton_niveau_left.place(x=0,y=206)

    bouton_niveau_right = Button(fenetre_bouton, image=imageBoutonEditeurNiveauDroite, bg='white', command=lambda:level_search("right"))
    bouton_niveau_right.place(x=206,y=206)

    boutonEditeurInfo = Button(fenetre_bouton, image=imageWIP, bg='white', command=info_editeur)
    boutonEditeurInfo.place(x=103,y=412)

    boutonEditeurExit = Button(fenetre_bouton, image=imageBoutonEditeurExit, bg='white', command=retour_menu)
    boutonEditeurExit.place(x=0,y=412)

    numeroNiveau = Label(fenetre_bouton, text=id_level, font="Arial, 30")
    numeroNiveau.pack(padx=103, pady=227)

    bouton_bloc_solide = Button(fenetre_bouton, image=imageBoutonEditeurBlocSolide, bg='white', command=lambda:typeBlocs("solide"))
    bouton_bloc_solide.place(x=0,y=103)

    bouton_bloc_spawn = Button(fenetre_bouton, image=imageBoutonEditeurBlocSpawn, bg='white', command=lambda:typeBlocs("spawn"))
    bouton_bloc_spawn.place(x=206,y=103)

    bouton_item_key = Button(fenetre_bouton, image=imageBoutonEditeurBlocSpawn, bg='white', command=lambda:typeBlocs("key"))
    bouton_item_key.place(x=0,y=309)

    bouton_gomme = Button(fenetre_bouton, image=imageBoutonEditeurBlocSpawn, bg='white', command=delspebloc)
    bouton_gomme.place(x=206,y=309)

def lancement_solo ():
    global joueur
    global positionJoueur
    global lienfichier
    global id_level
    global solo

    solo = True
    lienfichier = "assets/data/solo/level_editeur00.txt"
    id_level = [0,0]
    loadTestZone()
    posjxstart = 10
    posjystart = 13
    joueur = canevas.create_rectangle(0, 0, nombrePixel, nombrePixel, fill='blue')
    canevas.move(joueur,posjxstart*nombrePixel, posjystart*nombrePixel)
    positionJoueur = [posjxstart, posjystart] #0 = x & 1 = y
    close_menu()



def menu ():
    global boutonSolo, boutonEditeur, boutonExit, menuFrame
    loadTestZone()

    menuFrame = Frame(fenetre, width=largeur/2+largeur/4, height=hauteur/2+hauteur/4 ,bg='black')
    menuFrame.place(x=largeur/2, y=hauteur/2,anchor=CENTER)

    boutonSolo = Button(menuFrame, image=imageBoutonSolo, command=lancement_solo)
    boutonSolo.place(x=(largeur/2+largeur/4)/2-((largeur/2+largeur/4)/2)/2, y=(hauteur/2+hauteur/4)/2, anchor=CENTER)

    boutonEditeur = Button(menuFrame, image=imageBoutonEditeur, command=lancement_edition)
    boutonEditeur.place(x=(largeur/2+largeur/4)/2+((largeur/2+largeur/4)/2)/2, y=(hauteur/2+hauteur/4)/2, anchor=CENTER)

    boutonExit = Button(menuFrame, image=imageBoutonEditeurExit, command=fenetre.destroy)
    boutonExit.place(x=(largeur/2+largeur/4)/2, y=(hauteur/2+hauteur/4)/2, anchor=CENTER)

def close_menu ():
    menuFrame.place_forget()


################################################################### Fonction en jeu ###################################################################

def mouvement_joueur (event, direction):
    global positionJoueur
    if edit == False:
        pad = 0
        verify = False

        if direction == "up":
            posJTestX = 0
            posJTestY = -1
            xyJ = 1
            posJF = -1
            posMax = 0
            deplacement = [0, -nombrePixel]

        elif direction == "down":
            posJTestX = 0
            posJTestY = +1
            xyJ = 1
            posJF = +1
            posMax = nombreCaseY-1
            deplacement = [0, +nombrePixel]

        elif direction == "left":
            posJTestX = -1
            posJTestY = 0
            xyJ = 0
            posJF = -1
            posMax = 0
            deplacement = [-nombrePixel, 0]

        elif direction == "right":
            posJTestX = +1
            posJTestY = 0
            xyJ = 0
            posJF = +1
            posMax = nombreCaseX-1
            deplacement = [+nombrePixel, 0]


        while pad != len(dicoNiveau["listBloc"]):
            if  positionJoueur[0]+posJTestX == dicoNiveau["coordsBloc"][pad*2] and positionJoueur[1]+posJTestY == dicoNiveau["coordsBloc"][pad*2+1]:
                verify = True
            pad += 1

        if verify == False:
            if positionJoueur[xyJ] == posMax:
                level_search(direction)
            else:
                canevas.move(joueur, deplacement[0], deplacement[1])
                positionJoueur[xyJ] = positionJoueur[xyJ]+posJF
        print(positionJoueur)
    pass


################################################################### Fonction en édition ###################################################################

def typeBlocs (tBloc):
    global typeDuBloc
    global couleurBloc
    if tBloc == "solide":
        typeDuBloc = 0
        couleurBloc = 'black'
    elif tBloc == "spawn":
        if id_level == [0,0]:
            typeDuBloc = 1
            couleurBloc = 'blue'
        else:
            print("level [0,0] only")
    elif tBloc == "key":
        typeDuBloc = 2
        couleurBloc = '#6D071A'
    pass

def plassage_de_block (event):
    global dicoNiveau

    xSourisCase,ySourisCase=event.x,event.y

    xSourisCase = (xSourisCase/nombrePixel)
    xSourisCase = int(xSourisCase)

    ySourisCase = (ySourisCase/nombrePixel)
    ySourisCase = int(ySourisCase)

    padsouris = 0
    verify = False
    while padsouris != len(dicoNiveau["listBloc"]):
        if xSourisCase == dicoNiveau["coordsBloc"][padsouris*2] and ySourisCase == dicoNiveau["coordsBloc"][padsouris*2+1]:
            if delonespebloc == True:
                canevas.delete(dicoNiveau["listBloc"][padsouris])
                del dicoNiveau["listBloc"][padsouris]
                del dicoNiveau["coordsBloc"][padsouris*2]
                del dicoNiveau["coordsBloc"][padsouris*2]
                del dicoNiveau["typeBloc"][padsouris]
                del dicoNiveau["color"][padsouris]
                padsouris -= 1
            else:
                verify = True
        padsouris += 1

    if edit == True and verify == False and delonespebloc == False:
        if 1 in dicoNiveau["typeBloc"] and typeDuBloc == 1:
            canevas.delete(dicoNiveau["listBloc"][dicoNiveau["typeBloc"].index(1)])
            del dicoNiveau["listBloc"][dicoNiveau["typeBloc"].index(1)]
            del dicoNiveau["coordsBloc"][dicoNiveau["typeBloc"].index(1)*2]
            del dicoNiveau["coordsBloc"][dicoNiveau["typeBloc"].index(1)*2]
            del dicoNiveau["color"][dicoNiveau["typeBloc"].index(1)]

            del dicoNiveau["typeBloc"][dicoNiveau["typeBloc"].index(1)]
        dicoNiveau["listBloc"].append(canevas.create_rectangle(xSourisCase*nombrePixel,ySourisCase*nombrePixel,xSourisCase*nombrePixel+nombrePixel,ySourisCase*nombrePixel+nombrePixel, fill=couleurBloc))
        dicoNiveau["coordsBloc"].append(xSourisCase)
        dicoNiveau["coordsBloc"].append(ySourisCase)
        dicoNiveau["typeBloc"].append(typeDuBloc)
        dicoNiveau["color"].append(couleurBloc)
        print(dicoNiveau)

def deleteblock (event=0):
    global dicoNiveau
    
    padblocklist = 0
    while padblocklist < len(dicoNiveau["listBloc"]) and edit == True:
        canevas.delete(dicoNiveau["listBloc"][padblocklist])
        padblocklist += 1
    dicoNiveau["listBloc"].clear()
    dicoNiveau["coordsBloc"].clear()
    dicoNiveau["typeBloc"].clear()
    dicoNiveau["color"].clear()

def deleteLastBlock (event=0):
    global dicoNiveau

    if len(dicoNiveau["listBloc"]) > 0 and edit == True:
        canevas.delete(dicoNiveau["listBloc"][-1])
        del dicoNiveau["listBloc"][-1]
        del dicoNiveau["coordsBloc"][-1]
        del dicoNiveau["coordsBloc"][-1]
        del dicoNiveau["typeBloc"][-1]
        del dicoNiveau["color"][-1]

def save_level (event=0):
    if edit == True:
        with open(lienfichier, "wb") as fichierNiveau:
            pickle.dump(dicoNiveau, fichierNiveau)

"""def save_world ():
    if edit == True:
        with open(lienmonde, "wb") as fichierMonde:
            pickle.dump(dicoMonde, fichierMonde)"""

def info_editeur (event=0):
    global fenetreinfosTest

    fenetre_infos = tk.Toplevel()
    fenetre_infos.resizable(False,False)
    fenetre_infos.geometry('1200x600')
    infosLabel = Label(fenetre_infos, image=imageBoutonEditeurInfos)
    infosLabel.pack()
    fenetreinfosTest += 1
    if fenetreinfosTest == 2:
        fenetre_infos.destroy()
        fenetreinfosTest = 1

def delspebloc ():
    global delonespebloc
    if delonespebloc == False:
        delonespebloc = True
    else:
        delonespebloc = False

################################################################### Fonction fonctionnement du programme ###################################################################
def retour_menu (event=0):
    global lienfichier
    global edit
    global ligneX
    global ligneY
    global joueur
    global id_level
    global id_level_editeur
    padblocklist = 0

    if edit == True:
        fenetre_bouton.destroy()
        save_level()
        edit = False
        id_level_editeur = id_level
        while padblocklist < len(ligneX):
            canevas.delete(ligneX[padblocklist])
            padblocklist += 1
        ligneX.clear()
        padblocklist = 0
        while padblocklist < len(ligneY):
            canevas.delete(ligneY[padblocklist])
            padblocklist += 1
        ligneY.clear()
    elif solo == True:
        try:
            canevas.delete(joueur)
            positionJoueur.clear()
        except:
            pass
    lienfichier = "assets/data/menu.txt"
    loadTestZone()
    menuFrame.place(x=largeur/2, y=hauteur/2,anchor=CENTER)

def loadTestZone (event=0):
    global lienfichier
    global dicoNiveau
    global couleurBloc
    global typeDuBloc

    padblocklist = 0
    while padblocklist < len(dicoNiveau["listBloc"]):
        canevas.delete(dicoNiveau["listBloc"][padblocklist])
        padblocklist += 1
    dicoNiveau["listBloc"].clear()
    dicoNiveau["coordsBloc"].clear()
    dicoNiveau["typeBloc"].clear()
    dicoNiveau["color"].clear()

    if os.path.exists(lienfichier):
        with open(lienfichier, "rb") as fichier:
            dicoNiveau = pickle.load(fichier)

    else:
        if edit == True:
            with open(lienfichier, "wb") as fichierNiveau:
                pickle.dump(dicoNiveau, fichierNiveau)
    dicoNiveau["listBloc"].clear()
    rang = 0
    while rang < len(dicoNiveau["typeBloc"]):
        couleurBloc = dicoNiveau["color"][rang]
        dicoNiveau["listBloc"].append(canevas.create_rectangle(dicoNiveau["coordsBloc"][(rang*2)]*nombrePixel, dicoNiveau["coordsBloc"][(rang*2+1)]*nombrePixel, dicoNiveau["coordsBloc"][(rang*2)]*nombrePixel+nombrePixel, dicoNiveau["coordsBloc"][(rang*2+1)]*nombrePixel+nombrePixel, fill=couleurBloc))
        rang += 1
    typeDuBloc = 0
    couleurBloc = 'black'

def level_search (direction):
    global id_level
    global lienfichier
    global numeroNiveau

    if edit == True:
        if direction =='up':
            lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0])+str(id_level[1]-1)+".txt"
            if os.path.exists(lienfichier):
                lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                id_level[1] -= 1 # -1 comme repère en haut gauche
                lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0])+str(id_level[1])+".txt"
                loadTestZone()
                numeroNiveau.config(text=id_level)
            else:
                lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                deleteblock()
                id_level[1] -= 1
                numeroNiveau.config(text=id_level)

        if direction =='down':
            lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0])+str(id_level[1]+1)+".txt"
            if os.path.exists(lienfichier):
                lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                id_level[1] += 1
                lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0])+str(id_level[1])+".txt"
                loadTestZone()
                numeroNiveau.config(text=id_level)
            else:
                lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                deleteblock()
                id_level[1] += 1
                numeroNiveau.config(text=id_level)

        if direction =='left':
            lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0]-1)+str(id_level[1])+".txt"
            if os.path.exists(lienfichier):
                lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                id_level[0] -= 1
                lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0])+str(id_level[1])+".txt"
                loadTestZone()
                numeroNiveau.config(text=id_level)
            else:
                lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                deleteblock()
                id_level[0] -= 1
                numeroNiveau.config(text=id_level)

        if direction =='right':
            lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0]+1)+str(id_level[1])+".txt"
            if os.path.exists(lienfichier):
                lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                id_level[0] += 1
                lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0])+str(id_level[1])+".txt"
                loadTestZone()
                numeroNiveau.config(text=id_level)
            else:
                lienfichier = "assets/data/editeur/level_editeur"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                deleteblock()
                id_level[0] += 1
                numeroNiveau.config(text=id_level)

    else:
        if direction =='up':
            lienfichier = "assets/data/solo/level_editeur"+str(id_level[0])+str(id_level[1]-1)+".txt"
            if os.path.exists(lienfichier):
                id_level[1] -= 1
                loadTestZone()
                positionJoueur[1] = nombreCaseY-1
                canevas.moveto(joueur, positionJoueur[0]*nombrePixel-1, positionJoueur[1]*nombrePixel-1)


        if direction =='down':
            lienfichier = "assets/data/solo/level_editeur"+str(id_level[0])+str(id_level[1]+1)+".txt"
            if os.path.exists(lienfichier):
                id_level[1] += 1
                loadTestZone()
                positionJoueur[1] = 0
                canevas.moveto(joueur, positionJoueur[0]*nombrePixel-1, -positionJoueur[1]*nombrePixel-1)



        if direction =='left':
            lienfichier = "assets/data/solo/level_editeur"+str(id_level[0]-1)+str(id_level[1])+".txt"
            if os.path.exists(lienfichier):
                id_level[0] -= 1
                loadTestZone()
                positionJoueur[0] = nombreCaseX-1
                canevas.moveto(joueur, positionJoueur[0]*nombrePixel-1, positionJoueur[1]*nombrePixel-1)



        if direction =='right':
            lienfichier = "assets/data/solo/level_editeur"+str(id_level[0]+1)+str(id_level[1])+".txt"
            if os.path.exists(lienfichier):
                id_level[0] += 1
                loadTestZone()
                positionJoueur[0] = 0
                canevas.moveto(joueur, -positionJoueur[0]*nombrePixel-1, positionJoueur[1]*nombrePixel-1)


################################################################### Mise en place de la fenetre ###################################################################

fenetre = Tk()

largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()

fenetre.title("Game & Cube")
#fenetre.geometry("%dx%d%+d%+d" % (largeur,hauteur,x_fenetre,y_fenetre))
fenetre.attributes('-fullscreen', True)
canevas = Canvas(fenetre, width=largeur, height=hauteur,bg='grey')


################################################################### Les Binds ###################################################################

fenetre.bind("<Key-z>", lambda event : mouvement_joueur (event,"up"))
fenetre.bind("<Key-s>", lambda event : mouvement_joueur (event,"down"))
fenetre.bind("<Key-q>", lambda event : mouvement_joueur (event,"left"))
fenetre.bind("<Key-d>", lambda event : mouvement_joueur (event,"right"))

fenetre.bind("<Key-Z>", lambda event : mouvement_joueur (event,"up"))
fenetre.bind("<Key-S>", lambda event : mouvement_joueur (event,"down"))
fenetre.bind("<Key-Q>", lambda event : mouvement_joueur (event,"left"))
fenetre.bind("<Key-D>", lambda event : mouvement_joueur (event,"right"))

fenetre.bind("<Key-Up>", lambda event : mouvement_joueur (event,"up"))
fenetre.bind("<Key-Down>", lambda event : mouvement_joueur (event,"down"))
fenetre.bind("<Key-Left>", lambda event : mouvement_joueur (event,"left"))
fenetre.bind("<Key-Right>", lambda event :mouvement_joueur (event,"right"))

fenetre.bind("<B1-Motion>", lambda event : plassage_de_block(event))
fenetre.bind("<Button-1>", lambda event : plassage_de_block(event))

fenetre.bind("<Escape>", lambda event : retour_menu(event))

fenetre.bind("<Button-2>", lambda event : deleteLastBlock(event))
fenetre.bind("<MouseWheel>", lambda event : deleteLastBlock(event))

fenetre.bind("<Key-t>", lambda event : loadTestZone(event))
fenetre.bind("<Key-g>", lambda event : save_level(event))

first_launch()

#Autre

canevas.pack()
fenetre.mainloop()