#Import des bibliothèques
import tkinter as tk, tkinter.messagebox; import tkinter.scrolledtext; from tkinter import *; import pickle, os, shutil, webbrowser; from PIL import Image, ImageTk



################################################################### Les fonctions de mise en place du programme ###################################################################

def start(): #La fonction "start" permet de déclaré la plus part des variable global
    global monde, fenetre, etatEditeur, toggleMouvement, creditTexte, pbPlayer, bgMenuCredit, patchNotesTexte, bgMenuMAJ, directionsBinds, theKey, commandMondeSolo, exitCommand, imageResetSoloToggle, imageBoutonPlayTestToggle, imageNotExitTest, imageMonde1Test, imageMonde2Test, imageMonde3Test, imageNotExit, commandMondeEditeur, nombrePixel, imageMonde1Del, imageMonde2Del, imageMonde3Del, bgmenuresultat, imageBoutonEditeurFinish, largeurFenetre, hauteurFenetre, canevas, lienIconeFenetre, etatJeu, nombreCaseY, nombreCaseX, editBloc, racine, imageBoutonPlayTest, bgMenu, imageOK, imageInfoBouton, tailleImage, ratioImage, bgmenuSoloFrame, ratioFenetre, bgMenuEdition, nombreCase, imageBoutonEditeurGommeSelect, imageBoutonEditeurGomme, imageBoutonEditeurPoubelleMonde, imageBoutonEditeurBlocPorte, editTest, imageMonde1, imageMonde2, imageMonde3, imageResetSolo, imageBoutonEditeurItemCle, imageBoutonEditeurEditBloc, id_level, imageBoutonSolo, imageBoutonEditeur, ligneX, ligneY, imageBoutonEditeurNiveauHaut, imageBoutonEditeurNiveauBas, imageBoutonEditeurNiveauGauche, imageBoutonEditeurNiveauDroite, imageBoutonEditeurTP, imageBoutonEditeurRetour, imageWIP, imageBoutonEditeurPoubelle, imageExit, imageBoutonEditeurBlocSolide, couleurBloc, typeDuBloc, imageBoutonEditeurBlocSpawn, editGomme, id_monde, imageBoutonEditeurInfos

    ################################################################### Mise en place de la fenetre et du canevas

    fenetre = Tk()

    largeurFenetre = fenetre.winfo_screenwidth()
    hauteurFenetre = fenetre.winfo_screenheight()

    fenetre.title("Game & Cube")
    
    fenetre.attributes('-fullscreen', True)
    canevas = Canvas(fenetre, width=largeurFenetre, height=hauteurFenetre,bg='#3b3b3b')


    """monde={
            "niveaux":{
                    "0,0":[
                                {"idAssoc" : 0, "idTk":0, "x":0, "y":0, "type":0, "couleur":"black", "collect":0},
                                {"idAssoc" : 0, "idTk":0, "x":1, "y":0, "type":2, "couleur":"blue", "collect":0},
                                {"idAssoc" : 0, "idTk":0, "x":1, "y":1, "type":4, "couleur":"red", "collect":0}
                        ],

                    "0,1":[
                                {"idAssoc" : 0, "idTk":0, "x":0, "y":0, "type":1, "couleur":"black", "collect":0},
                                {"idAssoc" : 0, "idTk":0, "x":1,"y":0, "type":3, "couleur":"blue", "collect":0},
                                {"idAssoc" : 0, "idTk":0, "x":1, "y":1, "type":9, "couleur":"red", "collect":0}
                        ]
                    },
            "lastCoords":[[],[],[]],

            "runTime" : [0,0,0]

            "reset" : [True,True,True]

            }"""


    monde = {   "niveaux":{"0,0":[]},
                "lastCoords":[[],[],[]],
                "runTime":[0,0,0],
                "reset" : [True,True,True]
             }

    pbPlayer = [0,0,0]

    etatJeu="init"
    etatEditeur = "pose"
    racine = os.getcwd()
    racine = racine.replace("\\", "/" )
    racine = racine+str("/")
    init_dossiers_et_fichiers(racine)

    #Les coordonnées virtuel sont des coordonnées d'une matrice créée en fonction du nombre de cases à l'écran (défini avec "nombreCase")
    id_level = [0,0] #Numéro du niveau dans le quel on est (quand on change de niveau on ajoute ou retire 1 ) [default : [0,0]]
    id_monde = 1 #Numéro du monde dans le quel on est

    directionsBinds = {'z':"up",'q':"left",'d':"right",'s':"down"}
    theKey = ""

    nombreCase = 48 #En largeurFenetre (default = 48)
    nombrePixel = largeurFenetre/nombreCase #nombrePixel = nombre de pixels par case sur l'écran (en fonction de la résolution de l'écran, le nombre de pixel change pour toujours avoir le même nombre de case à l'écran)
    nombreCaseX = round(largeurFenetre/nombrePixel) #Le nombre de case en X permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en X
    nombreCaseY = round(hauteurFenetre/nombrePixel) #Le nombre de case en Y permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en Y
    ligneX = [] #Liste des ID des lignes X crées
    ligneY = [] #Liste des ID des lignes X crées

    commandMondeSolo = lancement_solo
    exitCommand = exit_menu
    commandMondeEditeur = lancement_editeur

    couleurBloc = 'black' #Défini la couleur d'un bloc
    typeDuBloc = 0 #Défini quel est le type de bloc (0 = solide, 1 = spawn, 2 = clé, 3 = porte)
    toggleMouvement = False
    editGomme = False #Permet de vérifier si la gomme de l'éditeur est déjà créer
    editBloc = False #Permet de vérifier si la fenetre de l'édition de bloc de l'éditeur est déjà créer
    editTest = False #Permet de vérifier si la l'édition de bloc de l'éditeur est activer
    #Import des images
    ratioFenetre = largeurFenetre/2560 #Calcule d'un ratio entre la résolution utilisé par l'utilisateur et la résolution utilisé pour mettre en place toutes les position d'image
    tailleImage = 100
    ratioImage = int(tailleImage*ratioFenetre)
    #Redimentionnement des images pour correspondre à la résolution voulue
    imageBoutonSolo = ImageTk.PhotoImage(Image.open(racine+"assets/images/bouton_solo.png").resize((ratioImage, ratioImage))) 
    imageBoutonEditeur = ImageTk.PhotoImage(Image.open(racine+"assets/images/bouton_editeur.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurNiveauHaut = ImageTk.PhotoImage(Image.open(racine+"assets/images/fleche_haut.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurNiveauBas = ImageTk.PhotoImage(Image.open(racine+"assets/images/fleche_bas.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurNiveauGauche = ImageTk.PhotoImage(Image.open(racine+"assets/images/fleche_gauche.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurNiveauDroite = ImageTk.PhotoImage(Image.open(racine+"assets/images/fleche_droite.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurTP = ImageTk.PhotoImage(Image.open(racine+"assets/images/bouton_bloc_tp.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurRetour = ImageTk.PhotoImage(Image.open(racine+"assets/images/retour.png").resize((ratioImage, ratioImage)))
    imageWIP = ImageTk.PhotoImage(Image.open(racine+"assets/images/WIP.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurPoubelle = ImageTk.PhotoImage(Image.open(racine+"assets/images/poubelle.png").resize((ratioImage, ratioImage)))
    imageExit = ImageTk.PhotoImage(Image.open(racine+"assets/images/exit.png").resize((ratioImage, ratioImage)))
    imageNotExit = ImageTk.PhotoImage(Image.open(racine+"assets/images/not_exit.png").resize((ratioImage, ratioImage)))
    imageNotExitTest = ImageTk.PhotoImage(Image.open(racine+"assets/images/not_exit_test.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurBlocSolide = ImageTk.PhotoImage(Image.open(racine+"assets/images/bouton_bloc_solide.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurBlocSpawn = ImageTk.PhotoImage(Image.open(racine+"assets/images/bouton_bloc_spawn.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurItemCle = ImageTk.PhotoImage(Image.open(racine+"assets/images/bouton_item_cle.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurBlocPorte = ImageTk.PhotoImage(Image.open(racine+"assets/images/bouton_bloc_porte.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurInfos = ImageTk.PhotoImage(Image.open(racine+"assets/images/help.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurEditBloc = ImageTk.PhotoImage(Image.open(racine+"assets/images/edit_bloc.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurGomme = ImageTk.PhotoImage(Image.open(racine+"assets/images/gomme.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurGommeSelect = ImageTk.PhotoImage(Image.open(racine+"assets/images/gomme_select.png").resize((ratioImage, ratioImage)))
    imageResetSolo = ImageTk.PhotoImage(Image.open(racine+"assets/images/Reset.png").resize((ratioImage, ratioImage)))
    imageResetSoloToggle = ImageTk.PhotoImage(Image.open(racine+"assets/images/Reset_toggle.png").resize((ratioImage, ratioImage)))
    imageBoutonPlayTest = ImageTk.PhotoImage(Image.open(racine+"assets/images/play_test.png").resize((ratioImage, ratioImage)))
    imageBoutonPlayTestToggle = ImageTk.PhotoImage(Image.open(racine+"assets/images/play_test_toggle.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurPoubelleMonde = ImageTk.PhotoImage(Image.open(racine+"assets/images/poubelle_monde.png").resize((ratioImage, ratioImage)))
    imageMonde1 = ImageTk.PhotoImage(Image.open(racine+"assets/images/M1.png").resize((ratioImage, ratioImage)))
    imageMonde2 = ImageTk.PhotoImage(Image.open(racine+"assets/images/M2.png").resize((ratioImage, ratioImage)))
    imageMonde3 = ImageTk.PhotoImage(Image.open(racine+"assets/images/M3.png").resize((ratioImage, ratioImage)))
    imageMonde1Del = ImageTk.PhotoImage(Image.open(racine+"assets/images/M1_del.png").resize((ratioImage, ratioImage)))
    imageMonde2Del = ImageTk.PhotoImage(Image.open(racine+"assets/images/M2_del.png").resize((ratioImage, ratioImage)))
    imageMonde3Del = ImageTk.PhotoImage(Image.open(racine+"assets/images/M3_del.png").resize((ratioImage, ratioImage)))
    imageMonde1Test = ImageTk.PhotoImage(Image.open(racine+"assets/images/M1_test.png").resize((ratioImage, ratioImage)))
    imageMonde2Test = ImageTk.PhotoImage(Image.open(racine+"assets/images/M2_test.png").resize((ratioImage, ratioImage)))
    imageMonde3Test = ImageTk.PhotoImage(Image.open(racine+"assets/images/M3_test.png").resize((ratioImage, ratioImage)))
    bgMenu = ImageTk.PhotoImage(Image.open(racine+"assets/images/menu_bg.png").resize((int(largeurFenetre/2+largeurFenetre/4),int(hauteurFenetre/2+hauteurFenetre/4))))
    bgmenuSoloFrame = ImageTk.PhotoImage(Image.open(racine+"assets/images/menu_solo.png").resize((int(largeurFenetre/2+largeurFenetre/4),int(hauteurFenetre/2+hauteurFenetre/4))))
    bgMenuEdition = ImageTk.PhotoImage(Image.open(racine+"assets/images/menu_editeur.png").resize((int(largeurFenetre/2+largeurFenetre/4),int(hauteurFenetre/2+hauteurFenetre/4))))
    imageOK = ImageTk.PhotoImage(Image.open(racine+"assets/images/ok.png").resize((ratioImage, ratioImage)))
    imageInfoBouton = ImageTk.PhotoImage(Image.open(racine+"assets/images/info_bouton.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurFinish = ImageTk.PhotoImage(Image.open(racine+"assets/images/bouton_bloc_finish.png").resize((ratioImage, ratioImage)))
    bgmenuresultat = ImageTk.PhotoImage(Image.open(racine+"assets/images/menu_result.png").resize((int(largeurFenetre/2+largeurFenetre/4),int(hauteurFenetre/2+hauteurFenetre/4))))
    bgMenuMAJ = ImageTk.PhotoImage(Image.open(racine+"assets/images/menu_patch_notes.png").resize((int(largeurFenetre/2+largeurFenetre/4),int(hauteurFenetre/2+hauteurFenetre/4))))
    bgMenuCredit = ImageTk.PhotoImage(Image.open(racine+"assets/images/menu_credit.png").resize((int(largeurFenetre/2+largeurFenetre/4),int(hauteurFenetre/2+hauteurFenetre/4))))
    lienIconeFenetre = racine+"assets/images/icone.ico"

    nombrePixel = largeurFenetre/nombreCase #nombrePixel = nombre de pixels par case sur l'écran (en fonction de la résolution de l'écran, le nombre de pixel change pour toujours avoir le même nombre de case à l'écran)
    nombreCaseX = round(largeurFenetre/nombrePixel) #Le nombre de case en X permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en X
    nombreCaseY = round(hauteurFenetre/nombrePixel) #Le nombre de case en Y permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en Y

    init_keys(fenetre) #Appel la fonction des binds
    menu_principal() #Appe la fonction menu (affichage du main menu)

    with open(racine+"assets/patch_notes.txt", "r") as patchnote:
        patchNotesTexte = patchnote.read()
    with open(racine+"assets/credit.txt", "r") as credit:
        creditTexte = credit.read()


    fenetre.iconbitmap(lienIconeFenetre)
    canevas.pack()
    fenetre.mainloop()

def init_dossiers_et_fichiers(racine):
    dossier_data = racine + "assets/data/"
    dossier_editeur = dossier_data + "editeur/"
    dossier_test_editeur = dossier_data + "test_editeur/"
    dossier_solo = dossier_data + "solo/"
    dossier_origine = dossier_data + "origine/"
    testEtCreeDossier(dossier_data)
    testEtCreeDossier(dossier_editeur)
    testEtCreeDossier(dossier_test_editeur)
    testEtCreeDossier(dossier_solo)
    testEtCreeDossier(dossier_origine)

    fichier_editeur_monde1 = dossier_editeur + "monde1.gac"
    fichier_editeur_monde2 = dossier_editeur + "monde2.gac"
    fichier_editeur_monde3 = dossier_editeur + "monde3.gac"
    testEtCreeFichier(fichier_editeur_monde1)
    testEtCreeFichier(fichier_editeur_monde2)
    testEtCreeFichier(fichier_editeur_monde3)

    fichier_origine_monde1 = dossier_origine + "monde1.gac"
    fichier_origine_monde2 = dossier_origine + "monde2.gac"
    fichier_origine_monde3 = dossier_origine + "monde3.gac"
    testEtCreeFichier(fichier_origine_monde1)
    testEtCreeFichier(fichier_origine_monde2)
    testEtCreeFichier(fichier_origine_monde3)

def testEtCreeDossier(chemin):
    if not os.path.exists(chemin):os.mkdir(chemin)

def testEtCreeFichier(chemin):
    if not os.path.exists(chemin):
        with open(chemin, "wb") as fichierMonde:
            pickle.dump(monde, fichierMonde)

def init_keys(f): #Les Binds
    #Binds direction
    """f.bind("<Key-z>", lambda event : mouvement_joueur ("up"))
    f.bind("<Key-s>", lambda event : mouvement_joueur ("down"))
    f.bind("<Key-q>", lambda event : mouvement_joueur ("left"))
    f.bind("<Key-d>", lambda event : mouvement_joueur ("right"))

    f.bind("<Key-Z>", lambda event : mouvement_joueur ("up"))
    f.bind("<Key-S>", lambda event : mouvement_joueur ("down"))
    f.bind("<Key-Q>", lambda event : mouvement_joueur ("left"))
    f.bind("<Key-D>", lambda event : mouvement_joueur ("right"))

    f.bind("<Key-Up>", lambda event : mouvement_joueur ("up"))
    f.bind("<Key-Down>", lambda event : mouvement_joueur ("down"))
    f.bind("<Key-Left>", lambda event : mouvement_joueur ("left"))
    f.bind("<Key-Right>", lambda event : mouvement_joueur ("right"))"""

    f.bind('<Key>', lambda k: on_key_pressed(k))
    f.bind('<KeyRelease>', lambda k: on_key_released(k))

    #Bind retour
    f.bind("<Escape>", lambda event : exit_key())

    #Bind clic gauche
    f.bind("<B1-Motion>", lambda event : clic_gauche(event))
    f.bind("<Button-1>", lambda event : clic_gauche(event))

    #Bind molette
    f.bind("<Button-2>", lambda event : del_last_bloc())
    f.bind("<MouseWheel>", lambda event : del_last_bloc())


################################################################### Foncitons des menus ###################################################################

def menu_principal():
    global menuPrincipalFrame, etatJeu
    etatJeu="menuPrincipal"
    menuPrincipalFrame = Frame(fenetre, width=largeurFenetre/2+largeurFenetre/4, height=hauteurFenetre/2+hauteurFenetre/4 ,bg='black')
    menuPrincipalFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

    fondMenu = Label(menuPrincipalFrame, image=bgMenu)
    fondMenu.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonSolo = Button(menuPrincipalFrame, image=imageBoutonSolo, relief='groove', bd=0, bg='black', command=menu_solo)
    boutonSolo.place(x=(largeurFenetre/2+largeurFenetre/4)/2-((largeurFenetre/2+largeurFenetre/4)/2)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonEditeur = Button(menuPrincipalFrame, image=imageBoutonEditeur, relief='groove', bd=0, bg='black', command=menu_edition)
    boutonEditeur.place(x=(largeurFenetre/2+largeurFenetre/4)/2+((largeurFenetre/2+largeurFenetre/4)/2)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonMAJ = Button(menuPrincipalFrame, image=imageInfoBouton, relief='groove', bd=0, bg='black', command=menu_note_maj)
    boutonMAJ.place(x=(largeurFenetre/2+largeurFenetre/4)-ratioImage*2, y=(hauteurFenetre/2+hauteurFenetre/4)-ratioImage*2, anchor=CENTER)

    boutonExit = Button(menuPrincipalFrame, image=imageExit, relief='groove', bd=0, bg='black', command=exit_menu)
    boutonExit.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonCredit = Button(menuPrincipalFrame, image=imageInfoBouton, relief='groove', bd=0, bg='black', command=menu_credit)
    boutonCredit.place(x=ratioImage*2, y=(hauteurFenetre/2+hauteurFenetre/4)-ratioImage*2, anchor=CENTER)

    Label(menuPrincipalFrame, text="Version 0.3", font=("Noto Mono", int(12*ratioFenetre)), bg='black', fg='white').place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)-10, anchor=CENTER)

def menu_edition():
    global menuEditionFrame,etatJeu, boutonEditeurMonde1, boutonEditeurMonde2, boutonEditeurMonde3, boutonExitEdit, boutonEditPlayTest
    etatJeu="menuEdition"

    menuEditionFrame = Frame(fenetre, width=largeurFenetre/2+largeurFenetre/4, height=hauteurFenetre/2+hauteurFenetre/4 ,bg='black')
    menuEditionFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

    fondMenuEdition = Label(menuEditionFrame, image=bgMenuEdition)
    fondMenuEdition.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonExitEdit = Button(menuEditionFrame, image=imageExit, relief='groove', bd=0, bg='black', command=exitCommand)
    boutonExitEdit.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonEditeurMonde1 = Button(menuEditionFrame, image=imageMonde1, relief='groove', bd=0, bg='black', command=lambda:commandMondeEditeur(1))
    boutonEditeurMonde1.place(x=(largeurFenetre/2+largeurFenetre/4)/2-((largeurFenetre/2+largeurFenetre/4)/2)/4, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonEditeurMonde2 = Button(menuEditionFrame, image=imageMonde2, relief='groove', bd=0, bg='black', command=lambda:commandMondeEditeur(2))
    boutonEditeurMonde2.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/1.37, anchor=CENTER)

    boutonEditeurMonde3 = Button(menuEditionFrame, image=imageMonde3, relief='groove', bd=0, bg='black', command=lambda:commandMondeEditeur(3))
    boutonEditeurMonde3.place(x=(largeurFenetre/2+largeurFenetre/4)/2+((largeurFenetre/2+largeurFenetre/4)/2)/4, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonEditPlayTest = Button(menuEditionFrame, image=imageBoutonPlayTest, relief='groove', bd=0, bg='black', command=toggle_test_editeur)
    boutonEditPlayTest.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)-(hauteurFenetre/2+hauteurFenetre/4)/1.37, anchor=CENTER)

    boutonEditeurInfo = Button(menuEditionFrame, image=imageBoutonEditeurInfos, relief='groove', bd=0, bg='black', command=info_editeur)
    boutonEditeurInfo.place(x=(largeurFenetre/2+largeurFenetre/4)-ratioImage*2, y=ratioImage*2, anchor=CENTER)

def menu_solo():
    global menuSoloFrame,etatJeu, boutonSoloMonde1, boutonSoloMonde2, boutonSoloMonde3, boutonExitSolo, boutonSoloReset
    etatJeu="menuSolo"

    menuSoloFrame = Frame(fenetre, width=largeurFenetre/2+largeurFenetre/4, height=hauteurFenetre/2+hauteurFenetre/4 ,bg='black')
    menuSoloFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

    fondmenuSoloFrame = Label(menuSoloFrame, image=bgmenuSoloFrame)
    fondmenuSoloFrame.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonExitSolo = Button(menuSoloFrame, image=imageExit, relief='groove', bd=0, bg='black', command=exitCommand)
    boutonExitSolo.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonSoloMonde1 = Button(menuSoloFrame, image=imageMonde1, relief='groove', bd=0, bg='black', command=lambda:commandMondeSolo(1))
    boutonSoloMonde1.place(x=(largeurFenetre/2+largeurFenetre/4)/2-((largeurFenetre/2+largeurFenetre/4)/2)/4, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonSoloMonde2 = Button(menuSoloFrame, image=imageMonde2, relief='groove', bd=0, bg='black', command=lambda:commandMondeSolo(2))
    boutonSoloMonde2.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/1.37, anchor=CENTER)

    boutonSoloMonde3 = Button(menuSoloFrame, image=imageMonde3, relief='groove', bd=0, bg='black', command=lambda:commandMondeSolo(3))
    boutonSoloMonde3.place(x=(largeurFenetre/2+largeurFenetre/4)/2+((largeurFenetre/2+largeurFenetre/4)/2)/4, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonSoloReset = Button(menuSoloFrame, image=imageResetSolo, relief='groove', bd=0, bg='black', command=toggle_reset)
    boutonSoloReset.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)-(hauteurFenetre/2+hauteurFenetre/4)/1.37, anchor=CENTER)

def menu_resultat():
    global menuResultatFrame

    menuResultatFrame = Frame(fenetre, width=largeurFenetre/2+largeurFenetre/4, height=hauteurFenetre/2+hauteurFenetre/4 ,bg='black')
    menuResultatFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

    Label(menuResultatFrame, image=bgmenuresultat).place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)
    Label(menuResultatFrame, text=("Temps de la Run : "+str(monde["runTime"][id_monde-1])+" s"), font=("Noto Mono", int(30*ratioFenetre)), bg='black', fg='white').place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)
    Label(menuResultatFrame, text=("Meilleur temps : "+str(pbPlayer[id_monde-1])+" s"), font=("Noto Mono", int(30*ratioFenetre)), bg='black', fg='white').place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2+100*ratioFenetre, anchor=CENTER)
    Label(menuResultatFrame, text=(messageScore), font=("Noto Mono", int(30*ratioFenetre)), bg='black', fg='white').place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2-100*ratioFenetre, anchor=CENTER)
    Button(menuResultatFrame, image=imageExit, relief='groove', bd=0, bg='black', command=exit_menu).place(x=(largeurFenetre/2+largeurFenetre/4)/2,y=(hauteurFenetre/2+hauteurFenetre/4)-ratioImage, anchor=CENTER) #boutonEditeurExit

def menu_note_maj():
    global menuNoteMAJFrame, etatJeu
    etatJeu = "menuNoteMAJ"

    menuNoteMAJFrame = Frame(fenetre, width=largeurFenetre/2+largeurFenetre/4, height=hauteurFenetre/2+hauteurFenetre/4 ,bg='black')
    menuNoteMAJFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

    Label(menuNoteMAJFrame, image=bgMenuMAJ).place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)
    Button(menuNoteMAJFrame, image=imageExit, relief='groove', bd=0, bg='black', command=exit_menu).place(x=(largeurFenetre/2+largeurFenetre/4)/2,y=(hauteurFenetre/2+hauteurFenetre/4)-ratioImage, anchor=CENTER) #boutonEditeurExit
    Label(menuNoteMAJFrame, text=patchNotesTexte, font=("Noto Mono", int(24*ratioFenetre)), bg="black", fg="white").place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

def menu_credit():
    global menuNoteCreditFrame, etatJeu
    etatJeu = "menuCredit"

    menuNoteCreditFrame = Frame(fenetre, width=largeurFenetre/2+largeurFenetre/4, height=hauteurFenetre/2+hauteurFenetre/4 ,bg='black')
    menuNoteCreditFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

    Label(menuNoteCreditFrame, image=bgMenuCredit).place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)
    Button(menuNoteCreditFrame, image=imageExit, relief='groove', bd=0, bg='black', command=exit_menu).place(x=(largeurFenetre/2+largeurFenetre/4)/2,y=(hauteurFenetre/2+hauteurFenetre/4)-ratioImage, anchor=CENTER) #boutonEditeurExit
    Label(menuNoteCreditFrame, text=creditTexte, font=("Noto Mono", int(24*ratioFenetre)), bg="black", fg="white").place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

def exit_menu():
    global etatJeu
    match etatJeu:
        case "menuPrincipal": fenetre.destroy()

        case "menuEdition":
            menuEditionFrame.place_forget()
            etatJeu="menuPrincipal"

        case "menuSolo":
            menuSoloFrame.place_forget()
            etatJeu="menuPrincipal"

        case "menuResultat":
            menuResultatFrame.destroy()
            etatJeu="menuSolo"

        case "menuNoteMAJ":
            menuNoteMAJFrame.destroy()
            etatJeu="menuPrincipal"
        
        case "menuCredit":
            menuNoteCreditFrame.destroy()
            etatJeu="menuPrincipal"

        case _: exit_mode()

def exit_mode():
    global etatJeu
    match etatJeu:
        case "editeur": exit_editeur()
        case "solo": exit_solo()
        case "test_editeur": exit_test_editeur()

def close_menu():
    menuPrincipalFrame.place_forget()
    match etatJeu:
        case "editeur": menuEditionFrame.place_forget()
        case "solo": menuSoloFrame.place_forget()
        case "test_editeur": menuEditionFrame.place_forget()


################################################################### Fonctions de lancement des modes ###################################################################

def lancement_editeur(id):
    global id_monde, id_level, etatJeu, fenetre_editeur, message_editeur, numeroNiveau, boutonGomme, textTypeBlocSelect, scrolledIDListe
    etatJeu = "editeur"
    close_menu()
    set_grille_fond()
    id_monde = id
    get_monde(id_monde)
    id_level = [0,0]
    get_niveau(id_level)
    affichage_niveau()

    #Fenetre des infos / boutons
    fenetre_editeur = tk.Toplevel() #Création de la fenetre des fonction/boutons de l'éditeur
    fenetre_editeur.geometry("%dx%d%+d%+d" % (300*ratioFenetre,700*ratioFenetre,50,50)) #taille 1 bouton = taille que tu veux + 3 
    fenetre_editeur.resizable(False,False) #Fenetre non redimentionable
    fenetre_editeur.attributes('-topmost',1) #Fenetre toujours au premier plan
    fenetre_editeur.protocol("WM_DELETE_WINDOW", disable_event) #Fenetre non detruisable manuelement
    fenetre_editeur.config(background='#ffffff')
    fenetre_editeur.iconbitmap(lienIconeFenetre)

    #Création des boutons / texte sur la fenetre de l'éditeur
    Button(fenetre_editeur, image=imageBoutonEditeurTP, relief='groove', bd=0, bg='#ffffff', command=lambda:type_bloc("tp")).place(x=ratioImage/2,y=ratioImage*4+ratioImage/2, anchor=CENTER) #bouton_save
    Button(fenetre_editeur, image=imageBoutonEditeurRetour, relief='groove', bd=0, bg='#ffffff', command=del_last_bloc).place(x=ratioImage+ratioImage/2,y=ratioImage/2, anchor=CENTER) #bouton_retour
    Button(fenetre_editeur, image=imageBoutonEditeurPoubelle, relief='groove', bd=0, bg='#ffffff', command=del_all_blocs).place(x=ratioImage*2+ratioImage/2,y=ratioImage/2, anchor=CENTER) #boutonEditeurPoubelle
    Button(fenetre_editeur, image=imageBoutonEditeurNiveauHaut, relief='groove', bd=0, bg='#ffffff', command=lambda:change_level("up")).place(x=ratioImage+ratioImage/2,y=ratioImage*2+ratioImage/2, anchor=CENTER) #bouton_niveau_up
    Button(fenetre_editeur, image=imageBoutonEditeurNiveauBas, relief='groove', bd=0, bg='#ffffff', command=lambda:change_level("down")).place(x=ratioImage+ratioImage/2,y=ratioImage*4+ratioImage/2, anchor=CENTER) #bouton_niveau_down
    Button(fenetre_editeur, image=imageBoutonEditeurNiveauGauche, relief='groove', bd=0, bg='#ffffff', command=lambda:change_level("left")).place(x=ratioImage/2,y=ratioImage*3+ratioImage/2, anchor=CENTER) #bouton_niveau_left
    Button(fenetre_editeur, image=imageBoutonEditeurNiveauDroite, relief='groove', bd=0, bg='#ffffff', command=lambda:change_level("right")).place(x=ratioImage*2+ratioImage/2,y=ratioImage*3+ratioImage/2, anchor=CENTER) #bouton_niveau_right
    Button(fenetre_editeur, image=imageBoutonEditeurPoubelleMonde, relief='groove', bd=0, bg='#ffffff', command=del_all_level).place(x=ratioImage*2+ratioImage/2,y=ratioImage+ratioImage/2, anchor=CENTER) #boutonEditeurDellAll
    Button(fenetre_editeur, image=imageExit, relief='groove', bd=0, bg='#ffffff', command=exit_editeur).place(x=ratioImage+ratioImage/2,y=ratioImage*5+ratioImage/2, anchor=CENTER) #boutonEditeurExit
    numeroNiveau = Label(fenetre_editeur, text=id_level, font=("Noto Mono", int(24*ratioFenetre)), bg='#ffffff') #Affichage du numéro du niveau actuel
    numeroNiveau.place(x=ratioImage+ratioImage/2,y=ratioImage*3+ratioImage/2, anchor=CENTER) #numeroNiveau
    Button(fenetre_editeur, image=imageBoutonEditeurBlocSolide, relief='groove', bd=0, bg='#ffffff', command=lambda:type_bloc("solide")).place(x=ratioImage/2,y=ratioImage*2+ratioImage/2, anchor=CENTER) #bouton_bloc_solide
    Button(fenetre_editeur, image=imageBoutonEditeurBlocSpawn, relief='groove', bd=0, bg='#ffffff', command=lambda:type_bloc("spawn")).place(x=ratioImage*2+ratioImage/2,y=ratioImage*2+ratioImage/2, anchor=CENTER) #bouton_bloc_spawn
    Button(fenetre_editeur, image=imageBoutonEditeurItemCle, relief='groove', bd=0, bg='#ffffff', command=lambda:type_bloc("key")).place(x=ratioImage/2,y=ratioImage*5+ratioImage/2, anchor=CENTER) #bouton_item_key
    Button(fenetre_editeur, image=imageBoutonEditeurFinish, relief='groove', bd=0, bg='#ffffff', command=lambda:type_bloc("finish")).place(x=ratioImage*2+ratioImage/2,y=ratioImage*4+ratioImage/2, anchor=CENTER) #bouton_bloc_finish
    boutonGomme = Button(fenetre_editeur, image=imageBoutonEditeurGomme, relief='groove', bd=0, bg='#ffffff', command=toggle_gomme)
    boutonGomme.place(x=ratioImage/2,y=ratioImage+ratioImage/2, anchor=CENTER) #bouton_gomme
    Button(fenetre_editeur, image=imageBoutonEditeurBlocPorte, relief='groove', bd=0, bg='#ffffff', command=lambda:type_bloc("porte")).place(x=ratioImage*2+ratioImage/2,y=ratioImage*5+ratioImage/2, anchor=CENTER) #bouton_bloc_port
    Button(fenetre_editeur, image=imageBoutonEditeurEditBloc, relief='groove', bd=0, bg='#ffffff', command=set_edit).place(x=ratioImage+ratioImage/2,y=ratioImage+ratioImage/2, anchor=CENTER) #bouton_edit
    Button(fenetre_editeur, image=imageInfoBouton, relief='groove', bd=0, bg='#ffffff').place(x=ratioImage/2,y=ratioImage/2, anchor=CENTER) #bouton_edit
    message_editeur = Label(fenetre_editeur, text="", font=("Noto Mono", int(25*ratioFenetre)), bg='#ffffff' ) #Affiche du type de bloc / erreur / info général
    message_editeur.place(x=ratioImage+ratioImage/2,y=ratioImage*6+ratioImage/2, anchor=CENTER) #message_editeur

    Label(fenetre_editeur, text="Edit Object", font=("Noto Mono", int(32*ratioFenetre)), bg="white").place(x=ratioImage*2+ratioImage/2+300*ratioFenetre,y=20*ratioFenetre, anchor=CENTER)
    Label(fenetre_editeur, text="Type Bloc : ", font=("Noto Mono", int(24*ratioFenetre)), bg="white").place(x=325*ratioFenetre, y=65*ratioFenetre)
    textTypeBlocSelect = Label(fenetre_editeur, text="None", font=("Noto Mono", int(24*ratioFenetre)), bg="white")
    textTypeBlocSelect.place(x=575*ratioFenetre, y=65*ratioFenetre)

    Label(fenetre_editeur, text="Liste ID", font=("Noto Mono", int(28*ratioFenetre)), bg="white").place(x=ratioImage*2+ratioImage/2+300*ratioFenetre,y=325*ratioFenetre, anchor=CENTER)

    scrolledIDListe = tkinter.scrolledtext.ScrolledText(master = fenetre_editeur,wrap = tk.WORD,width = int(60*ratioFenetre),height = int(20*ratioFenetre), font=(int(14*ratioFenetre)))
    scrolledIDListe.place(x=300*ratioFenetre,y=350*ratioFenetre)

def lancement_solo(id):
    global id_monde, id_level, etatJeu, positionJoueur, joueur, temps
    etatJeu = "solo"
    id_monde = id
    get_monde(id_monde)
    try: id_level = [monde["lastCoords"][id_monde-1][1][0], monde["lastCoords"][id_monde-1][1][1]]
    except:
        id_level = [0,0]
    get_niveau(id_level)
    for bloc in monde["niveaux"][niveau]: #Cherche si un bloc d'apparition du joueur existe dans le niveau [0,0] pour faire aparaitre 
        if bloc["type"] == 1: #Si il existe, les coordonées d'apparition sont mis à jour
            posjxstart = bloc["x"]
            posjystart = bloc["y"]
            break #Quand les coordonnées sont trouver, la boucle s'arrete pour ne pas chercher des coordonnées pour rien
    try:
        posjxstart = monde["lastCoords"][id_monde-1][0][0]
        posjystart = monde["lastCoords"][id_monde-1][0][1]
    except:
        pass
    try:
        posjxstart
        close_menu()
        affichage_niveau()
        temps = 0
        chrono()
        set_direction()
        joueur = canevas.create_rectangle(0, 0, nombrePixel, nombrePixel, fill='blue', width=0) #Création du joueur
        canevas.moveto(joueur,posjxstart*nombrePixel, posjystart*nombrePixel) #Déplacement du joueur au coordonnées d'apparition
        positionJoueur = [posjxstart, posjystart] #0 = x & 1 = y #Actualisation des position du joueur sur la grille
    except:
        etatJeu = "menuSolo"
        tkinter.messagebox.showerror("Erreur", "Il n'y a pas de bloc d'apparition dans ce monde") #Affichage d'un message d'erreur

def lancement_test_edition(id):
    global id_level, etatJeu, joueur, positionJoueur
    etatJeu = "test_editeur"
    originalPath = racine+"assets/data/editeur/monde"+str(id)+".gac" #"originalPath" contient le lien du dossier éditeur
    copyPath = racine+"assets/data/test_editeur/monde"+str(id)+".gac" #"copyPath" contient le lien du dossier test_editeur où vont etre copier les fichier de l'éditeur pour ne pas modifier les fichier dans l'éditeur
    if os.path.exists(copyPath): #Si le dossier contient déjà quelque chose, il est détruit puis recréer 
        shutil.copy(originalPath, copyPath)
    id_monde = id
    get_monde(id_monde)
    id_level = [0,0]
    get_niveau(id_level)
    for bloc in monde["niveaux"][niveau]: #Cherche si un bloc d'apparition du joueur existe dans le niveau [0,0] pour faire aparaitre 
        if bloc["type"] == 1: #Si il existe, les coordonées d'apparition sont mis à jour
            posjxstart = bloc["x"]
            posjystart = bloc["y"]
            break #Quand les coordonnées sont trouver, la boucle s'arrete pour ne pas chercher des coordonnées pour rien
    try:
        posjxstart
        close_menu()
        affichage_niveau()
        joueur = canevas.create_rectangle(0, 0, nombrePixel, nombrePixel, fill='blue', width=0) #Création du joueur
        canevas.move(joueur,posjxstart*nombrePixel, posjystart*nombrePixel) #Déplacement du joueur au coordonnées d'apparition
        positionJoueur = [posjxstart, posjystart] #0 = x & 1 = y #Actualisation des position du joueur sur la grille
    except:
        etatJeu = "menuEdition"
        tkinter.messagebox.showerror("Erreur", "Il n'y a pas de bloc d'apparition dans ce monde") #Affichage d'un message d'erreur

def exit_editeur():
    global etatJeu, etatEditeur
    del_grille_fond()
    save(id_monde)
    cacher_niveau()
    fenetre_editeur.destroy()
    if etatEditeur == "edit":
        etatEditeur = "pose"
    etatJeu="menuEdition"
    menuPrincipalFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)
    menuEditionFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

def exit_solo():
    global etatJeu, monde, toggleMouvement
    calcul_temps()
    #monde["lastCoords"][id_monde-1] = [[int(str(positionJoueur[0])),int(str(positionJoueur[1]))], id_level]
    monde["lastCoords"][id_monde-1] = [[int(str(positionJoueur[0])), int(str(positionJoueur[1]))], [id_level[0], id_level[1]]]
    save(id_monde)
    cacher_niveau()
    fenetre.after_cancel(boucleTemps)
    fenetre.after_cancel(boucleDirection)
    menuPrincipalFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)
    menuSoloFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)
    canevas.delete(joueur)
    etatJeu = "menuSolo"
    if toggleMouvement:
        toggleMouvement = False
        fenetre.after_cancel(boubleMouvement)
    positionJoueur.clear()

def exit_test_editeur():
    global etatJeu
    save(id_monde)
    cacher_niveau()
    etatJeu="menuEdition"
    menuPrincipalFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)
    menuEditionFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)
    canevas.delete(joueur)
    positionJoueur.clear()

################################################################### Fonctions du mode édition ###################################################################

def type_bloc(tBloc):
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

    elif tBloc == "tp":
        typeDuBloc = 4
        couleurBloc = 'white'
        message_editeur.config(text="Bloc TP")
    
    elif tBloc == "finish":
        typeDuBloc = 5
        couleurBloc = 'red'
        message_editeur.config(text="Bloc de fin")

def clic_gauche (event):
    if etatJeu == "editeur":
        xSourisGrille,ySourisGrille=event.x,event.y

        xSourisGrille = (xSourisGrille/nombrePixel)
        xSourisGrille = int(xSourisGrille)

        ySourisGrille = (ySourisGrille/nombrePixel)
        ySourisGrille = int(ySourisGrille)

        match etatEditeur:
            case "pose": pose_bloc(xSourisGrille,ySourisGrille)
            case "gomme": gomme(xSourisGrille,ySourisGrille)
            case "edit": edit_bloc(xSourisGrille,ySourisGrille)

def pose_bloc(x,y):
    global monde
    indexBloc = 0
    for bloc in monde["niveaux"][niveau]:
        if bloc["x"] == x and bloc ["y"] == y:
            return
        if bloc["type"] == 1 and typeDuBloc == 1 or bloc["type"] == 5 and typeDuBloc == 5:
            canevas.delete(bloc["idTk"])
            del monde["niveaux"][niveau][indexBloc]
        indexBloc += 1
    demiPixel = 0
    if typeDuBloc == 2:
        demiPixel = nombrePixel/4
    monde["niveaux"][niveau].append({"idAssoc" : 0, "idTk":canevas.create_rectangle(x*nombrePixel+demiPixel, y*nombrePixel+demiPixel, x*nombrePixel+nombrePixel-demiPixel, y*nombrePixel+nombrePixel-demiPixel, fill=couleurBloc), "x":x, "y":y, "type":typeDuBloc, "couleur":couleurBloc, "collect":0})
    save(id_monde)

def del_last_bloc():
    global monde
    if etatJeu == "editeur" and len(monde["niveaux"][niveau]) > 0:
        canevas.delete(monde["niveaux"][niveau][-1]["idTk"])
        del monde["niveaux"][niveau][-1]
        save(id_monde)

def del_all_blocs():
    global monde
    cacher_niveau()
    monde["niveaux"][niveau] = list()
    save(id_monde)

def del_all_level():
    global monde, id_level
    attention = tkinter.messagebox.askyesno("Attention", "Voulez vous détruire tout les blocs de ce niveau ?")
    if attention:
        cacher_niveau()
        for niveauTest in monde["niveaux"]:
            monde["niveaux"][niveauTest].clear()
        id_level = [0,0]
        save(id_monde)

def toggle_gomme():
    global etatEditeur, boutonGomme
    if etatEditeur != "gomme" and etatEditeur != "edit":
        etatEditeur = "gomme"
        boutonGomme.configure(image = imageBoutonEditeurGommeSelect)
    elif etatEditeur == "gomme":
        etatEditeur = "pose"
        boutonGomme.configure(image = imageBoutonEditeurGomme)

def gomme(x,y):
    if etatJeu == "editeur":
        indexBloc = 0
        for bloc in monde["niveaux"][niveau]:
            if bloc["x"] == x and bloc["y"] == y:
                canevas.delete(bloc["idTk"])
                del monde["niveaux"][niveau][indexBloc]
                break
            indexBloc += 1

def set_edit():
    global etatEditeur
    if etatEditeur == "pose":
        etatEditeur = "edit"
        fenetre_editeur.geometry("%dx%d" % (800*ratioFenetre,700*ratioFenetre))

    elif etatEditeur == "edit":
        etatEditeur = "pose"
        fenetre_editeur.geometry("%dx%d" % (300*ratioFenetre,700*ratioFenetre))

def edit_bloc(x,y):
    global selectBloc, selectNiveau
    for bloc in monde["niveaux"][niveau]:
        if bloc["x"] == x and bloc["y"] == y:
            selectNiveau = niveau
            selectBloc = bloc
            match bloc["type"]:
                case 0:
                    textTypeBlocSelect.config(text="Bloc Solide")
                    config_edit(0)
                case 1:
                    textTypeBlocSelect.config(text="Bloc Spawn")
                    config_edit(1)
                case 2:
                    textTypeBlocSelect.config(text="Item Clé")
                    config_edit(2)
                case 3:
                    textTypeBlocSelect.config(text="Bloc Porte")
                    config_edit(3)
                case 4:
                    textTypeBlocSelect.config(text="Bloc TP")
                    config_edit(4)
                case 5: textTypeBlocSelect.config(text="Bloc de fin")
            break

def config_edit(typeB):
    global entryIDcle,boutonIDCleValidation,couleurSet,textIDKey,textIDTP1,textIDTP2,entryID1,entryID2,boutonIDTPValidation, textTypeBlocSelect, scrolledIDListe, listeIDUsed
    try:
        entryIDcle.destroy()
        boutonIDCleValidation.destroy()
        couleurSet.destroy()
        textIDKey.destroy()
    except:
        pass
    try:
        textIDTP1.destroy()
        textIDTP2.destroy()
        entryID1.destroy()
        entryID2.destroy()
        boutonIDTPValidation.destroy()
    except:
        pass

    if typeB == 2 or typeB == 3:
        entryIDcle = Entry(fenetre_editeur, bg="lightgrey", width=int(10*ratioFenetre), font=("Noto Mono", int(24*ratioFenetre)))
        entryIDcle.place(x=575*ratioFenetre, y=110*ratioFenetre)
        boutonIDCleValidation = Button(fenetre_editeur, image=imageOK, relief='groove', bd=0, bg='black', command=lambda:get_key(str(entryIDcle.get())))
        boutonIDCleValidation.place(x=325*ratioFenetre,y=175*ratioFenetre)
        textIDKey = Label(fenetre_editeur, text="ID :", font=("Noto Mono", int(24*ratioFenetre)), bg="white")
        textIDKey.place(x=430*ratioFenetre,y=110*ratioFenetre) 
        couleurSet = Scale(fenetre_editeur, orient='horizontal', from_=1, to=7, resolution=1, tickinterval=2, length=180*ratioFenetre, label='Couleur', font=("Noto Mono", int(10*ratioFenetre)), bg="white", command=change_color)
        couleurSet.place(x=575*ratioFenetre,y=150*ratioFenetre)
    elif typeB == 4:
        textIDTP1 = Label(fenetre_editeur, text="ID départ", font=("Noto Mono", int(24*ratioFenetre)), bg="white")
        textIDTP1.place(x=400*ratioFenetre,y=130*ratioFenetre,anchor=CENTER)
        textIDTP2 = Label(fenetre_editeur, text="ID arrivée", font=("Noto Mono", int(24*ratioFenetre)), bg="white")
        textIDTP2.place(x=700*ratioFenetre,y=130*ratioFenetre,anchor=CENTER)
        entryID1 = Entry(fenetre_editeur, bg="lightgrey", width=int(10*ratioFenetre), font=("Noto Mono", int(24*ratioFenetre)))
        entryID1.place(x=400*ratioFenetre, y=210*ratioFenetre,anchor=CENTER)
        entryID2 = Entry(fenetre_editeur, bg="lightgrey", width=int(10*ratioFenetre), font=("Noto Mono", int(24*ratioFenetre)))
        entryID2.place(x=700*ratioFenetre, y=210*ratioFenetre,anchor=CENTER)
        boutonIDTPValidation = Button(fenetre_editeur, image=imageOK, relief='groove', bd=0, bg='black', command=lambda:get_tp([int(entryID1.get()),int(entryID2.get())]))
        boutonIDTPValidation.place(x=550*ratioFenetre,y=240*ratioFenetre,anchor=CENTER)
    calcul_id_utilise()
    scrolledIDListe.delete("1.0","end")
    for i in range(len(listeIDUsed)):
        scrolledIDListe.insert(tk.INSERT,"ID bloc : "+str(listeIDUsed[i]["idAssoc"])+", Type : "+str(listeIDUsed[i]["type"])+", Couleur : "+str(listeIDUsed[i]["couleur"])+", ID niveau : "+str(listeLevelIDUsed[i])+"\n", listeIDUsed[i]["couleur"])
        colorTextID = listeIDUsed[i]["couleur"]
        if colorTextID == "white":
            colorTextID = "black"
        scrolledIDListe.tag_config(listeIDUsed[i]["couleur"], foreground=colorTextID)

def get_key(id):
    global monde
    indexBloc = 0
    for bloc in monde["niveaux"][niveau]:
        if bloc["x"] == selectBloc["x"] and bloc["y"] == selectBloc["y"]:
            monde["niveaux"][niveau][indexBloc]["idAssoc"] = id
        indexBloc += 1

def get_tp(id):
    global monde
    indexBloc = 0
    for bloc in monde["niveaux"][niveau]:
        if bloc["x"] == selectBloc["x"] and bloc["y"] == selectBloc["y"]:
            monde["niveaux"][niveau][indexBloc]["idAssoc"] = id
        indexBloc += 1

def change_color(c): #Change la couleur du bloc selectionner
    global monde
    match couleurSet.get():
        case 1: newColorBloc = 'orange'
        case 2: newColorBloc = 'yellow'
        case 3: newColorBloc = 'green'
        case 4: newColorBloc = 'blue'
        case 5: newColorBloc = 'pink'
        case 6: newColorBloc = 'purple'
        case 7: newColorBloc = 'brown'

    indexBloc = 0
    for bloc in monde["niveaux"][niveau]:
        if bloc["x"] == selectBloc["x"] and bloc["y"] == selectBloc["y"]:
            monde["niveaux"][niveau][indexBloc]["couleur"] = newColorBloc
            canevas.itemconfig(bloc["idTk"], fill=bloc["couleur"])
            save(id_monde)
            break
        indexBloc += 1

def calcul_id_utilise():
    global listeIDUsed, listeLevelIDUsed
    listeIDUsed = []
    listeLevelIDUsed = []
    for niveauTest in monde["niveaux"]:
        for bloc in monde["niveaux"][niveauTest]:
            if bloc["type"] == 2 or bloc["type"] == 3 or bloc["type"] == 4:
                listeIDUsed.append(bloc)
                listeLevelIDUsed.append(niveauTest)


################################################################### Fonctions du Solo ###################################################################

def on_key_pressed(k):
    global theKey
    theKey = k.char

def on_key_released(k):
    global toggleMouvement, theKey
    if etatJeu == "solo" or etatJeu == "test_editeur":
        if k.char == theKey:
            theKey = ""
            toggleMouvement = False
            fenetre.after_cancel(boubleMouvement)

def set_direction():
    global direction_mouvement, toggleMouvement, boucleDirection
    if etatJeu == "solo" or etatJeu == "test_editeur":
        direction_mouvement = directionsBinds.get(theKey)
        if not toggleMouvement:
            if directionsBinds.get(theKey) is not None:
                toggleMouvement = True
                mouvement_joueur()
        boucleDirection = fenetre.after(1, set_direction)

def mouvement_joueur():
    global positionJoueur, joueur, id_level, boubleMouvement
    if direction_mouvement == "up": #Si la direction est egale à "up"
        posJTestX = positionJoueur[0] #Test de la prochaine position du joueur dans la grille pour x
        posJTestY = positionJoueur[1]-1 #Test de la prochaine position du joueur dans la grille pour y
        xyJ = 1 #Indique quel est l'axe qui est demander (0=x et 1=y)
        posJF = -1 #Donne de combien doit être changer les coordonnées du joueur en fonction de l'axe
        posMax = 0 #Donne la position max du joueur sur la grille 
        deplacement = [0, -nombrePixel] #Donne de combien le joueur doit ce déplacer sur la grille
        tp = [positionJoueur[0],nombreCaseY-1]

    elif direction_mouvement == "down":
        posJTestX = positionJoueur[0]
        posJTestY = positionJoueur[1]+1
        xyJ = 1
        posJF = +1
        posMax = nombreCaseY-1
        deplacement = [0, +nombrePixel]
        tp = [positionJoueur[0],0]

    elif direction_mouvement == "left":
        posJTestX = positionJoueur[0]-1
        posJTestY = positionJoueur[1]
        xyJ = 0
        posJF = -1
        posMax = 0
        deplacement = [-nombrePixel, 0]
        tp = [nombreCaseX-1,positionJoueur[1]]

    elif direction_mouvement == "right":
        posJTestX = positionJoueur[0]+1
        posJTestY = positionJoueur[1]
        xyJ = 0
        posJF = +1
        posMax = nombreCaseX-1
        deplacement = [+nombrePixel, 0]
        tp = [0,positionJoueur[1]]
    else: return

    indexBloc = 0
    ok = True
    for bloc in monde["niveaux"][niveau]:
        if bloc["x"] == posJTestX and bloc["y"] == posJTestY:
            if bloc["type"] == 0:
                ok = False

            elif bloc["type"] == 2 and bloc["collect"] == 0:
                ramasse_cle(indexBloc)

            elif bloc["type"] == 3:
                ok = ouvre_porte(indexBloc)

            elif bloc["type"] == 4:
                tp_joueur(indexBloc)
            
            elif bloc["type"] == 5:
                fin_niveau()
                return
        indexBloc += 1

    if ok == True:
        if positionJoueur[xyJ] == posMax: #Si la position du joueur est egale à la limite de l'écran (ou de la map)
            id_level[xyJ] = id_level[xyJ]+int(posJF)
            cacher_niveau()
            get_niveau(id_level) #La fonction level_search est appeler
            affichage_niveau()
            positionJoueur = tp
            canevas.moveto(joueur,tp[0]*nombrePixel,tp[1]*nombrePixel)
        else:
            canevas.move(joueur, deplacement[0], deplacement[1]) #Le joueur est déplacer sur la case demander
            positionJoueur[xyJ] = positionJoueur[xyJ]+posJF #Les coordonnées du joueur sont actualiser
    boubleMouvement = fenetre.after(45, mouvement_joueur)

def ramasse_cle(indexBloc):
    global monde
    monde["niveaux"][niveau][indexBloc]["collect"] = 1
    canevas.delete(monde["niveaux"][niveau][indexBloc]["idTk"])

def ouvre_porte(indexBloc):
    global monde
    for niveauTest in monde["niveaux"]:
        for bloc in monde["niveaux"][niveauTest]:
            if bloc["type"] == 2 and bloc["collect"] == 1 and bloc["idAssoc"] == monde["niveaux"][niveau][indexBloc]["idAssoc"]:
                monde["niveaux"][niveau][indexBloc]["collect"] = 1
                canevas.delete(monde["niveaux"][niveau][indexBloc]["idTk"])
                return True

    return False

def tp_joueur(indexBloc):
    global id_level, positionJoueur
    for niveauTest in monde["niveaux"]:
        for bloc in monde["niveaux"][niveauTest]:
            if bloc["type"] == 4:
                try:
                    if bloc["idAssoc"][0] == monde["niveaux"][niveau][indexBloc]["idAssoc"][1]:
                        get_list_niveau(niveauTest)
                        cacher_niveau()
                        get_niveau(id_level) #La fonction get_niveau est appeler
                        affichage_niveau()
                        positionJoueur = [bloc["x"],bloc["y"]]
                        canevas.moveto(joueur,positionJoueur[0]*nombrePixel,positionJoueur[1]*nombrePixel)
                        return
                except: return

def fin_niveau():
    global monde, etatJeu, messageScore
    if etatJeu == "solo":
        exit_solo()
        etatJeu = "solo"
        if monde["reset"][id_monde-1]: #Si le reset du niveau à été effectuer
            if pbPlayer[id_monde-1] == 0 or monde["runTime"][id_monde-1] < pbPlayer[id_monde-1]:
                pbPlayer[id_monde-1] = monde["runTime"][id_monde-1]
                messageScore = "Nouveau Score"
            else: messageScore = ""
        else: messageScore = "Ce niveau doit être réinitialisé pour sauvegarder un nouveau score"
        menu_resultat()
        monde["runTime"][id_monde-1] = 0
        monde["reset"][id_monde-1] = False
        save(id_monde)
        etatJeu = "menuResultat"
        with open(racine+"assets/data/origine/pb_Joueur.gac", "wb") as fichierMonde:
            pickle.dump(pbPlayer, fichierMonde)
        print(monde["lastCoords"])

def chrono():
    global temps, boucleTemps
    temps += 1
    boucleTemps = fenetre.after(1000, chrono)

def calcul_temps():
    global monde
    fenetre.after_cancel(boucleTemps)
    monde["runTime"][id_monde-1] += temps


################################################################### Fonctions du fonctionnement global du programme ###################################################################

def disable_event(): #Disable
    pass

def exit_key(): #Permet des retour au menu avec la touche "echap"
    exit_menu()

def info_editeur(): #Fenêtre d'infos des action possible
    webbrowser.open(racine+"assets/Guide_editeur.pdf")

def get_niveau(id): #Permet de tourver le niveau à charger
    global niveau, monde
    id_level_str = [str(i) for i in id_level]
    id_str = ",".join(id_level_str)
    for niveau in monde["niveaux"]:
        if niveau==id_str: break
    else:
        niveau = id_str
        monde["niveaux"][niveau] = list()
    print(monde["lastCoords"])

def get_monde(id): #Permet de tourver le monde à chargerf
    global monde
    dossier_data = racine + "assets/data/"
    match etatJeu:
        case "editeur": dossier = dossier_data + "editeur/monde"+str(id)+".gac"
        case "solo": dossier = dossier_data + "solo/monde"+str(id)+".gac"
        case "test_editeur": dossier = dossier_data + "test_editeur/monde"+str(id)+".gac"
    with open(dossier, "rb") as fichierMonde:
        monde = pickle.load(fichierMonde)

def get_list_niveau(niveauTest):
    global id_level
    id_level = [int(niveauTest.split(",")[0]),int(niveauTest.split(",")[1])]

def set_grille_fond(): #Affiche la grille de l'éditeur
    ######################################################################## Le cadirage
    ligneCreer_x = nombrePixel #Variable qui renseigne à quel x les lignes du cadriage doivent être placer
    ligneCreer_y = nombrePixel #Variable qui renseigne à quel y les lignes du cadriage doivent être placer

    #Création des ligne de l'éditeur (le cadriage dans le fond qui permet de mieux savoir où les blocs seront placer)
    while ligneCreer_x <= largeurFenetre: #Temps que la bordure de l'écran n'est pas attein les lignes sont placer
        ligneX.append(canevas.create_line(ligneCreer_x, 0, ligneCreer_x, hauteurFenetre)) #Crée une ligne vertical en fonction de "ligneCreer_x"
        ligneCreer_x += nombrePixel #Ajout du nombre de pixel n'esaissaire entre 2 ligne (la taille d'un bloc)

    while ligneCreer_y <= hauteurFenetre: #Temps que la bordure de l'écran n'est pas attein les lignes sont placer
        ligneY.append(canevas.create_line(0, ligneCreer_y, largeurFenetre, ligneCreer_y)) #Crée une ligne horizontal en fonction de "ligneCreer_y"
        ligneCreer_y += nombrePixel #Ajout du nombre de pixel n'esaissaire entre 2 ligne (la taille d'un bloc)

def del_grille_fond(): #Masque la grille de l'éditeur
    for ligne in ligneX:
        canevas.delete(ligne)
    ligneX.clear()
    for ligne in ligneY:
        canevas.delete(ligne)
    ligneY.clear()

def affichage_niveau(): #Affiche le niveau selectionner
    global monde
    indexBloc = 0
    for bloc in monde["niveaux"][niveau]:
        couleurBloc = bloc["couleur"]
        demiPixel = 0
        if bloc["type"] == 2:
            demiPixel = nombrePixel/4
        if bloc["collect"] == 0:
            monde["niveaux"][niveau][indexBloc]["idTk"] = (canevas.create_rectangle(bloc["x"]*nombrePixel+demiPixel, bloc["y"]*nombrePixel+demiPixel, bloc["x"]*nombrePixel+nombrePixel-demiPixel, bloc["y"]*nombrePixel+nombrePixel-demiPixel, fill=couleurBloc))
        indexBloc += 1
    couleurBloc = 'black'

def cacher_niveau(): #Masque le niveau
    for bloc in monde["niveaux"][niveau]:
        canevas.delete(bloc["idTk"])

def supp_niveau():
    global monde
    del monde["niveaux"][niveau]

def save(id):
    global monde
    dossier_data = racine + "assets/data/"
    match etatJeu:
        case "editeur": dossier = dossier_data + "editeur/monde"+str(id)+".gac"
        case "solo": dossier = dossier_data + "solo/monde"+str(id)+".gac"
        case "test_editeur": dossier = dossier_data + "test_editeur/monde"+str(id)+".gac"
    with open(dossier, "wb") as fichierMonde:
        pickle.dump(monde, fichierMonde)

def change_level(direction):
    global id_level, numeroNiveau
    cacher_niveau()
    match direction:
        case "up": id_level[1] -= 1
        case "down": id_level[1] += 1
        case "left": id_level[0] -= 1
        case "right": id_level[0] += 1
    get_niveau(id_level)
    affichage_niveau()
    numeroNiveau.config(text=id_level)

def toggle_reset():
    global boutonSoloMonde1, boutonSoloMonde2, boutonSoloMonde3, commandMondeSolo, exitCommand, boutonExitSolo
    if commandMondeSolo != reset_solo:
        commandMondeSolo = reset_solo
        exitCommand = ""
        boutonSoloMonde1.config(image=imageMonde1Del)
        boutonSoloMonde2.config(image=imageMonde2Del)
        boutonSoloMonde3.config(image=imageMonde3Del)
        boutonSoloReset.config(image=imageResetSoloToggle)
        boutonExitSolo.config(image=imageNotExit, command=exitCommand)
    else:
        commandMondeSolo = lancement_solo
        exitCommand = exit_menu
        boutonSoloMonde1.config(image=imageMonde1)
        boutonSoloMonde2.config(image=imageMonde2)
        boutonSoloMonde3.config(image=imageMonde3)
        boutonSoloReset.config(image=imageResetSolo)
        boutonExitSolo.config(image=imageExit, command=exitCommand)

def reset_solo(n):
    global monde
    attention = tkinter.messagebox.askyesno("Attention", "Voulez-vous réinitialisez se monde ?")
    if attention:
        originalPath = racine+"assets/data/origine/monde"+str(n)+".gac"
        copyPath = racine+"assets/data/solo/monde"+str(n)+".gac"
        shutil.copy(originalPath, copyPath)
        monde["reset"][n-1] = True
        toggle_reset()

def toggle_test_editeur():
    global boutonEditeurMonde1, boutonSoloMonde2, boutonSoloMonde3, commandMondeEditeur, exitCommand, boutonExitEdit
    if commandMondeEditeur != lancement_test_edition:
        commandMondeEditeur = lancement_test_edition
        exitCommand = ""
        boutonEditeurMonde1.config(image=imageMonde1Test)
        boutonEditeurMonde2.config(image=imageMonde2Test)
        boutonEditeurMonde3.config(image=imageMonde3Test)
        boutonEditPlayTest.config(image=imageBoutonPlayTestToggle)
        boutonExitEdit.config(image=imageNotExitTest, command=exitCommand)
    else:
        commandMondeEditeur = lancement_editeur
        exitCommand = exit_menu
        boutonEditeurMonde1.config(image=imageMonde1)
        boutonEditeurMonde2.config(image=imageMonde2)
        boutonEditeurMonde3.config(image=imageMonde3)
        boutonEditPlayTest.config(image=imageBoutonPlayTest)
        boutonExitEdit.config(image=imageExit, command=exitCommand)

def wip():
    tkinter.messagebox.showinfo("WIP", "Work In Progress")


################################################################### Autre ###################################################################
start()


"""

"""