#Import des bibliothèques

from tkinter import *
import tkinter as tk, tkinter.messagebox
import pickle, os, shutil
try:
    import vlc
except ImportError:
    os.system('pip install python-vlc')
import vlc


################################################################### Les fonctions de mise en place des modes ###################################################################

def first_launch (): #La fonction "first_launch" permet de déclaré la plus part des variable global
    global editBloc, cwd, musicDeFond, originalPath, imageMonde1, imageMonde2, imageMonde3, imageResetSolo, imageBoutonEditeurItemCle, imageBoutonEditeurEditBloc, newColorBloc, freezeEdit, fenetreeditTest, listeNiveau, id_level, lienfichier, edit, nombrePixel, nombreCaseX, nombreCaseY, imageBoutonSolo, imageBoutonEditeur, ligneX, ligneY, imageBoutonEditeurNiveauHaut, imageBoutonEditeurNiveauBas, imageBoutonEditeurNiveauGauche, imageBoutonEditeurNiveauDroite, imageBoutonEditeurSave, imageBoutonEditeurRetour, imageWIP, imageBoutonEditeurPoubelle, imageBoutonEditeurExit, imageEditeurInfos, fenetreinfosTest, imageBoutonEditeurBlocSolide, couleurBloc, typeDuBloc, imageBoutonEditeurBlocSpawn, delonespebloc, listeMonde, id_monde, solo, lienmonde, imageBoutonEditeurInfos

    cwd = os.getcwd()
    cwd = cwd.replace("\\", "/" )
    cwd = cwd+str("/")
    #Les coordonnées virtuel sont des coordonnées d'une matrice créée en fonction du nombre de cases à l'écran (défini avec "nombreCase")
    listeNiveau = [] # Default : [{"coordsBloc" : [], "idBloc" : 0, "typeBloc" : 0, "color" : ""}] Cette liste contient toutes les informations sur les blocs d'un niveau
    listeMonde = [] # Default : [{"idKeyPorte" : 0, "coordsBloc" : [], "idLevel" : "", "keyCollect" : 0}] Cette liste contient toutes les spécificités des bloc des niveau du monde
    id_level = [0,0] #Numéro du niveau dans le quel on est (quand on change de niveau on ajoute ou retire 1 ) [default : [0,0]]
    id_monde = 1 #Numéro du monde dans le quel on est
    lienfichier = str(cwd)+"assets/data/menu.txt" #Lien a utiliser pour charger ou sauvegarder un niveau [default : "assets/data/menu.txt"]
    lienmonde = str(cwd)+"assets/data/editeur/monde"+str(id_monde)+"_info.txt"
    originalPath = str(cwd)+"assets/data/origine"
    edit = False #Permet de vérifier si le mode d'édition est activer [default : False]
    nombreCase = 48 #En largeur (default = 48)
    nombrePixel = largeur/nombreCase #nombrePixel = nombre de pixels par case sur l'écran (en fonction de la résolution de l'écran, le nombre de pixel change pour toujours avoir le même nombre de case à l'écran)
    nombreCaseX = largeur/nombrePixel #Le nombre de case en X permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en X
    nombreCaseY = hauteur/nombrePixel #Le nombre de case en Y permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en Y
    ligneX = [] #Liste des ID des lignes X crées
    ligneY = [] #Liste des ID des lignes X crées
    fenetreinfosTest = False #Permet de vérifier si la fenetre d'info de l'éditeur est déjà créer
    fenetreeditTest = False #Permet de vérifier si la fenetre d'edition de bloc de l'éditeur est déjà créer
    couleurBloc = 'black' #Défini la couleur d'un bloc
    newColorBloc = 'red' #Défini la nouvelle couleur du bloc
    typeDuBloc = 0 #Défini quel est le type de bloc (0 = solide, 1 = spawn, 2 = clé, 3 = porte)
    delonespebloc = False #Permet de vérifier si la gomme de l'éditeur est déjà créer
    solo = False #Permet de lancer le solo
    freezeEdit = False #Permet de mettre en pose les fonctions de l'éditeur
    editBloc = False #Permet de vérifier si la l'édition de bloc de l'éditeur est déjà créer
    imageBoutonSolo = PhotoImage(file = str(cwd)+"assets/images/bouton_solo.png") #Image du bouton du solo sur le menu principal
    imageBoutonEditeur = PhotoImage(file = str(cwd)+"assets/images/bouton_editeur.png") #Image du bouton de l'éditeur sur le menu principal
    imageBoutonEditeurNiveauHaut = PhotoImage(file = str(cwd)+"assets/images/fleche_haut.png")
    imageBoutonEditeurNiveauBas = PhotoImage(file = str(cwd)+"assets/images/fleche_bas.png")
    imageBoutonEditeurNiveauGauche = PhotoImage(file = str(cwd)+"assets/images/fleche_gauche.png")
    imageBoutonEditeurNiveauDroite = PhotoImage(file = str(cwd)+"assets/images/fleche_droite.png")
    imageBoutonEditeurSave = PhotoImage(file = str(cwd)+"assets/images/save.png")
    imageBoutonEditeurRetour = PhotoImage(file = str(cwd)+"assets/images/retour.png")
    imageWIP = PhotoImage(file = str(cwd)+"assets/images/WIP.png")
    imageBoutonEditeurPoubelle = PhotoImage(file = str(cwd)+"assets/images/poubelle.png")
    imageBoutonEditeurExit = PhotoImage(file = str(cwd)+"assets/images/exit.png")
    imageEditeurInfos = PhotoImage(file = str(cwd)+"assets/images/Menu_infos.png")
    imageBoutonEditeurBlocSolide = PhotoImage(file = str(cwd)+"assets/images/bouton_bloc_solide.png")
    imageBoutonEditeurBlocSpawn = PhotoImage(file= str(cwd)+"assets/images/bouton_bloc_spawn.png")
    imageBoutonEditeurItemCle = PhotoImage(file= str(cwd)+"assets/images/bouton_item_cle.png")
    imageBoutonEditeurInfos = PhotoImage(file= str(cwd)+"assets/images/help.png")
    imageBoutonEditeurEditBloc = PhotoImage(file= str(cwd)+"assets/images/edit_bloc.png")
    imageResetSolo = PhotoImage(file=str(cwd)+"assets/images/Reset.png")
    imageMonde1 = PhotoImage(file=str(cwd)+"assets/images/M1.png")
    imageMonde2 = PhotoImage(file=str(cwd)+"assets/images/M2.png")
    imageMonde3 = PhotoImage(file=str(cwd)+"assets/images/M3.png")
    musicDeFond = vlc.MediaPlayer(str(cwd)+"assets/musica/Gymnopédie No°1.wav")
    init_keys(fenetre)
    menu()
    #bg_music()

def lancement_edition (): #La fonction "lancement_edition" permet de mettre en place tout le système de la création de niveau
    global edit, lienfichier, ligneX, fenetre_bouton, id_level, numeroNiveau
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
    id_level = [0,0]
    lienfichier = str(cwd)+"assets/data/solo/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
    load_level() #Appel de la fonction qui charge les niveau
    load_world()
    #Fenetre des infos / boutons
    fenetre_bouton = tk.Toplevel() #Création de la fenetre des fonction/boutons de l'éditeur
    fenetre_bouton.geometry('312x641') #taille 1 bouton = taille que tu veux + 3
    fenetre_bouton.resizable(False,False) #Fenetre non redimentionable
    fenetre_bouton.attributes('-topmost',1)
    fenetre_bouton.protocol("WM_DELETE_WINDOW", disable_event)

    bouton_save = Button(fenetre_bouton, image=imageBoutonEditeurSave, bg='white', command=save_level)
    bouton_save.place(x=0,y=0)

    bouton_retour = Button(fenetre_bouton, image=imageBoutonEditeurRetour, bg='white', command=deleteLastBlock)
    bouton_retour.place(x=103,y=0)

    boutonEditeurPoubelle = Button(fenetre_bouton, image=imageBoutonEditeurPoubelle, bg='white', command=deleteblock)
    boutonEditeurPoubelle.place(x=206,y=0)

    bouton_niveau_up = Button(fenetre_bouton, image=imageBoutonEditeurNiveauHaut, bg='white', command=lambda:level_search("up"))
    bouton_niveau_up.place(x=103,y=103)

    bouton_niveau_down = Button(fenetre_bouton, image=imageBoutonEditeurNiveauBas, bg='black', command=lambda:level_search("down"))
    bouton_niveau_down.place(x=103,y=309)
    
    bouton_niveau_left = Button(fenetre_bouton, image=imageBoutonEditeurNiveauGauche, bg='white', command=lambda:level_search("left"))
    bouton_niveau_left.place(x=0,y=206)

    bouton_niveau_right = Button(fenetre_bouton, image=imageBoutonEditeurNiveauDroite, bg='white', command=lambda:level_search("right"))
    bouton_niveau_right.place(x=206,y=206)

    boutonEditeurInfo = Button(fenetre_bouton, image=imageBoutonEditeurInfos, bg='white', command=info_editeur)
    boutonEditeurInfo.place(x=103,y=412)

    boutonEditeurExit = Button(fenetre_bouton, image=imageBoutonEditeurExit, bg='white', command=lambda:retour_menu("postEditMenu"))
    boutonEditeurExit.place(x=206,y=515)

    numeroNiveau = Label(fenetre_bouton, text=id_level, font="Arial, 30")
    numeroNiveau.pack(padx=103, pady=230)

    bouton_bloc_solide = Button(fenetre_bouton, image=imageBoutonEditeurBlocSolide, bg='white', command=lambda:typeBlocs("solide"))
    bouton_bloc_solide.place(x=0,y=103)

    bouton_bloc_spawn = Button(fenetre_bouton, image=imageBoutonEditeurBlocSpawn, bg='white', command=lambda:typeBlocs("spawn"))
    bouton_bloc_spawn.place(x=206,y=103)

    bouton_item_key = Button(fenetre_bouton, image=imageBoutonEditeurItemCle, bg='white', command=lambda:typeBlocs("key"))
    bouton_item_key.place(x=0,y=309)

    bouton_gomme = Button(fenetre_bouton, image=imageWIP, bg='white', command=delspebloc)
    bouton_gomme.place(x=0,y=412)

    bouton_bloc_port = Button(fenetre_bouton, image=imageWIP, command=lambda:typeBlocs("porte"))
    bouton_bloc_port.place(x=206,y=309)

    bouton_edit = Button(fenetre_bouton, image=imageBoutonEditeurEditBloc, bg='white', command=set_edit_objet)
    bouton_edit.place(x=206,y=412)

def lancement_solo ():
    global joueur, positionJoueur, lienfichier, id_level, solo

    solo = True
    id_level = [0,0]
    lienfichier = str(cwd)+"assets/data/solo/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
    load_level()
    load_world()
    for pasdubloc in listeNiveau:
        if pasdubloc["typeBloc"] == 1:
            posjxstart = pasdubloc["coordsBloc"][0]
            posjystart = pasdubloc["coordsBloc"][1]
            break
    joueur = canevas.create_rectangle(0, 0, nombrePixel, nombrePixel, fill='blue')
    canevas.move(joueur,posjxstart*nombrePixel, posjystart*nombrePixel)
    positionJoueur = [posjxstart, posjystart] #0 = x & 1 = y
    close_menu()

def menu ():
    global menuFrame
    load_level()

    menuFrame = Frame(fenetre, width=largeur/2+largeur/4, height=hauteur/2+hauteur/4 ,bg='black')
    menuFrame.place(x=largeur/2, y=hauteur/2,anchor=CENTER)

    boutonSolo = Button(menuFrame, image=imageBoutonSolo, command=menu_post_solo)
    boutonSolo.place(x=(largeur/2+largeur/4)/2-((largeur/2+largeur/4)/2)/2, y=(hauteur/2+hauteur/4)/2, anchor=CENTER)

    boutonEditeur = Button(menuFrame, image=imageBoutonEditeur, command=menu_post_edition)
    boutonEditeur.place(x=(largeur/2+largeur/4)/2+((largeur/2+largeur/4)/2)/2, y=(hauteur/2+hauteur/4)/2, anchor=CENTER)

    boutonExit = Button(menuFrame, image=imageBoutonEditeurExit, command=fenetre.destroy)
    boutonExit.place(x=(largeur/2+largeur/4)/2, y=(hauteur/2+hauteur/4)/2, anchor=CENTER)

def menu_post_edition ():
    global menuPostEdit

    menuPostEdit = Frame(fenetre, width=largeur/2+largeur/4, height=hauteur/2+hauteur/4 ,bg='black')
    menuPostEdit.place(x=largeur/2, y=hauteur/2,anchor=CENTER)

    boutonExitEdit = Button(menuPostEdit, image=imageBoutonEditeurExit, command=lambda:retour_menu("Menu"))
    boutonExitEdit.place(x=(largeur/2+largeur/4)/2, y=(hauteur/2+hauteur/4)/2, anchor=CENTER)

    boutonEditeurMonde1 = Button(menuPostEdit, image=imageMonde1, command=lambda:monde_finder_editeur(1))
    boutonEditeurMonde1.place(x=(largeur/2+largeur/4)/2-((largeur/2+largeur/4)/2)/4, y=(hauteur/2+hauteur/4)/2, anchor=CENTER)

    boutonEditeurMonde2 = Button(menuPostEdit, image=imageMonde2, command=lambda:monde_finder_editeur(2))
    boutonEditeurMonde2.place(x=(largeur/2+largeur/4)/2, y=(hauteur/2+hauteur/4)/1.37, anchor=CENTER)

    boutonEditeurMonde3 = Button(menuPostEdit, image=imageMonde3, command=lambda:monde_finder_editeur(3))
    boutonEditeurMonde3.place(x=(largeur/2+largeur/4)/2+((largeur/2+largeur/4)/2)/4, y=(hauteur/2+hauteur/4)/2, anchor=CENTER)

    titreMonde = Label(menuPostEdit, text="Select World", font="Arial, 48", fg='white', bg='black')
    titreMonde.place(x=(largeur/2+largeur/4)/2, y=50, anchor=CENTER)

def monde_finder_editeur (numMonde):
    global id_monde, lienmonde, lienfichier

    id_monde = numMonde
    lienmonde = str(cwd)+"assets/data/editeur/monde"+str(id_monde)+"_info.txt"
    lienfichier = str(cwd)+"assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
    lancement_edition()

def menu_post_solo ():
    global menuPostSolo

    menuPostSolo = Frame(fenetre, width=largeur/2+largeur/4, height=hauteur/2+hauteur/4 ,bg='black')
    menuPostSolo.place(x=largeur/2, y=hauteur/2,anchor=CENTER)

    boutonExitSolo = Button(menuPostSolo, image=imageBoutonEditeurExit, command=lambda:retour_menu("Menu"))
    boutonExitSolo.place(x=(largeur/2+largeur/4)/2, y=(hauteur/2+hauteur/4)/2, anchor=CENTER)

    boutonSoloMonde1 = Button(menuPostSolo, image=imageMonde1, command=lambda:monde_finder_solo(1))
    boutonSoloMonde1.place(x=(largeur/2+largeur/4)/2-((largeur/2+largeur/4)/2)/4, y=(hauteur/2+hauteur/4)/2, anchor=CENTER)

    boutonSoloMonde2 = Button(menuPostSolo, image=imageMonde2, command=lambda:monde_finder_solo(2))
    boutonSoloMonde2.place(x=(largeur/2+largeur/4)/2, y=(hauteur/2+hauteur/4)/1.37, anchor=CENTER)

    boutonSoloMonde3 = Button(menuPostSolo, image=imageMonde3, command=lambda:monde_finder_solo(3))
    boutonSoloMonde3.place(x=(largeur/2+largeur/4)/2+((largeur/2+largeur/4)/2)/4, y=(hauteur/2+hauteur/4)/2, anchor=CENTER)

    boutonSoloReset = Button(menuPostSolo, image=imageResetSolo, command=reset_solo)
    boutonSoloReset.place(x=(largeur/2+largeur/4)/2, y=(hauteur/2+hauteur/4)-(hauteur/2+hauteur/4)/1.37, anchor=CENTER)

    titreSolo = Label(menuPostSolo, text="WIP", font="Arial, 48", fg='white', bg='black')
    titreSolo.place(x=(largeur/2+largeur/4)/2, y=50, anchor=CENTER)

def monde_finder_solo (numMonde):
    global id_monde, lienmonde, lienfichier

    id_monde = numMonde
    lienmonde = str(cwd)+"assets/data/solo/monde"+str(id_monde)+"_info.txt"
    lienfichier = str(cwd)+"assets/data/solo/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
    lancement_solo()

def close_menu ():
    try:
        menuFrame.place_forget()
    except:
        pass
    try:
        menuPostEdit.place_forget()
    except:
        pass
    try:
            menuPostSolo.place_forget()
    except:
        pass

def bg_music ():
    musicDeFond.play()


################################################################### Fonction du joueur ###################################################################

def mouvement_joueur (event, direction):
    global positionJoueur, listeMonde

    if solo == True:
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
        #Collision bloc
        while pad != len(listeNiveau):
            if  positionJoueur[0]+posJTestX == listeNiveau[pad]["coordsBloc"][0] and positionJoueur[1]+posJTestY == listeNiveau[pad]["coordsBloc"][1]:
                #Collision avec bloc solide
                if listeNiveau[pad]["typeBloc"] == 0:
                    verify = True

                #Collision avec bloc spawn
                elif listeNiveau[pad]["typeBloc"] == 1:
                    verify = False

                #Collision avec clé
                elif listeNiveau[pad]["typeBloc"] == 2:
                    verify = False

                    for blocinListeMonde in listeMonde:
                        if positionJoueur[0]+posJTestX == blocinListeMonde["coordsBloc"][0] and positionJoueur[1]+posJTestY == blocinListeMonde["coordsBloc"][1] and blocinListeMonde["idLevel"] == str(id_level) and blocinListeMonde["keyCollect"] == 0: #Permet de savoir si le bloc exite déjà dans la liste
                                touch_key(pad,blocinListeMonde)
                                pad -= 1

                #Collision avec bloc porte
                elif listeNiveau[pad]["typeBloc"] == 3:
                    verify = True
                    for blocinListeMonde in listeMonde:
                        if positionJoueur[0]+posJTestX == blocinListeMonde["coordsBloc"][0] and positionJoueur[1]+posJTestY == blocinListeMonde["coordsBloc"][1] and blocinListeMonde["idLevel"] == str(id_level) and blocinListeMonde["keyCollect"] == 1: #Permet de savoir si le bloc exite déjà dans la liste
                                touch_porte(pad,blocinListeMonde)
                                pad -= 1

            pad += 1

        if verify == False:
            #Collision limite map 
            if positionJoueur[xyJ] == posMax:
                level_search(direction)
            #Mouvement
            else:
                canevas.move(joueur, deplacement[0], deplacement[1])
                positionJoueur[xyJ] = positionJoueur[xyJ]+posJF

def touch_key (pad,blocinListeMonde):
    for blocinListeMonde2 in listeMonde:
        if blocinListeMonde2["idKeyPorte"] == blocinListeMonde["idKeyPorte"]:
            blocinListeMonde2["keyCollect"] = 1
    canevas.delete(listeNiveau[pad]["idBloc"])
    del listeNiveau[pad]
    save_level()
    save_world()

def touch_porte(pad,blocinListeMonde):
    for blocinListeMonde2 in listeMonde:
        if blocinListeMonde2["idKeyPorte"] == blocinListeMonde["idKeyPorte"]:
            del blocinListeMonde2
            break
    canevas.delete(listeNiveau[pad]["idBloc"])
    del listeNiveau[pad]
    save_level()
    save_world()


################################################################### Fonction du mode édition ###################################################################

def typeBlocs (tBloc): #Indication du type de bloc à placer
    global typeDuBloc, couleurBloc
    if tBloc == "solide":
        typeDuBloc = 0
        couleurBloc = 'black'

    elif tBloc == "spawn":
        if id_level == [0,0]:
            typeDuBloc = 1
            couleurBloc = 'cyan'
        else:
            print("level [0,0] only")

    elif tBloc == "key":
        typeDuBloc = 2
        couleurBloc = 'orange'

    elif tBloc == "porte":
        typeDuBloc = 3
        couleurBloc = 'orange'

def clic_gauche (event): #Utilisation du clic gauche (placer un bloc, détruire, selectionner...)
    global listeNiveau, entryIDcle, boutonIDCleValidation, selectBlocID, couleurSet, textIDKey, padsouris, selectBlocCoordX, selectBlocCoordY

    xSourisCase,ySourisCase=event.x,event.y

    xSourisCase = (xSourisCase/nombrePixel)
    xSourisCase = int(xSourisCase)

    ySourisCase = (ySourisCase/nombrePixel)
    ySourisCase = int(ySourisCase)

    if edit == True: #Mode Edition
        padsouris = 0
        verify = False
        while padsouris != len(listeNiveau):
            if xSourisCase == listeNiveau[padsouris]["coordsBloc"][0] and ySourisCase == listeNiveau[padsouris]["coordsBloc"][1]:

                if delonespebloc == True: #La gomme
                    canevas.delete(listeNiveau[padsouris]["idBloc"])
                    del listeNiveau[padsouris]
                    padsouris -= 1

                else:
                    verify = True

            padsouris += 1

        if verify == False and delonespebloc == False:
            padsouris = 0
            while padsouris != len(listeNiveau):
                if listeNiveau[padsouris]["typeBloc"] == 1 and typeDuBloc == 1: #Vérification de si le bloc d'apparition existe déjà
                    canevas.delete(listeNiveau[padsouris]["idBloc"])
                    del listeNiveau[padsouris]
                    padsouris -= 1
                padsouris += 1
            listeNiveau.append({"coordsBloc" : [xSourisCase, ySourisCase], "idBloc" : canevas.create_rectangle(xSourisCase*nombrePixel, ySourisCase*nombrePixel, xSourisCase*nombrePixel+nombrePixel, ySourisCase*nombrePixel+nombrePixel, fill=couleurBloc), "typeBloc" : typeDuBloc, "color" : str(couleurBloc)})

    elif editBloc == True:
        try:
            entryIDcle.destroy()
        except:
            pass
        try:
            boutonIDCleValidation.destroy()
        except:
            pass
        try:
            couleurSet.destroy()
        except:
            pass
        try:
            textIDKey.destroy()
        except:
            pass
        verifyEdit = False
        for blocinListeNiveau in listeNiveau:
            if xSourisCase == blocinListeNiveau["coordsBloc"][0] and ySourisCase == blocinListeNiveau["coordsBloc"][1]:

                if blocinListeNiveau["typeBloc"] == 0:
                    textTypeBlocSelect.config(text="Bloc Solide")
                    selectBlocID = blocinListeNiveau["idBloc"]
                    verifyEdit = False

                elif blocinListeNiveau["typeBloc"] == 1:
                    textTypeBlocSelect.config(text="Bloc Spawn")
                    selectBlocID = blocinListeNiveau["idBloc"]
                    verifyEdit = False

                elif blocinListeNiveau["typeBloc"] == 2:
                    textTypeBlocSelect.config(text="Item Clé ")
                    selectBlocID = blocinListeNiveau["idBloc"]
                    verifyEdit = True

                elif blocinListeNiveau["typeBloc"] == 3:
                    textTypeBlocSelect.config(text="Bloc Porte")
                    selectBlocID = blocinListeNiveau["idBloc"]
                    verifyEdit = True

                if verifyEdit == True:
                    selectBlocCoordX = blocinListeNiveau["coordsBloc"][0]
                    selectBlocCoordY = blocinListeNiveau["coordsBloc"][1]

                    entryIDcle = Entry(fenetre_edit_bloc, bg="lightgrey", width=10, font="Arial, 24")
                    entryIDcle.place(x=250, y=150)

                    boutonIDCleValidation = Button(fenetre_edit_bloc, image=imageWIP, command=lambda:getKeyID(entryIDcle.get()))
                    boutonIDCleValidation.place(x=25,y=150)

                    textIDKey = Label(fenetre_edit_bloc, text="ID :", font="Arial, 24")
                    textIDKey.place(x=175,y=150) 

                    couleurSet = Scale(fenetre_edit_bloc, orient='horizontal', from_=1, to=5, resolution=1, tickinterval=2, length=180, label='Couleur', font=("Arial, 10"), command=change_color)
                    couleurSet.place(x=250,y=200)
                break
            else:
                textTypeBlocSelect.config(text="Air")

def deleteblock (event=0): #Destruction total du niveau
    global listeNiveau
    for blocinListeNiveau in listeNiveau and edit == True:
        canevas.delete(blocinListeNiveau["idBloc"])
    listeNiveau.clear()
    listeMonde.clear()

def deleteLastBlock (event=0): #Destruction du dernier bloc placé
    global listeNiveau
    if len(listeNiveau) > 0 and edit == True:
        canevas.delete(listeNiveau[-1]["idBloc"])
        if listeNiveau[-1]["typeBloc"] == 2:
            for blocinListeMonde in listeMonde:
                if blocinListeMonde["coordsBloc"] == listeNiveau[-1]["coordsBloc"]:
                    del blocinListeMonde
                    break
        del listeNiveau[-1]

def save_level (): #Sauvegarde du niveau
    with open(lienfichier, "wb") as fichierNiveau:
        pickle.dump(listeNiveau, fichierNiveau)

def save_world (): #Sauvegarde du monde
    with open(lienmonde, "wb") as fichierMonde:
        pickle.dump(listeMonde, fichierMonde)

def load_world (): #Chargement du monde
    global listeMonde
    listeMonde.clear()
    if os.path.exists(lienmonde):
        with open(lienmonde, "rb") as fichierMonde:
            listeMonde = pickle.load(fichierMonde)

def info_editeur (event=0): #Fenêtre d'infos des action possible
    global fenetreinfosTest, fenetre_infos
    if fenetreinfosTest == False:
        fenetre_infos = tk.Toplevel()
        fenetre_infos.resizable(False,False)
        fenetre_infos.geometry('1200x600')
        fenetre_infos.attributes('-topmost',1)
        infosLabel = Label(fenetre_infos, image=imageEditeurInfos)
        infosLabel.pack()
        fenetreinfosTest = True
    elif fenetreinfosTest == True:
        fenetre_infos.destroy()
        fenetreinfosTest = False

def delspebloc (): #Toggle de la destruciton d'un bloc spécifique (utilise clic_gauche pour delete)
    global delonespebloc
    if delonespebloc == False:
        delonespebloc = True
    else:
        delonespebloc = False

def set_edit_objet (): #Mise en place du mode d'édition de bloc
    global edit, fenetreeditTest, fenetre_edit_bloc, editBloc, textTypeBlocSelect
    if fenetreeditTest == False:
        fenetre_edit_bloc = tk.Toplevel()
        fenetre_edit_bloc.resizable(False,False)
        fenetre_edit_bloc.geometry('500x300')
        fenetre_edit_bloc.attributes('-topmost',1)
        fenetre_edit_bloc.protocol("WM_DELETE_WINDOW", disable_event)

        titreEdit = Label(fenetre_edit_bloc, text="Edit Object", font="Arial, 32")
        titreEdit.place(x=250,y=20, anchor=CENTER)

        textTypeBloc = Label(fenetre_edit_bloc, text="Type Bloc : ", font="Arial, 24")
        textTypeBloc.place(x=25, y=75)

        textTypeBlocSelect = Label(fenetre_edit_bloc, text="None", font="Arial, 24")
        textTypeBlocSelect.place(x=250, y=75)

        fenetreeditTest = True
        edit = False
        editBloc = True
    elif fenetreeditTest == True:
        fenetre_edit_bloc.destroy()
        fenetreeditTest = False
        edit = True
        editBloc = False

def getKeyID (IDValue): #Enregistre les infos d'une clé
    global listeMonde
    verify = False
    if IDValue == "":
        IDValue = '0'
    for blocinListeMonde in listeMonde:
        if selectBlocCoordX == blocinListeMonde["coordsBloc"][0] and selectBlocCoordY == blocinListeMonde["coordsBloc"][1] and blocinListeMonde["idLevel"] == str(id_level): #Permet de savoir si le bloc exite déjà dans la liste
                blocinListeMonde["idKeyPorte"] = IDValue
                verify = True
                break
    if verify == False:
        listeMonde.append({"idKeyPorte" : IDValue, "coordsBloc" : [selectBlocCoordX, selectBlocCoordY], "idLevel" : str(id_level), "keyCollect" : 0})
    save_world()

def change_color (c): #Change la couleur du bloc selectionner
    global listeNiveau, newColorBloc
    if couleurSet.get() == 1:
        newColorBloc = 'orange'
    elif couleurSet.get() == 2:
        newColorBloc = 'yellow'
    elif couleurSet.get() == 3:
        newColorBloc = 'green'
    elif couleurSet.get() == 4:
        newColorBloc = 'lightgreen'
    elif couleurSet.get() == 5:
        newColorBloc = 'purple'

    canevas.itemconfig(selectBlocID, fill=newColorBloc)
    for blocinListeNiveau in listeNiveau:
        if blocinListeNiveau["idBloc"] == selectBlocID:
            blocinListeNiveau["color"] = newColorBloc
            break


################################################################### Fonction fonctionnement du programme ###################################################################

def disable_event(): #Disable
   pass

def exit_key (event): #Permet des retour au menu avec la touche "echap"
    if edit == True:
        retour_menu("postEditMenu")
    elif solo == True:
        save_level()
        save_world()
        retour_menu("postSoloMenu")
    else:
        retour_menu("Menu")

def retour_menu (goToMenu): #Retour au menu
    global lienfichier, solo, fenetreinfosTest, fenetreeditTest, edit, ligneX, ligneY, joueur, id_level

    if goToMenu == "postEditMenu":
        fenetre_bouton.destroy()
        try:
            fenetre_edit_bloc.destroy()
            fenetreeditTest = 0
        except:
            pass
        save_level()
        save_world()
        edit = False
        for paddeLigne in ligneX:
            canevas.delete(paddeLigne)
        ligneX.clear()
        for paddeLigne in ligneY:
            canevas.delete(paddeLigne)
        ligneY.clear()
        try:
            fenetre_infos.destroy()
            fenetreinfosTest = 0
        except:
            pass
        menuPostEdit.place(x=largeur/2, y=hauteur/2,anchor=CENTER)

    elif goToMenu == "postSoloMenu":
        try:
            canevas.delete(joueur)
            positionJoueur.clear()
        except:
            pass
        solo = False
        menuPostSolo.place(x=largeur/2, y=hauteur/2,anchor=CENTER)

    elif goToMenu == "Menu":
        try:
            menuPostEdit.place_forget()
        except:
            pass
        try:
            menuPostSolo.place_forget()
        except:
            pass
        menuFrame.place(x=largeur/2, y=hauteur/2,anchor=CENTER)
    lienfichier = "assets/data/menu.txt"
    load_level()

def load_level (event=0): #Charge les niveau et détruit les ancien
    global lienfichier, listeNiveau, couleurBloc, typeDuBloc
    for blocinListeNiveau in listeNiveau:
        canevas.delete(blocinListeNiveau["idBloc"])
    listeNiveau.clear()

    if os.path.exists(lienfichier):
        with open(lienfichier, "rb") as fichier:
            listeNiveau = pickle.load(fichier)

    else:
        if edit == True:
            with open(lienfichier, "wb") as fichierNiveau:
                pickle.dump(listeNiveau, fichierNiveau)

    for blocinListeNiveau in listeNiveau:
        del blocinListeNiveau["idBloc"]

    for blocinListeNiveau in listeNiveau:
        couleurBloc = blocinListeNiveau["color"]
        blocinListeNiveau["idBloc"] = (canevas.create_rectangle(blocinListeNiveau["coordsBloc"][0]*nombrePixel, blocinListeNiveau["coordsBloc"][1]*nombrePixel, blocinListeNiveau["coordsBloc"][0]*nombrePixel+nombrePixel, blocinListeNiveau["coordsBloc"][1]*nombrePixel+nombrePixel, fill=couleurBloc))
    typeDuBloc = 0
    couleurBloc = 'black'

def level_search (direction): #Cherche le bon niveau a charger
    global id_level, lienfichier, numeroNiveau
    if solo == True:
        if direction =='up':
            lienfichier = str(cwd)+"assets/data/solo/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1]-1)+".txt"
            if os.path.exists(lienfichier):
                id_level[1] -= 1
                load_level()
                positionJoueur[1] = nombreCaseY-1
                canevas.moveto(joueur, positionJoueur[0]*nombrePixel-1, positionJoueur[1]*nombrePixel-1)

        if direction =='down':
            lienfichier = str(cwd)+"assets/data/solo/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1]+1)+".txt"
            if os.path.exists(lienfichier):
                id_level[1] += 1
                load_level()
                positionJoueur[1] = 0
                canevas.moveto(joueur, positionJoueur[0]*nombrePixel-1, -positionJoueur[1]*nombrePixel-1)

        if direction =='left':
            lienfichier = str(cwd)+"assets/data/solo/monde"+str(id_monde)+"/niveau"+str(id_level[0]-1)+str(id_level[1])+".txt"
            if os.path.exists(lienfichier):
                id_level[0] -= 1
                load_level()
                positionJoueur[0] = nombreCaseX-1
                canevas.moveto(joueur, positionJoueur[0]*nombrePixel-1, positionJoueur[1]*nombrePixel-1)

        if direction =='right':
            lienfichier = str(cwd)+"assets/data/solo/monde"+str(id_monde)+"/niveau"+str(id_level[0]+1)+str(id_level[1])+".txt"
            if os.path.exists(lienfichier):
                id_level[0] += 1
                load_level()
                positionJoueur[0] = 0
                canevas.moveto(joueur, -positionJoueur[0]*nombrePixel-1, positionJoueur[1]*nombrePixel-1)
    else:
        if direction =='up':
            lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1]-1)+".txt"
            if os.path.exists(lienfichier):
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                id_level[1] -= 1 # -1 comme repère en haut gauche
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                load_level()
                numeroNiveau.config(text=id_level)
            else:
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                deleteblock()
                id_level[1] -= 1
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                numeroNiveau.config(text=id_level)

        if direction =='down':
            lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1]+1)+".txt"
            if os.path.exists(lienfichier):
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                id_level[1] += 1
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                load_level()
                numeroNiveau.config(text=id_level)
            else:
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                deleteblock()
                id_level[1] += 1
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                numeroNiveau.config(text=id_level)

        if direction =='left':
            lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0]-1)+str(id_level[1])+".txt"
            if os.path.exists(lienfichier):
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                id_level[0] -= 1
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                load_level()
                numeroNiveau.config(text=id_level)
            else:
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                deleteblock()
                id_level[0] -= 1
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                numeroNiveau.config(text=id_level)

        if direction =='right':
            lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0]+1)+str(id_level[1])+".txt"
            if os.path.exists(lienfichier):
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                id_level[0] += 1
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                load_level()
                numeroNiveau.config(text=id_level)
            else:
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                save_level()
                deleteblock()
                id_level[0] += 1
                lienfichier = "assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
                numeroNiveau.config(text=id_level)

def init_keys(f): #Les Binds
    #Binds direction
    f.bind("<Key-z>", lambda event : mouvement_joueur (event,"up"))
    f.bind("<Key-s>", lambda event : mouvement_joueur (event,"down"))
    f.bind("<Key-q>", lambda event : mouvement_joueur (event,"left"))
    f.bind("<Key-d>", lambda event : mouvement_joueur (event,"right"))

    f.bind("<Key-Z>", lambda event : mouvement_joueur (event,"up"))
    f.bind("<Key-S>", lambda event : mouvement_joueur (event,"down"))
    f.bind("<Key-Q>", lambda event : mouvement_joueur (event,"left"))
    f.bind("<Key-D>", lambda event : mouvement_joueur (event,"right"))

    f.bind("<Key-Up>", lambda event : mouvement_joueur (event,"up"))
    f.bind("<Key-Down>", lambda event : mouvement_joueur (event,"down"))
    f.bind("<Key-Left>", lambda event : mouvement_joueur (event,"left"))
    f.bind("<Key-Right>", lambda event :mouvement_joueur (event,"right"))

    #Bind retour
    f.bind("<Escape>", lambda event : exit_key(event))

    #Bind clic gauche
    f.bind("<B1-Motion>", lambda event : clic_gauche(event))
    f.bind("<Button-1>", lambda event : clic_gauche(event))

    #Bind molette
    f.bind("<Button-2>", lambda event : deleteLastBlock(event))
    f.bind("<MouseWheel>", lambda event : deleteLastBlock(event))

def reset_solo():
    attention = tkinter.messagebox.askyesno("Attention", "Voulez vous reset la progression ?")
    if attention:
        originalPath = str(cwd)+"assets/data/origine"
        copyPath = str(cwd)+"assets/data/solo/"
        shutil.rmtree(copyPath)
        shutil.copytree(originalPath, copyPath)


################################################################### Mise en place de la fenetre ###################################################################

fenetre = Tk()

largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()

fenetre.title("Game & Cube")
fenetre.attributes('-fullscreen', True)
canevas = Canvas(fenetre, width=largeur, height=hauteur,bg='#3b3b3b')

################################################################### Autre ###################################################################
first_launch()
canevas.pack()
fenetre.mainloop()

"""
Problème si on del tout la liste des clé est del aussi (faut juste supp les bon blocs)
"""