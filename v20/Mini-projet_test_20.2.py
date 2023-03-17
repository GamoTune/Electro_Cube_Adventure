#Import des bibliothèques
import tkinter as tk, tkinter.messagebox; from tkinter import *; import pickle, os, shutil


################################################################### Les fonctions de mise en place des modes ###################################################################

def first_launch (): #La fonction "first_launch" permet de déclaré la plus part des variable globald
    global editBloc, cwd, imageBoutonPlayTest, imageBGGlobal, nombreCase, fonctionDeplacement, imageBoutonEditeurGommeSelect, imageBoutonEditeurGomme, imageBoutonEditeurPoubelleMonde, imageBoutonEditeurBlocPorte, editTest, originalPath, imageMonde1, imageMonde2, imageMonde3, imageResetSolo, imageBoutonEditeurItemCle, imageBoutonEditeurEditBloc, newColorBloc, freezeEdit, fenetreeditTest, listeNiveau, id_level, lienfichier, edit, imageBoutonSolo, imageBoutonEditeur, ligneX, ligneY, imageBoutonEditeurNiveauHaut, imageBoutonEditeurNiveauBas, imageBoutonEditeurNiveauGauche, imageBoutonEditeurNiveauDroite, imageBoutonEditeurSave, imageBoutonEditeurRetour, imageWIP, imageBoutonEditeurPoubelle, imageBoutonEditeurExit, imageEditeurInfos, fenetreinfosTest, imageBoutonEditeurBlocSolide, couleurBloc, typeDuBloc, imageBoutonEditeurBlocSpawn, delonespebloc, listeMonde, id_monde, solo, lienmonde, imageBoutonEditeurInfos

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
    editBloc = False #Permet de vérifier si la fenetre de l'édition de bloc de l'éditeur est déjà créer
    editTest = False #Permet de vérifier si la l'édition de bloc de l'éditeur est activer
    #Import des images
    imageBoutonSolo = PhotoImage(file = str(cwd)+"assets/images/bouton_solo.png")
    imageBoutonEditeur = PhotoImage(file = str(cwd)+"assets/images/bouton_editeur.png")
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
    imageBoutonEditeurBlocPorte = PhotoImage(file= str(cwd)+"assets/images/bouton_bloc_porte.png")
    imageBoutonEditeurInfos = PhotoImage(file= str(cwd)+"assets/images/help.png")
    imageBoutonEditeurEditBloc = PhotoImage(file= str(cwd)+"assets/images/edit_bloc.png")
    imageBoutonEditeurGomme = PhotoImage(file= str(cwd)+"assets/images/gomme.png")
    imageBoutonEditeurGommeSelect = PhotoImage(file= str(cwd)+"assets/images/gomme_select.png")
    imageResetSolo = PhotoImage(file= str(cwd)+"assets/images/Reset.png")
    imageBoutonPlayTest = PhotoImage(file= str(cwd)+"assets/images/play_test.png")
    imageBoutonEditeurPoubelleMonde = PhotoImage(file = str(cwd)+"assets/images/poubelle_monde.png")
    imageMonde1 = PhotoImage(file= str(cwd)+"assets/images/M1.png")
    imageMonde2 = PhotoImage(file= str(cwd)+"assets/images/M2.png")
    imageMonde3 = PhotoImage(file= str(cwd)+"assets/images/M3.png")
    imageBGGlobal = PhotoImage(file= str(cwd)+"assets/images/fond_editeur.png")
    init_keys(fenetre) #Appel la fonction des binds 
    grille()
    menu() #Appe la fonction menu (affichage du main menu)

def lancement_edition (): #La fonction "lancement_edition" permet de mettre en place tout le système de la création de niveau
    global edit, lienfichier, ligneX, fenetre_bouton, id_level, numeroNiveau, message_editeur, fonctionDeplacement, boutonGomme
    close_menu() #Ferme le menu

######################################################################## Le cadirage
    ligneCreer_x = nombrePixel #Variable qui renseigne à quel x les lignes du cadriage doivent être placer
    ligneCreer_y = nombrePixel #Variable qui renseigne à quel y les lignes du cadriage doivent être placer

#Création des ligne de l'éditeur (le cadriage dans le fond qui permet de mieux savoir où les blocs seront placer)
    while ligneCreer_x <= largeur: #Temps que la bordure de l'écran n'est pas attein les lignes sont placer
        ligneX.append(canevas.create_line(ligneCreer_x, 0, ligneCreer_x, hauteur)) #Crée une ligne vertical en fonction de "ligneCreer_x"
        ligneCreer_x += nombrePixel #Ajout du nombre de pixel n'esaissaire entre 2 ligne (la taille d'un bloc)

    while ligneCreer_y <= hauteur: #Temps que la bordure de l'écran n'est pas attein les lignes sont placer
        ligneY.append(canevas.create_line(0, ligneCreer_y, largeur, ligneCreer_y)) #Crée une ligne horizontal en fonction de "ligneCreer_y"
        ligneCreer_y += nombrePixel #Ajout du nombre de pixel n'esaissaire entre 2 ligne (la taille d'un bloc)

######################################################################## L'édition
    edit = True #Indication au programme que l'éditeur est lancer et que les fonction de l'édition peuvent maintement fonctionnner
    id_level = [0,0] #Le level de départ est [0,0]
    lienfichier = str(cwd)+"assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt" #Changement du lien des ficier pour chercher le niveau dans le dossier editeur
    load_level() #Appel de la fonction qui charge un niveau
    load_world() #Appel de la fonction qui change un monde
    fonctionDeplacement = level_search #Changement du binds des touches de direction pour changer de niveau plus facilement dans l'éditeur
    #Fenetre des infos / boutons
    fenetre_bouton = tk.Toplevel() #Création de la fenetre des fonction/boutons de l'éditeur
    fenetre_bouton.geometry('312x621') #taille 1 bouton = taille que tu veux + 3
    fenetre_bouton.resizable(False,False) #Fenetre non redimentionable
    fenetre_bouton.attributes('-topmost',1) #Fenetre toujours au premier plan
    fenetre_bouton.protocol("WM_DELETE_WINDOW", disable_event) #Fenetre non detruisable manuelement
    fenetre_bouton.attributes('-alpha',1) #Permet de changer l'opacité de la fenetre
    #Création des boutons / texte sur la fenetre de l'éditeur
    Button(fenetre_bouton, image=imageBoutonEditeurSave, command=save_level).place(x=0,y=0) #bouton_save
    Button(fenetre_bouton, image=imageBoutonEditeurRetour, command=deleteLastBlock).place(x=103,y=0) #bouton_retour
    Button(fenetre_bouton, image=imageBoutonEditeurPoubelle, command=lambda:delete_all_blocks("")).place(x=206,y=0) #boutonEditeurPoubelle
    Button(fenetre_bouton, image=imageBoutonEditeurNiveauHaut, command=lambda:level_search("up")).place(x=103,y=103) #bouton_niveau_up
    Button(fenetre_bouton, image=imageBoutonEditeurNiveauBas, command=lambda:level_search("down")).place(x=103,y=309) #bouton_niveau_down
    Button(fenetre_bouton, image=imageBoutonEditeurNiveauGauche, command=lambda:level_search("left")).place(x=0,y=206) #bouton_niveau_left
    Button(fenetre_bouton, image=imageBoutonEditeurNiveauDroite, command=lambda:level_search("right")).place(x=206,y=206) #bouton_niveau_right
    Button(fenetre_bouton, image=imageBoutonEditeurPoubelleMonde, command=delete_all_level).place(x=103,y=412) #boutonEditeurDellAll
    Button(fenetre_bouton, image=imageBoutonEditeurExit, command=lambda:retour_menu("postEditMenu")).place(x=206,y=515) #boutonEditeurExit
    numeroNiveau = Label(fenetre_bouton, text=id_level, font="Arial, 30") #Affichage du numéro du niveau actuel
    numeroNiveau.pack(padx=103, pady=230) #numeroNiveau
    Button(fenetre_bouton, image=imageBoutonEditeurBlocSolide, command=lambda:type_Blocs("solide")).place(x=0,y=103) #bouton_bloc_solide
    Button(fenetre_bouton, image=imageBoutonEditeurBlocSpawn, command=lambda:type_Blocs("spawn")).place(x=206,y=103) #bouton_bloc_spawn
    Button(fenetre_bouton, image=imageBoutonEditeurItemCle, command=lambda:type_Blocs("key")).place(x=0,y=309) #bouton_item_key
    boutonGomme = Button(fenetre_bouton, image=imageBoutonEditeurGomme, command=delspebloc)
    boutonGomme.place(x=0,y=412) #bouton_gomme
    Button(fenetre_bouton, image=imageBoutonEditeurBlocPorte, command=lambda:type_Blocs("porte")).place(x=206,y=309) #bouton_bloc_port
    Button(fenetre_bouton, image=imageBoutonEditeurEditBloc, command=set_edit_objet).place(x=206,y=412) #bouton_edit
    message_editeur = Label(fenetre_bouton, text="", font="Arial, 30" ) #Affiche du type de bloc / erreur / info général
    message_editeur.place(x=103,y=568, anchor=CENTER) #message_editeur

def lancement_solo ():
    global joueur, positionJoueur, lienfichier, id_level, solo, fonctionDeplacement
    solo = True #Active le mod solo
    fonctionDeplacement = mouvement_joueur #Change les binds des déplacements pour déplacer le joueur
    id_level = [0,0] #Change l'id des niveaux en [0,0] pur commencer au start d'un niveau
    load_level() #Charge le niveau
    load_world() #Charge le monde
    for pasdubloc in listeNiveau: #Cherche si un bloc d'apparition du joueur existe dans le niveau [0,0] pour faire aparaitre 
        if pasdubloc["typeBloc"] == 1: #Si il existe, les coordonées d'apparition sont mis à jour
            posjxstart = pasdubloc["coordsBloc"][0]
            posjystart = pasdubloc["coordsBloc"][1]
            break #Quand les coordonnées sont trouver, la boucle s'arrete pour ne pas chercher des coordonnées pour rien
    try: posjxstart #Si in n'y a pas de bloc d'apparition, la variable n'est pas déclarer donc il y a une erreur
    except: #Si il n'y a donc pas de coordonnées d'appartion, le mode solo ne se lance pas
        solo = False #Désactivation du mode solo
        lienfichier = "assets/data/menu.txt" #Changement du lien pour charger le menu
        load_level() #Chargement du menu
        tkinter.messagebox.showerror("Erreur", "Il n'y a pas de bloc d'apparition dans ce monde") #Affichage d'un message d'erreur
    else: #Si il y a un bloc d'apparition
        joueur = canevas.create_rectangle(0, 0, nombrePixel, nombrePixel, fill='blue', width=0) #Création du joueur
        canevas.move(joueur,posjxstart*nombrePixel, posjystart*nombrePixel) #Déplacement du joueur au coordonnées d'apparition
        positionJoueur = [posjxstart, posjystart] #0 = x & 1 = y #Actualisation des position du joueur sur la grille
        close_menu() #Fermeture du menu

def play_test ():
    global lienmonde, lienfichier, editTest, id_level
    originalPath = str(cwd)+"assets/data/editeur" #"originalPath" contient le lien du dossier éditeur
    copyPath = str(cwd)+"assets/data/test_editeur/" #"copyPath" contient le lien du dossier test_editeur où vont etre copier les fichier de l'éditeur pour ne pas modifier les fichier dans l'éditeur
    if os.path.exists(copyPath): #Si le docier contient déjà quelque chose, il est détruit puis recréer 
        shutil.rmtree(copyPath) #Suprétion du docier
    shutil.copytree(originalPath, copyPath) #Création de la copie du docier d'origine
    id_level = [0,0] #Le niveau a charger est le [0,0]
    lienmonde = str(cwd)+"assets/data/test_editeur/monde"+str(id_monde)+"_info.txt" #Mise à jour du lien pour charger le monde
    lienfichier = str(cwd)+"assets/data/test_editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt" #Mise à jour du lien pour charger le niveau
    editTest = True #Le mode du test des niveau de l'éditeur est activer
    lancement_solo() #Appel de la fonction du lancement du solo


################################################################### Fonctions du joueur ###################################################################

def mouvement_joueur (direction): #Permet au joueur de ce déplacer dans un niveau et d'intéragire avec des objets
    #Direction est un paramètre de la fonction, renseigne sur le direction soueyter par l'utilisateur
    global positionJoueur, listeMonde
    
    if solo == True: #Si le mode solo est activer la fonction sera utilisable, sinon, non
        pad = 0 #Variable temporaire pour une boucle while
        verify = False #verify est une variable local qui indique à une partie de la fonction si elle peut etre executer

        if direction == "up": #Si la direction est egale à "up"
            posJTestX = 0 #Test de la prochaine position du joueur dans la grille pour x
            posJTestY = -1 #Test de la prochaine position du joueur dans la grille pour y
            xyJ = 1 #Indique quel est l'axe qui est demander (0=x et 1=y)
            posJF = -1 #Donne de combien doit être changer les coordonnées du joueur en fonction de l'axe
            posMax = 0 #Donne la position max du joueur sur la grille 
            deplacement = [0, -nombrePixel] #Donne de combien le joueur doit ce déplacer sur la grille

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
        while pad != len(listeNiveau): #Parcours de la liste des blocs pour savoir si la prochaine destination du joueur se trouve sur un bloc ou non
            if  positionJoueur[0]+posJTestX == listeNiveau[pad]["coordsBloc"][0] and positionJoueur[1]+posJTestY == listeNiveau[pad]["coordsBloc"][1]: #Vérification
                #Collision avec bloc solide
                if listeNiveau[pad]["typeBloc"] == 0: #Vérification du type du bloc # 0 = bloc solide
                    verify = True #verify=True signifie que la partie d'aprés ne peut pas s'executé

                #Collision avec bloc spawn
                elif listeNiveau[pad]["typeBloc"] == 1: # 1 = spawn
                    verify = False #La suite va pouvoir s'éxécuté

                #Collision avec clé
                elif listeNiveau[pad]["typeBloc"] == 2: # 2 = clé
                    verify = False

                    for blocinListeMonde in listeMonde: #Parcours de la liste Monde pour trouver de quel clé il s'agit
                        if positionJoueur[0]+posJTestX == blocinListeMonde["coordsBloc"][0] and positionJoueur[1]+posJTestY == blocinListeMonde["coordsBloc"][1] and blocinListeMonde["idLevel"] == str(id_level) and blocinListeMonde["keyCollect"] == 0: #Vérification que la clé n'est pas déjà été prise
                                touch_key(pad,blocinListeMonde) #Une fois que la clé est trouver, la fonction touch_key est appeler
                                pad -= 1 #Comme un bloc est détruit, un petit retour en arrière sur le parcours des bloc est obligatoire

                #Collision avec bloc porte
                elif listeNiveau[pad]["typeBloc"] == 3: # 3 = porte
                    verify = True
                    for blocinListeMonde in listeMonde: #Parcours de la liste Monde pour trouver de quel porte il s'agit
                        if positionJoueur[0]+posJTestX == blocinListeMonde["coordsBloc"][0] and positionJoueur[1]+posJTestY == blocinListeMonde["coordsBloc"][1] and blocinListeMonde["idLevel"] == str(id_level) and blocinListeMonde["keyCollect"] == 1: #Vérification que la clé est déjà été prise
                                touch_porte(pad,blocinListeMonde) #Une fois que la porte est trouver, la fonction touch_porte est appeler
                                pad -= 1 #Comme un bloc est détruit, un petit retour en arrière sur le parcours des bloc est obligatoire

            pad += 1 #Ajout de 1 à pad pour avancer dans la boucle while

        if verify == False: #Si verify = False (donc que aucun bloc ne bloque le passage), une vérification des limite de l'écran s'impose
            #Collision limite map 
            if positionJoueur[xyJ] == posMax: #Si la position du joueur est egale à la limite de l'écran (ou de la map)
                level_search(direction) #La fonction level_search est appeler
            #Mouvement
            else: #Sinon
                canevas.move(joueur, deplacement[0], deplacement[1]) #Le joueur est déplacer sur la case demander
                positionJoueur[xyJ] = positionJoueur[xyJ]+posJF #Les coordonnées du joueur sont actualiser

def touch_key (pad,blocinListeMonde): #Fonction touch_key permet de récupérer une clé
    for blocinListeMonde2 in listeMonde: #Parcours de la liste Monde 
        if blocinListeMonde2["idKeyPorte"] == blocinListeMonde["idKeyPorte"]: #Si l'identifient de la clé correspond à selui demander alors
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


################################################################### Fonctions du mode édition ###################################################################

def type_Blocs (tBloc): #Indication du type de bloc à placer
    global typeDuBloc, couleurBloc, message_editeur
    if tBloc == "solide":
        typeDuBloc = 0
        couleurBloc = 'black'
        message_editeur.config(text="Bloc solide")

    elif tBloc == "spawn":
        if id_level == [0,0]:
            typeDuBloc = 1
            couleurBloc = 'cyan'
            message_editeur.config(text="Bloc spawn")
        else:
            message_editeur.config(text="[0,0] only")

    elif tBloc == "key":
        typeDuBloc = 2
        couleurBloc = 'orange'
        message_editeur.config(text="Item clé")

    elif tBloc == "porte":
        typeDuBloc = 3
        couleurBloc = 'orange'
        message_editeur.config(text="Bloc porte")

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
            if typeDuBloc == 2:
                demiPixel = nombrePixel/4
            else:
                demiPixel = 0
            listeNiveau.append({"coordsBloc" : [xSourisCase, ySourisCase], "idBloc" : canevas.create_rectangle(xSourisCase*nombrePixel+demiPixel, ySourisCase*nombrePixel+demiPixel, xSourisCase*nombrePixel+nombrePixel-demiPixel, ySourisCase*nombrePixel+nombrePixel-demiPixel, fill=couleurBloc), "typeBloc" : typeDuBloc, "color" : str(couleurBloc)})

    elif editBloc == True: #Y a un truc a faire ici niveau optimisation en mettant tout dans le même try
        try:
            entryIDcle.destroy()
            boutonIDCleValidation.destroy()
            couleurSet.destroy()
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

                    couleurSet = Scale(fenetre_edit_bloc, orient='horizontal', from_=1, to=8, resolution=1, tickinterval=2, length=180, label='Couleur', font=("Arial, 10"), command=change_color)
                    couleurSet.place(x=250,y=200)
                break
            else:
                textTypeBlocSelect.config(text="Air")

def delete_all_blocks (val): #Destruction total du niveau
    global listeNiveau
    if val != "FORCE":
        attention = tkinter.messagebox.askyesno("Attention", "Voulez vous détruire tout les blocs de ce niveau ?")
        if attention:
            val = "FORCE"
    if val == "FORCE":
        for blocinListeNiveau in listeNiveau:
            for blocinListeMonde in listeMonde:
                if blocinListeMonde["coordsBloc"] == blocinListeNiveau["coordsBloc"] and blocinListeMonde["idLevel"] == str(id_level):
                    listeMonde.remove(blocinListeMonde)
            canevas.delete(blocinListeNiveau["idBloc"])
        listeNiveau.clear()

def deleteLastBlock (): #Destruction du dernier bloc placé
    global listeNiveau
    if len(listeNiveau) > 0 and edit == True:
        canevas.delete(listeNiveau[-1]["idBloc"])
        if listeNiveau[-1]["typeBloc"] == 2:
            for blocinListeMonde in listeMonde:
                if blocinListeMonde["coordsBloc"] == listeNiveau[-1]["coordsBloc"]:
                    del blocinListeMonde
                    break
        del listeNiveau[-1]

def delete_all_level():
    global id_level
    attention = tkinter.messagebox.askyesno("Attention", "Voulez vous détruire tout les niveaux du mondes ?")
    if attention:
        delete_all_blocks("FORCE")
        id_level = [0,0]
        path = str(cwd)+"assets/data/editeur/monde"+str(id_monde)
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))
        listeMonde.clear()

def save_level (): #Sauvegarde du niveau
    with open(lienfichier, "wb") as fichierNiveau:
        pickle.dump(listeNiveau, fichierNiveau)
        print(lienfichier)

def save_world (): #Sauvegarde du monde
    with open(lienmonde, "wb") as fichierMonde:
        pickle.dump(listeMonde, fichierMonde)

def load_world (): #Chargement du monde
    global listeMonde
    listeMonde.clear()
    if os.path.exists(lienmonde):
        with open(lienmonde, "rb") as fichierMonde:
            listeMonde = pickle.load(fichierMonde)

def info_editeur (): #Fenêtre d'infos des action possible
    global fenetreinfosTest, fenetre_infos
    if fenetreinfosTest == False:
        fenetre_infos = tk.Toplevel()
        fenetre_infos.resizable(False,False)
        fenetre_infos.geometry('1200x600')
        fenetre_infos.attributes('-topmost',1)
        fenetre_infos.protocol("WM_DELETE_WINDOW", disable_event)
        infosLabel = Label(fenetre_infos, image=imageEditeurInfos)
        infosLabel.pack()
        fenetreinfosTest = True
    elif fenetreinfosTest == True:
        fenetre_infos.destroy()
        fenetreinfosTest = False

def delspebloc (): #Toggle de la destruciton d'un bloc spécifique (utilise clic_gauche pour delete)
    global delonespebloc, boutonGomme
    if delonespebloc == False:
        delonespebloc = True
        boutonGomme.configure(image = imageBoutonEditeurGommeSelect)
    else:
        delonespebloc = False
        boutonGomme.configure(image = imageBoutonEditeurGomme)

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
        newColorBloc = 'red'
    elif couleurSet.get() == 2:
        newColorBloc = 'orange'
    elif couleurSet.get() == 3:
        newColorBloc = 'yellow'
    elif couleurSet.get() == 4:
        newColorBloc = 'green'
    elif couleurSet.get() == 5:
        newColorBloc = 'blue'
    elif couleurSet.get() == 6:
        newColorBloc = 'pink'
    elif couleurSet.get() == 7:
        newColorBloc = 'purple'
    elif couleurSet.get() == 8:
        newColorBloc = 'brown'

    canevas.itemconfig(selectBlocID, fill=newColorBloc)
    for blocinListeNiveau in listeNiveau:
        if blocinListeNiveau["idBloc"] == selectBlocID:
            blocinListeNiveau["color"] = newColorBloc
            break


################################################################### Fonctions du fonctionnement global du programme ###################################################################

def grille (): #Met en place la grille des blocs 
    global nombrePixel, nombreCaseX, nombreCaseY, nombreCase
    nombrePixel = largeur/nombreCase #nombrePixel = nombre de pixels par case sur l'écran (en fonction de la résolution de l'écran, le nombre de pixel change pour toujours avoir le même nombre de case à l'écran)
    nombreCaseX = round(largeur/nombrePixel) #Le nombre de case en X permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en X
    nombreCaseY = round(hauteur/nombrePixel) #Le nombre de case en Y permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en Y

def disable_event(): #Disable
   pass

def exit_key (): #Permet des retour au menu avec la touche "echap"
    global editTest
    if edit == True:
        retour_menu("postEditMenu")
    elif solo == True:
        if editTest == True:
            retour_menu("postEditTestMenu")
            editTest = False
        else:
            retour_menu("postSoloMenu")
    else:
        retour_menu("Menu")

def load_level (): #Charge les niveau et détruit les ancien
    global lienfichier, listeNiveau, couleurBloc, typeDuBloc
    for blocinListeNiveau in listeNiveau:
        canevas.delete(blocinListeNiveau["idBloc"])
    listeNiveau.clear()

    if os.path.exists(lienfichier):
        with open(lienfichier, "rb") as fichier:
            listeNiveau = pickle.load(fichier)

    elif solo == 1:
        pass

    else:
        if edit == True:
            with open(lienfichier, "wb") as fichierNiveau:
                pickle.dump(listeNiveau, fichierNiveau)

    for blocinListeNiveau in listeNiveau:
        del blocinListeNiveau["idBloc"]

    for blocinListeNiveau in listeNiveau:
        couleurBloc = blocinListeNiveau["color"]
        if blocinListeNiveau["typeBloc"] == 2:
            demiPixel = nombrePixel/4
        else:
            demiPixel = 0
        blocinListeNiveau["idBloc"] = (canevas.create_rectangle(blocinListeNiveau["coordsBloc"][0]*nombrePixel+demiPixel, blocinListeNiveau["coordsBloc"][1]*nombrePixel+demiPixel, blocinListeNiveau["coordsBloc"][0]*nombrePixel+nombrePixel-demiPixel, blocinListeNiveau["coordsBloc"][1]*nombrePixel+nombrePixel-demiPixel, fill=couleurBloc))
    typeDuBloc = 0
    couleurBloc = 'black'

def level_search (direction): #Cherche le bon niveau a charger
    global id_level, lienfichier, numeroNiveau
    if editTest == True:
        repertoirJeu = "test_editeur/"
    elif solo == True:
        repertoirJeu = "solo/"
    elif edit == True:
        repertoirJeu = "editeur/"

    save_level()
    if direction =='up':
        lienfichier = str(cwd)+"assets/data/"+str(repertoirJeu)+"monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1]-1)+".txt"
        if os.path.exists(lienfichier):
            id_level[1] -= 1
            if solo == True:
                positionJoueur[1] = nombreCaseY-1
                canevas.moveto(joueur, positionJoueur[0]*nombrePixel-1, positionJoueur[1]*nombrePixel-1)

    if direction =='down':
        lienfichier = str(cwd)+"assets/data/"+str(repertoirJeu)+"monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1]+1)+".txt"
        if os.path.exists(lienfichier):
            id_level[1] += 1
            if solo == True:
                positionJoueur[1] = 0
                canevas.moveto(joueur, positionJoueur[0]*nombrePixel-1, -positionJoueur[1]*nombrePixel-1)

    if direction =='left':
        lienfichier = str(cwd)+"assets/data/"+str(repertoirJeu)+"monde"+str(id_monde)+"/niveau"+str(id_level[0]-1)+str(id_level[1])+".txt"
        if os.path.exists(lienfichier):
            id_level[0] -= 1
            if solo == True:
                positionJoueur[0] = nombreCaseX-1
                canevas.moveto(joueur, positionJoueur[0]*nombrePixel-1, positionJoueur[1]*nombrePixel-1)

    if direction =='right':
        lienfichier = str(cwd)+"assets/data/"+str(repertoirJeu)+"monde"+str(id_monde)+"/niveau"+str(id_level[0]+1)+str(id_level[1])+".txt"
        if os.path.exists(lienfichier):
            id_level[0] += 1
            if solo == True:
                positionJoueur[0] = 0
                canevas.moveto(joueur, -positionJoueur[0]*nombrePixel-1, positionJoueur[1]*nombrePixel-1)

    if edit == True:
        numeroNiveau.configure(text=id_level)
    load_level()

def init_keys(f): #Les Binds
    #Binds direction
    f.bind("<Key-z>", lambda event : fonctionDeplacement ("up"))
    f.bind("<Key-s>", lambda event : fonctionDeplacement ("down"))
    f.bind("<Key-q>", lambda event : fonctionDeplacement ("left"))
    f.bind("<Key-d>", lambda event : fonctionDeplacement ("right"))

    f.bind("<Key-Z>", lambda event : fonctionDeplacement ("up"))
    f.bind("<Key-S>", lambda event : fonctionDeplacement ("down"))
    f.bind("<Key-Q>", lambda event : fonctionDeplacement ("left"))
    f.bind("<Key-D>", lambda event : fonctionDeplacement ("right"))

    f.bind("<Key-Up>", lambda event : fonctionDeplacement ("up"))
    f.bind("<Key-Down>", lambda event : fonctionDeplacement ("down"))
    f.bind("<Key-Left>", lambda event : fonctionDeplacement ("left"))
    f.bind("<Key-Right>", lambda event : fonctionDeplacement ("right"))

    #Bind retour
    f.bind("<Escape>", lambda event : exit_key())

    #Bind clic gauche
    f.bind("<B1-Motion>", lambda event : clic_gauche(event))
    f.bind("<Button-1>", lambda event : clic_gauche(event))

    #Bind molette
    f.bind("<Button-2>", lambda event : deleteLastBlock())
    f.bind("<MouseWheel>", lambda event : deleteLastBlock())

def reset_solo():
    attention = tkinter.messagebox.askyesno("Attention", "Voulez vous reset la progression ?")
    if attention:
        originalPath = str(cwd)+"assets/data/origine"
        copyPath = str(cwd)+"assets/data/solo/"
        shutil.rmtree(copyPath)
        shutil.copytree(originalPath, copyPath)


################################################################### Foncitons des menus ###################################################################

def menu ():
    global menuFrame

    menuFrame = Frame(fenetre, width=largeur/2+largeur/4, height=hauteur/2+hauteur/4 ,bg='black')
    menuFrame.place(x=largeur/2, y=hauteur/2,anchor=CENTER)

    boutonSolo = Button(menuFrame, image=imageBoutonSolo, command=menu_pre_solo)
    boutonSolo.place(x=(largeur/2+largeur/4)/2-((largeur/2+largeur/4)/2)/2, y=(hauteur/2+hauteur/4)/2, anchor=CENTER)

    boutonEditeur = Button(menuFrame, image=imageBoutonEditeur, command=menu_pre_edition)
    boutonEditeur.place(x=(largeur/2+largeur/4)/2+((largeur/2+largeur/4)/2)/2, y=(hauteur/2+hauteur/4)/2, anchor=CENTER)

    boutonExit = Button(menuFrame, image=imageBoutonEditeurExit, command=fenetre.destroy)
    boutonExit.place(x=(largeur/2+largeur/4)/2, y=(hauteur/2+hauteur/4)/2, anchor=CENTER)

def menu_pre_edition ():
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

    boutonEditPlayTest = Button(menuPostEdit, image=imageBoutonPlayTest, command=play_test)
    boutonEditPlayTest.place(x=(largeur/2+largeur/4)/2, y=(hauteur/2+hauteur/4)-(hauteur/2+hauteur/4)/1.37, anchor=CENTER)

    boutonEditeurInfo = Button(menuPostEdit, image=imageBoutonEditeurInfos, command=info_editeur)
    boutonEditeurInfo.place(x=(largeur/2+largeur/4)-75,y=75, anchor=CENTER)

def monde_finder_editeur (numMonde):
    global id_monde, lienmonde, lienfichier

    id_monde = numMonde
    lienmonde = str(cwd)+"assets/data/editeur/monde"+str(id_monde)+"_info.txt"
    lienfichier = str(cwd)+"assets/data/editeur/monde"+str(id_monde)+"/niveau"+str(id_level[0])+str(id_level[1])+".txt"
    lancement_edition()

def menu_pre_solo ():
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
    elif goToMenu == "postEditTestMenu":
        canevas.delete(joueur)
        positionJoueur.clear()
        solo = False
        menuPostEdit.place(x=largeur/2, y=hauteur/2,anchor=CENTER)
        save_level()
        save_world()
    lienfichier = "assets/data/menu.txt"
    load_level()

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
2 clé ne peuvent pas avoir le même id sinon irécuprable
"""