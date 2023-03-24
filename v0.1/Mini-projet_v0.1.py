#Import des bibliothèques
import tkinter as tk, tkinter.messagebox; from tkinter import *; import pickle, os, shutil, webbrowser
try:
    from PIL import Image, ImageTk
except:
    os.system('pip install Pillow')
from PIL import Image, ImageTk


################################################################### Les fonctions de mise en place du programme ###################################################################

def start(): #La fonction "start" permet de déclaré la plus part des variable global
    global monde, fenetre, etatEditeur, nombrePixel, largeurFenetre, hauteurFenetre, canevas, etatJeu, nombreCaseY, nombreCaseX, editBloc, racine, imageBoutonPlayTest, bgMenu, imageOK, imageInfoBouton, tailleImage, ratioImage, bgmenuSoloFrame, ratioFenetre, bgMenuEdition, nombreCase, imageBoutonEditeurGommeSelect, imageBoutonEditeurGomme, imageBoutonEditeurPoubelleMonde, imageBoutonEditeurBlocPorte, editTest, imageMonde1, imageMonde2, imageMonde3, imageResetSolo, imageBoutonEditeurItemCle, imageBoutonEditeurEditBloc, newColorBloc, fenetreeditTest, id_level, imageBoutonSolo, imageBoutonEditeur, ligneX, ligneY, imageBoutonEditeurNiveauHaut, imageBoutonEditeurNiveauBas, imageBoutonEditeurNiveauGauche, imageBoutonEditeurNiveauDroite, imageBoutonEditeurTP, imageBoutonEditeurRetour, imageWIP, imageBoutonEditeurPoubelle, imageBoutonEditeurExit, imageBoutonEditeurBlocSolide, couleurBloc, typeDuBloc, imageBoutonEditeurBlocSpawn, editGomme, id_monde, imageBoutonEditeurInfos

    ################################################################### Mise en place de la fenetre et du canevas

    fenetre = Tk()

    largeurFenetre = fenetre.winfo_screenwidth()
    hauteurFenetre = fenetre.winfo_screenheight()

    fenetre.title("Game & Cube")
    fenetre.attributes('-fullscreen', True)
    canevas = Canvas(fenetre, width=largeurFenetre, height=hauteurFenetre,bg='#3b3b3b')


    """monde={
        "00":[
                    {"idAssoc" : 0, "idTk":0, "x":0, "y":0, "type":0, "couleur":"black", "collect":0},
                    {"idAssoc" : 0, "idTk":0, "x":1, "y":0, "type":2, "couleur":"blue", "collect":0},
                    {"idAssoc" : 0, "idTk":0, "x":1, "y":1, "type":4, "couleur":"red", "collect":0}
            ],

        "01":[
                    {"idAssoc" : 0, "idTk":0, "x":0, "y":0, "type":1, "couleur":"black", "collect":0},
                    {"idAssoc" : 0, "idTk":0, "x":1,"y":0, "type":3, "couleur":"blue", "collect":0},
                    {"idAssoc" : 0, "idTk":0, "x":1, "y":1, "type":9, "couleur":"red", "collect":0}
            ]
            }"""


    monde = {
        "00":[
        
        ]
    }

    etatJeu="init"
    etatEditeur = "pose"
    racine = os.getcwd()
    racine = racine.replace("\\", "/" )
    racine = racine+str("/")
    init_dossiers_et_fichiers(racine)

    #Les coordonnées virtuel sont des coordonnées d'une matrice créée en fonction du nombre de cases à l'écran (défini avec "nombreCase")
    id_level = [0,0] #Numéro du niveau dans le quel on est (quand on change de niveau on ajoute ou retire 1 ) [default : [0,0]]
    id_monde = 1 #Numéro du monde dans le quel on est

    nombreCase = 48 #En largeurFenetre (default = 48)
    nombrePixel = largeurFenetre/nombreCase #nombrePixel = nombre de pixels par case sur l'écran (en fonction de la résolution de l'écran, le nombre de pixel change pour toujours avoir le même nombre de case à l'écran)
    nombreCaseX = round(largeurFenetre/nombrePixel) #Le nombre de case en X permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en X
    nombreCaseY = round(hauteurFenetre/nombrePixel) #Le nombre de case en Y permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en Y
    ligneX = [] #Liste des ID des lignes X crées
    ligneY = [] #Liste des ID des lignes X crées

    fenetreeditTest = False #Permet de vérifier si la fenetre d'edition de bloc de l'éditeur est déjà créer
    couleurBloc = 'black' #Défini la couleur d'un bloc
    newColorBloc = 'red' #Défini la nouvelle couleur du bloc
    typeDuBloc = 0 #Défini quel est le type de bloc (0 = solide, 1 = spawn, 2 = clé, 3 = porte)
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
    imageBoutonEditeurExit = ImageTk.PhotoImage(Image.open(racine+"assets/images/exit.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurBlocSolide = ImageTk.PhotoImage(Image.open(racine+"assets/images/bouton_bloc_solide.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurBlocSpawn = ImageTk.PhotoImage(Image.open(racine+"assets/images/bouton_bloc_spawn.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurItemCle = ImageTk.PhotoImage(Image.open(racine+"assets/images/bouton_item_cle.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurBlocPorte = ImageTk.PhotoImage(Image.open(racine+"assets/images/bouton_bloc_porte.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurInfos = ImageTk.PhotoImage(Image.open(racine+"assets/images/help.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurEditBloc = ImageTk.PhotoImage(Image.open(racine+"assets/images/edit_bloc.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurGomme = ImageTk.PhotoImage(Image.open(racine+"assets/images/gomme.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurGommeSelect = ImageTk.PhotoImage(Image.open(racine+"assets/images/gomme_select.png").resize((ratioImage, ratioImage)))
    imageResetSolo = ImageTk.PhotoImage(Image.open(racine+"assets/images/Reset.png").resize((ratioImage, ratioImage)))
    imageBoutonPlayTest = ImageTk.PhotoImage(Image.open(racine+"assets/images/play_test.png").resize((ratioImage, ratioImage)))
    imageBoutonEditeurPoubelleMonde = ImageTk.PhotoImage(Image.open(racine+"assets/images/poubelle_monde.png").resize((ratioImage, ratioImage)))
    imageMonde1 = ImageTk.PhotoImage(Image.open(racine+"assets/images/M1.png").resize((ratioImage, ratioImage)))
    imageMonde2 = ImageTk.PhotoImage(Image.open(racine+"assets/images/M2.png").resize((ratioImage, ratioImage)))
    imageMonde3 = ImageTk.PhotoImage(Image.open(racine+"assets/images/M3.png").resize((ratioImage, ratioImage)))
    bgMenu = ImageTk.PhotoImage(Image.open(racine+"assets/images/menu_bg.png").resize((int(largeurFenetre/2+largeurFenetre/4),int(hauteurFenetre/2+hauteurFenetre/4))))
    bgmenuSoloFrame = ImageTk.PhotoImage(Image.open(racine+"assets/images/menu_solo.png").resize((int(largeurFenetre/2+largeurFenetre/4),int(hauteurFenetre/2+hauteurFenetre/4))))
    bgMenuEdition = ImageTk.PhotoImage(Image.open(racine+"assets/images/menu_editeur.png").resize((int(largeurFenetre/2+largeurFenetre/4),int(hauteurFenetre/2+hauteurFenetre/4))))
    imageOK = ImageTk.PhotoImage(Image.open(racine+"assets/images/ok.png").resize((ratioImage, ratioImage)))
    imageInfoBouton = ImageTk.PhotoImage(Image.open(racine+"assets/images/info_bouton.png").resize((ratioImage, ratioImage)))

    nombrePixel = largeurFenetre/nombreCase #nombrePixel = nombre de pixels par case sur l'écran (en fonction de la résolution de l'écran, le nombre de pixel change pour toujours avoir le même nombre de case à l'écran)
    nombreCaseX = round(largeurFenetre/nombrePixel) #Le nombre de case en X permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en X
    nombreCaseY = round(hauteurFenetre/nombrePixel) #Le nombre de case en Y permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en Y

    init_keys(fenetre) #Appel la fonction des binds
    menu_principal() #Appe la fonction menu (affichage du main menu)

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
    f.bind("<Key-z>", lambda event : mouvement_joueur ("up"))
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
    f.bind("<Key-Right>", lambda event : mouvement_joueur ("right"))

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

    boutonExit = Button(menuPrincipalFrame, image=imageBoutonEditeurExit, relief='groove', bd=0, bg='black', command=exit_menu)
    boutonExit.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

def menu_edition():
    global menuEditionFrame,etatJeu
    etatJeu="menuEdition"

    menuEditionFrame = Frame(fenetre, width=largeurFenetre/2+largeurFenetre/4, height=hauteurFenetre/2+hauteurFenetre/4 ,bg='black')
    menuEditionFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

    fondMenuEdition = Label(menuEditionFrame, image=bgMenuEdition)
    fondMenuEdition.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonExitEdit = Button(menuEditionFrame, image=imageBoutonEditeurExit, relief='groove', bd=0, bg='black', command=exit_menu)
    boutonExitEdit.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonEditeurMonde1 = Button(menuEditionFrame, image=imageMonde1, relief='groove', bd=0, bg='black', command=lambda:lancement_editeur(1))
    boutonEditeurMonde1.place(x=(largeurFenetre/2+largeurFenetre/4)/2-((largeurFenetre/2+largeurFenetre/4)/2)/4, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonEditeurMonde2 = Button(menuEditionFrame, image=imageMonde2, relief='groove', bd=0, bg='black', command=lambda:lancement_editeur(2))
    boutonEditeurMonde2.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/1.37, anchor=CENTER)

    boutonEditeurMonde3 = Button(menuEditionFrame, image=imageMonde3, relief='groove', bd=0, bg='black', command=lambda:lancement_editeur(3))
    boutonEditeurMonde3.place(x=(largeurFenetre/2+largeurFenetre/4)/2+((largeurFenetre/2+largeurFenetre/4)/2)/4, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonEditPlayTest = Button(menuEditionFrame, image=imageBoutonPlayTest, relief='groove', bd=0, bg='black', command=lancement_test_edition)
    boutonEditPlayTest.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)-(hauteurFenetre/2+hauteurFenetre/4)/1.37, anchor=CENTER)

    boutonEditeurInfo = Button(menuEditionFrame, image=imageBoutonEditeurInfos, relief='groove', bd=0, bg='black', command=info_editeur)
    boutonEditeurInfo.place(x=(largeurFenetre/2+largeurFenetre/4)-ratioImage*2,y=ratioImage*2, anchor=CENTER)

def menu_solo():
    global menuSoloFrame,etatJeu
    etatJeu="menuSolo"

    menuSoloFrame = Frame(fenetre, width=largeurFenetre/2+largeurFenetre/4, height=hauteurFenetre/2+hauteurFenetre/4 ,bg='black')
    menuSoloFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

    fondmenuSoloFrame = Label(menuSoloFrame, image=bgmenuSoloFrame)
    fondmenuSoloFrame.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonExitSolo = Button(menuSoloFrame, image=imageBoutonEditeurExit, relief='groove', bd=0, bg='black', command=exit_menu)
    boutonExitSolo.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonSoloMonde1 = Button(menuSoloFrame, image=imageMonde1, relief='groove', bd=0, bg='black', command=lambda:lancement_solo(1))
    boutonSoloMonde1.place(x=(largeurFenetre/2+largeurFenetre/4)/2-((largeurFenetre/2+largeurFenetre/4)/2)/4, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonSoloMonde2 = Button(menuSoloFrame, image=imageMonde2, relief='groove', bd=0, bg='black', command=lambda:lancement_solo(2))
    boutonSoloMonde2.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/1.37, anchor=CENTER)

    boutonSoloMonde3 = Button(menuSoloFrame, image=imageMonde3, relief='groove', bd=0, bg='black', command=lambda:lancement_solo(3))
    boutonSoloMonde3.place(x=(largeurFenetre/2+largeurFenetre/4)/2+((largeurFenetre/2+largeurFenetre/4)/2)/4, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonSoloReset = Button(menuSoloFrame, image=imageResetSolo, relief='groove', bd=0, bg='black', command=reset_solo)
    boutonSoloReset.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)-(hauteurFenetre/2+hauteurFenetre/4)/1.37, anchor=CENTER)

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

        case "editeur": exit_editeur()
        case "solo": exit_solo()
        case "test_editeur": exit_test_editeur()

def close_menu():
    exit_menu()
    menuPrincipalFrame.place_forget()


################################################################### Fonctions de lancement des modes ###################################################################

def lancement_editeur(id):
    global id_monde, id_level, etatJeu, fenetre_editeur, message_editeur, numeroNiveau, boutonGomme
    close_menu()
    etatJeu = "editeur"
    set_grille_fond()
    id_monde = id
    get_monde(id_monde)
    id_level = [0,0]
    get_niveau(id_level)
    affichage_niveau()

    #Fenetre des infos / boutons
    fenetre_editeur = tk.Toplevel() #Création de la fenetre des fonction/boutons de l'éditeur
    fenetre_editeur.geometry("%dx%d%+d%+d" % (300*ratioFenetre,600*ratioFenetre,50,50)) #taille 1 bouton = taille que tu veux + 3 
    fenetre_editeur.resizable(False,False) #Fenetre non redimentionable
    fenetre_editeur.attributes('-topmost',1) #Fenetre toujours au premier plan
    fenetre_editeur.protocol("WM_DELETE_WINDOW", disable_event) #Fenetre non detruisable manuelement
    fenetre_editeur.config(background='#ffffff')

    #Création des boutons / texte sur la fenetre de l'éditeur
    Button(fenetre_editeur, image=imageBoutonEditeurTP, relief='groove', bd=0, bg='#ffffff', command=lambda:type_bloc("tp")).place(x=ratioImage/2,y=ratioImage/2, anchor=CENTER) #bouton_save
    Button(fenetre_editeur, image=imageBoutonEditeurRetour, relief='groove', bd=0, bg='#ffffff', command=del_last_bloc).place(x=ratioImage+ratioImage/2,y=ratioImage/2, anchor=CENTER) #bouton_retour
    Button(fenetre_editeur, image=imageBoutonEditeurPoubelle, relief='groove', bd=0, bg='#ffffff', command=del_all_blocs).place(x=ratioImage*2+ratioImage/2,y=ratioImage/2, anchor=CENTER) #boutonEditeurPoubelle
    Button(fenetre_editeur, image=imageBoutonEditeurNiveauHaut, relief='groove', bd=0, bg='#ffffff', command=lambda:change_level("up")).place(x=ratioImage+ratioImage/2,y=ratioImage+ratioImage/2, anchor=CENTER) #bouton_niveau_up
    Button(fenetre_editeur, image=imageBoutonEditeurNiveauBas, relief='groove', bd=0, bg='#ffffff', command=lambda:change_level("down")).place(x=ratioImage+ratioImage/2,y=ratioImage*3+ratioImage/2, anchor=CENTER) #bouton_niveau_down
    Button(fenetre_editeur, image=imageBoutonEditeurNiveauGauche, relief='groove', bd=0, bg='#ffffff', command=lambda:change_level("left")).place(x=ratioImage/2,y=ratioImage*2+ratioImage/2, anchor=CENTER) #bouton_niveau_left
    Button(fenetre_editeur, image=imageBoutonEditeurNiveauDroite, relief='groove', bd=0, bg='#ffffff', command=lambda:change_level("right")).place(x=ratioImage*2+ratioImage/2,y=ratioImage*2+ratioImage/2, anchor=CENTER) #bouton_niveau_right
    Button(fenetre_editeur, image=imageBoutonEditeurPoubelleMonde, relief='groove', bd=0, bg='#ffffff', command=del_all_level).place(x=ratioImage+ratioImage/2,y=ratioImage*4+ratioImage/2, anchor=CENTER) #boutonEditeurDellAll
    Button(fenetre_editeur, image=imageBoutonEditeurExit, relief='groove', bd=0, bg='#ffffff', command=exit_editeur).place(x=ratioImage*2+ratioImage/2,y=ratioImage*5+ratioImage/2, anchor=CENTER) #boutonEditeurExit
    numeroNiveau = Label(fenetre_editeur, text=id_level, font="Arial, 30", bg='#ffffff') #Affichage du numéro du niveau actuel
    numeroNiveau.place(x=ratioImage+ratioImage/2,y=ratioImage*2+ratioImage/2, anchor=CENTER) #numeroNiveau
    Button(fenetre_editeur, image=imageBoutonEditeurBlocSolide, relief='groove', bd=0, bg='#ffffff', command=lambda:type_bloc("solide")).place(x=ratioImage/2,y=ratioImage+ratioImage/2, anchor=CENTER) #bouton_bloc_solide
    Button(fenetre_editeur, image=imageBoutonEditeurBlocSpawn, relief='groove', bd=0, bg='#ffffff', command=lambda:type_bloc("spawn")).place(x=ratioImage*2+ratioImage/2,y=ratioImage+ratioImage/2, anchor=CENTER) #bouton_bloc_spawn
    Button(fenetre_editeur, image=imageBoutonEditeurItemCle, relief='groove', bd=0, bg='#ffffff', command=lambda:type_bloc("key")).place(x=ratioImage/2,y=ratioImage*3+ratioImage/2, anchor=CENTER) #bouton_item_key
    boutonGomme = Button(fenetre_editeur, image=imageBoutonEditeurGomme, relief='groove', bd=0, bg='#ffffff', command=toggle_gomme)
    boutonGomme.place(x=ratioImage/2,y=ratioImage*4+ratioImage/2, anchor=CENTER) #bouton_gomme
    Button(fenetre_editeur, image=imageBoutonEditeurBlocPorte, relief='groove', bd=0, bg='#ffffff', command=lambda:type_bloc("porte")).place(x=ratioImage*2+ratioImage/2,y=ratioImage*3+ratioImage/2, anchor=CENTER) #bouton_bloc_port
    Button(fenetre_editeur, image=imageBoutonEditeurEditBloc, relief='groove', bd=0, bg='#ffffff', command=set_edit_fenetre).place(x=ratioImage*2+ratioImage/2,y=ratioImage*4+ratioImage/2, anchor=CENTER) #bouton_edit
    message_editeur = Label(fenetre_editeur, text="", font="Arial, 25", bg='#ffffff' ) #Affiche du type de bloc / erreur / info général
    message_editeur.place(x=ratioImage,y=ratioImage*5+ratioImage/2, anchor=CENTER) #message_editeur

def lancement_solo(id):
    global id_monde, id_level, etatJeu, positionJoueur, joueur
    close_menu()
    etatJeu = "solo"
    id_monde = id
    get_monde(id_monde)
    id_level = [0,0]
    get_niveau(id_level)
    for bloc in monde[niveau]: #Cherche si un bloc d'apparition du joueur existe dans le niveau [0,0] pour faire aparaitre 
        if bloc["type"] == 1: #Si il existe, les coordonées d'apparition sont mis à jour
            posjxstart = bloc["x"]
            posjystart = bloc["y"]
            break #Quand les coordonnées sont trouver, la boucle s'arrete pour ne pas chercher des coordonnées pour rien
    try: posjxstart
    except:
        close_menu()
        etatJeu = "menuSolo"
        tkinter.messagebox.showerror("Erreur", "Il n'y a pas de bloc d'apparition dans ce monde") #Affichage d'un message d'erreur
    else:
        affichage_niveau()
        joueur = canevas.create_rectangle(0, 0, nombrePixel, nombrePixel, fill='blue', width=0) #Création du joueur
        canevas.move(joueur,posjxstart*nombrePixel, posjystart*nombrePixel) #Déplacement du joueur au coordonnées d'apparition
        positionJoueur = [posjxstart, posjystart] #0 = x & 1 = y #Actualisation des position du joueur sur la grille

def lancement_test_edition():
    global id_level, etatJeu, joueur, positionJoueur
    close_menu()
    originalPath = racine+"assets/data/editeur" #"originalPath" contient le lien du dossier éditeur
    copyPath = racine+"assets/data/test_editeur/" #"copyPath" contient le lien du dossier test_editeur où vont etre copier les fichier de l'éditeur pour ne pas modifier les fichier dans l'éditeur
    if os.path.exists(copyPath): #Si le dossier contient déjà quelque chose, il est détruit puis recréer 
        shutil.rmtree(copyPath) #Suprétion du dossier
    shutil.copytree(originalPath, copyPath) #Création de la copie du docier d'origine
    etatJeu = "test_editeur"
    get_monde(id_monde)
    id_level = [0,0]
    get_niveau(id_level)
    for bloc in monde[niveau]: #Cherche si un bloc d'apparition du joueur existe dans le niveau [0,0] pour faire aparaitre 
        if bloc["type"] == 1: #Si il existe, les coordonées d'apparition sont mis à jour
            posjxstart = bloc["x"]
            posjystart = bloc["y"]
            break #Quand les coordonnées sont trouver, la boucle s'arrete pour ne pas chercher des coordonnées pour rien
    try: posjxstart
    except:
        tkinter.messagebox.showerror("Erreur", "Il n'y a pas de bloc d'apparition dans ce monde") #Affichage d'un message d'erreur
    else:
        affichage_niveau()
        joueur = canevas.create_rectangle(0, 0, nombrePixel, nombrePixel, fill='blue', width=0) #Création du joueur
        canevas.move(joueur,posjxstart*nombrePixel, posjystart*nombrePixel) #Déplacement du joueur au coordonnées d'apparition
        positionJoueur = [posjxstart, posjystart] #0 = x & 1 = y #Actualisation des position du joueur sur la grille


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
    for bloc in monde[niveau]:
        if bloc["x"] == x and bloc ["y"] == y:
            return
        if bloc["type"] == 1 and typeDuBloc == 1:
            canevas.delete(bloc["idTk"])
            del monde[niveau][indexBloc]
        indexBloc += 1
    demiPixel = 0
    if typeDuBloc == 2:
        demiPixel = nombrePixel/4
    monde[niveau].append({"idAssoc" : 0, "idTk":canevas.create_rectangle(x*nombrePixel+demiPixel, y*nombrePixel+demiPixel, x*nombrePixel+nombrePixel-demiPixel, y*nombrePixel+nombrePixel-demiPixel, fill=couleurBloc), "x":x, "y":y, "type":typeDuBloc, "couleur":couleurBloc, "collect":0})
    save(id_monde)

def del_last_bloc():
    global monde
    if etatJeu == "editeur" and len(monde[niveau]) > 0:
        print(monde[niveau][-1]["idTk"])
        canevas.delete(monde[niveau][-1]["idTk"])
        del monde[niveau][-1]
        save(id_monde)

def del_all_blocs():
    global monde
    cacher_niveau()
    monde[niveau] = list()
    save(id_monde)

def del_all_level():
    global monde, id_level
    attention = tkinter.messagebox.askyesno("Attention", "Voulez vous détruire tout les blocs de ce niveau ?")
    if attention:
        cacher_niveau()
        monde[niveau].clear()
        id_level = [0,0]
        save(id)

def toggle_gomme ():
    global etatEditeur
    if etatEditeur != "gomme":
        etatEditeur = "gomme"
    else:
        etatEditeur = "pose"

def gomme(x,y):
    if etatJeu == "editeur":
        indexBloc = 0
        for bloc in monde[niveau]:
            if bloc["x"] == x and bloc["y"] == y:
                canevas.delete(bloc["idTk"])
                del monde[niveau][indexBloc]
                break
            indexBloc += 1

def set_edit_fenetre():
    global etatEditeur, textTypeBlocSelect, fenetre_edit_bloc
    if etatEditeur != "edit":
        etatEditeur = "edit"

        fenetre_edit_bloc = tk.Toplevel()
        fenetre_edit_bloc.resizable(False,False)
        fenetre_edit_bloc.geometry("%dx%d%+d%+d" % (500*ratioFenetre,300*ratioFenetre,50,50))
        fenetre_edit_bloc.attributes('-topmost',1)
        fenetre_edit_bloc.protocol("WM_DELETE_WINDOW", disable_event)

        Label(fenetre_edit_bloc, text="Edit Object", font=("Arial", int(32*ratioFenetre))).place(x=ratioImage*2+ratioImage/2,y=20*ratioFenetre, anchor=CENTER)
        Label(fenetre_edit_bloc, text="Type Bloc : ", font=("Arial", int(24*ratioFenetre))).place(x=25*ratioFenetre, y=65*ratioFenetre)
        textTypeBlocSelect = Label(fenetre_edit_bloc, text="None", font=("Arial", int(24*ratioFenetre)))
        textTypeBlocSelect.place(x=275*ratioFenetre, y=65*ratioFenetre)
    else:
        etatEditeur = "pose"
        fenetre_edit_bloc.destroy()

def edit_bloc(x,y):
    global selectBlocID
    for bloc in monde[niveau]:
        if bloc["x"] == x and bloc["y"] == y:
            selectBlocID = bloc["idTk"]
            match bloc["type"]:
                case 0: textTypeBlocSelect.config(text="Bloc Solide")
                case 1: textTypeBlocSelect.config(text="Bloc Spawn")
                case 2:
                    textTypeBlocSelect.config(text="Item Clé")
                    config_edit_fenetre(2)
                case 3:
                    textTypeBlocSelect.config(text="Bloc Porte")
                    config_edit_fenetre(3)
                case 4:
                    textTypeBlocSelect.config(text="Bloc TP")
                    config_edit_fenetre(4)
            break

def config_edit_fenetre(typeB):
    global entryIDcle,boutonIDCleValidation,couleurSet,textIDKey,textIDTP1,textIDTP2,entryID1,entryID2,boutonIDTPValidation
    try:
        entryIDcle.destroy()
        #infoBouton.destroy()
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
        entryIDcle = Entry(fenetre_edit_bloc, bg="lightgrey", width=int(10*ratioFenetre), font=("Arial", int(24*ratioFenetre)))
        entryIDcle.place(x=275*ratioFenetre, y=110*ratioFenetre)
        boutonIDCleValidation = Button(fenetre_edit_bloc, image=imageOK, relief='groove', bd=0, bg='black', command=lambda:get_key(str(entryIDcle.get())))
        boutonIDCleValidation.place(x=25*ratioFenetre,y=175*ratioFenetre)
        """infoBouton = Button(fenetre_edit_bloc, image=imageInfoBouton, relief='groove', bd=0, bg='black', command=id_exist)
        infoBouton.place(x=130*ratioFenetre,y=175*ratioFenetre)"""
        textIDKey = Label(fenetre_edit_bloc, text="ID :", font=("Arial", int(24*ratioFenetre)))
        textIDKey.place(x=130*ratioFenetre,y=110*ratioFenetre) 
        couleurSet = Scale(fenetre_edit_bloc, orient='horizontal', from_=1, to=8, resolution=1, tickinterval=2, length=180*ratioFenetre, label='Couleur', font=("Arial", int(10*ratioFenetre)), command=change_color)
        couleurSet.place(x=275*ratioFenetre,y=150*ratioFenetre)
    elif typeB == 4:
        textIDTP1 = Label(fenetre_edit_bloc, text="ID départ", font=("Arial", int(24*ratioFenetre)))
        textIDTP1.place(x=100*ratioFenetre,y=130*ratioFenetre,anchor=CENTER)
        textIDTP2 = Label(fenetre_edit_bloc, text="ID arrivée", font=("Arial", int(24*ratioFenetre)))
        textIDTP2.place(x=400*ratioFenetre,y=130*ratioFenetre,anchor=CENTER)
        entryID1 = Entry(fenetre_edit_bloc, bg="lightgrey", width=int(10*ratioFenetre), font=("Arial", int(24*ratioFenetre)))
        entryID1.place(x=100*ratioFenetre, y=210*ratioFenetre,anchor=CENTER)
        entryID2 = Entry(fenetre_edit_bloc, bg="lightgrey", width=int(10*ratioFenetre), font=("Arial", int(24*ratioFenetre)))
        entryID2.place(x=400*ratioFenetre, y=210*ratioFenetre,anchor=CENTER)
        boutonIDTPValidation = Button(fenetre_edit_bloc, image=imageOK, relief='groove', bd=0, bg='black', command=lambda:get_tp((entryID1.get(),entryID2.get())))
        boutonIDTPValidation.place(x=250*ratioFenetre,y=240*ratioFenetre,anchor=CENTER)

def get_key(id):
    global monde
    indexBloc = 0
    for bloc in monde[niveau]:
        if bloc["idTk"] == selectBlocID:
            monde[niveau][indexBloc]["idAssoc"] = id
        indexBloc += 1
    print(monde)

def get_tp(id):
    global monde
    indexBloc = 0
    for bloc in monde[niveau]:
        if bloc["idTk"] == selectBlocID:
            monde[niveau][indexBloc]["idAssoc"] = id
        indexBloc += 1

def change_color (c): #Change la couleur du bloc selectionner
    global newColorBloc
    match couleurSet.get():
        case 1: newColorBloc = 'orange'
        case 2: newColorBloc = 'red'
        case 3: newColorBloc = 'yellow'
        case 4: newColorBloc = 'green'
        case 5: newColorBloc = 'blue'
        case 6: newColorBloc = 'pink'
        case 7: newColorBloc = 'purple'
        case 8: newColorBloc = 'brown'

    for bloc in monde[niveau]:
        if bloc["idTk"] == selectBlocID:
            bloc["color"] = newColorBloc
            canevas.itemconfig(bloc["idTk"], fill=newColorBloc)
            break


################################################################### Fonctions du joueur ###################################################################

def mouvement_joueur(direction):
    global positionJoueur, joueur, id_level

    if etatJeu == "solo" or etatJeu == "test_editeur":
        if direction == "up": #Si la direction est egale à "up"
            posJTestX = positionJoueur[0] #Test de la prochaine position du joueur dans la grille pour x
            posJTestY = positionJoueur[1]-1 #Test de la prochaine position du joueur dans la grille pour y
            xyJ = 1 #Indique quel est l'axe qui est demander (0=x et 1=y)
            posJF = -1 #Donne de combien doit être changer les coordonnées du joueur en fonction de l'axe
            posMax = 0 #Donne la position max du joueur sur la grille 
            deplacement = [0, -nombrePixel] #Donne de combien le joueur doit ce déplacer sur la grille
            tp = [positionJoueur[0],nombreCaseY-1]

        elif direction == "down":
            posJTestX = positionJoueur[0]
            posJTestY = positionJoueur[1]+1
            xyJ = 1
            posJF = +1
            posMax = nombreCaseY-1
            deplacement = [0, +nombrePixel]
            tp = [positionJoueur[0],0]

        elif direction == "left":
            posJTestX = positionJoueur[0]-1
            posJTestY = positionJoueur[1]
            xyJ = 0
            posJF = -1
            posMax = 0
            deplacement = [-nombrePixel, 0]
            tp = [nombreCaseX-1,positionJoueur[1]]

        elif direction == "right":
            posJTestX = positionJoueur[0]+1
            posJTestY = positionJoueur[1]
            xyJ = 0
            posJF = +1
            posMax = nombreCaseX-1
            deplacement = [+nombrePixel, 0]
            tp = [0,positionJoueur[1]]

        indexBloc = 0
        ok = True
        for bloc in monde[niveau]:
            if bloc["x"] == posJTestX and bloc["y"] == posJTestY:
                if bloc["type"] == 0:
                    ok = False

                elif bloc["type"] == 2 and bloc["collect"] == 0:
                    ramasse_cle(indexBloc)

                elif bloc["type"] == 3:
                    ok = ouvre_porte(indexBloc)

                elif bloc["type"] == 4:
                    tp_joueur(indexBloc)

            indexBloc += 1
        if ok == True:
            if positionJoueur[xyJ] == posMax: #Si la position du joueur est egale à la limite de l'écran (ou de la map)
                print(type(id_level[xyJ]), type(int(posJF)))
                id_level[xyJ] = id_level[xyJ]+int(posJF)
                cacher_niveau()
                get_niveau(id_level) #La fonction level_search est appeler
                affichage_niveau()
                positionJoueur = tp
                canevas.moveto(joueur,tp[0]*nombrePixel,tp[1]*nombrePixel)
            else:
                canevas.move(joueur, deplacement[0], deplacement[1]) #Le joueur est déplacer sur la case demander
                positionJoueur[xyJ] = positionJoueur[xyJ]+posJF #Les coordonnées du joueur sont actualiser

def ramasse_cle(indexBloc):
    global monde
    monde[niveau][indexBloc]["collect"] = 1
    canevas.delete(monde[niveau][indexBloc]["idTk"])

def ouvre_porte(indexBloc):
    global monde
    for bloc in monde[niveau]:
        if bloc["type"] == 2 and bloc["collect"] == 1:
            monde[niveau][indexBloc]["collect"] = 1
            canevas.delete(monde[niveau][indexBloc]["idTk"])
            return True
    return False

def tp_joueur(indexBloc):
    global id_level, positionJoueur
    indexNiveau = 0
    indexBlocTP = 0
    for niveauTest in monde:
        for bloc in monde[niveauTest]:
            if bloc["type"] == 4:
                if bloc["idAssoc"][0] == monde[niveau][indexBloc]["idAssoc"][1]:
                    id_level = [int(niveauTest[0]),int(niveauTest[1])]
                    print(id_level)
                    cacher_niveau()
                    get_niveau(id_level) #La fonction level_search est appeler
                    affichage_niveau()
                    positionJoueur = [bloc["x"],bloc["y"]]
                    canevas.moveto(joueur,positionJoueur[0]*nombrePixel,positionJoueur[1]*nombrePixel)
                    break

            indexBlocTP += 0
        indexNiveau +=1


################################################################### Fonctions du fonctionnement global du programme ###################################################################

def disable_event(): #Disable
    pass

def exit_key(): #Permet des retour au menu avec la touche "echap"
    exit_menu()

def info_editeur(): #Fenêtre d'infos des action possible
    webbrowser.open(racine+"assets/Guide_editeur.pdf")

def get_niveau(id): #Permet de tourver le niveau à charger
    global niveau, monde
    for niveau in monde:
        if(niveau==str(id[0])+str(id[1])): break
    else:
        niveau=str(id[0])+str(id[1])
        monde[niveau] = list()

def get_monde(id): #Permet de tourver le monde à charger
    global monde
    dossier_data = racine + "assets/data/"
    match etatJeu:
        case "editeur": dossier = dossier_data + "editeur/monde"+str(id)+".gac"
        case "solo": dossier = dossier_data + "solo/monde"+str(id)+".gac"
        case "test_editeur": dossier = dossier_data + "test_editeur/monde"+str(id)+".gac"
    with open(dossier, "rb") as fichierMonde:
        monde = pickle.load(fichierMonde)

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
    for bloc in monde[niveau]:
        couleurBloc = bloc["couleur"]
        demiPixel = 0
        if bloc["type"] == 2:
            demiPixel = nombrePixel/4
        if not bloc["collect"] == 1:
            monde[niveau][indexBloc]["idTk"] = (canevas.create_rectangle(bloc["x"]*nombrePixel+demiPixel, bloc["y"]*nombrePixel+demiPixel, bloc["x"]*nombrePixel+nombrePixel-demiPixel, bloc["y"]*nombrePixel+nombrePixel-demiPixel, fill=couleurBloc))
        indexBloc += 1
    couleurBloc = 'black'

def cacher_niveau(): #Masque le niveau
    for bloc in monde[niveau]:
        canevas.delete(bloc["idTk"])

def supp_niveau():
    global monde
    del monde[niveau]

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

def exit_editeur():
    global etatJeu
    del_grille_fond()
    save(id_monde)
    cacher_niveau()
    fenetre_editeur.destroy()
    if etatEditeur == "edit":
        fenetre_edit_bloc.destroy()
    etatJeu="menuEdition"
    menuPrincipalFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)
    menuEditionFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

def exit_solo():
    global etatJeu
    save(id_monde)
    cacher_niveau()
    etatJeu="menuSolo"
    menuPrincipalFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)
    menuSoloFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)
    canevas.delete(joueur)
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

def reset_solo():
    attention = tkinter.messagebox.askyesno("Attention", "Voulez vous reset la progression ?")
    if attention:
        originalPath = racine+"assets/data/origine"
        copyPath = racine+"assets/data/solo/"
        shutil.rmtree(copyPath)
        shutil.copytree(originalPath, copyPath)


################################################################### Autre ###################################################################
start()