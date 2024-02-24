#Import des bibliothèques
import tkinter as tk, tkinter.messagebox; import tkinter.scrolledtext; from tkinter import *; import pickle, os, shutil, webbrowser
try: #Comme PIL n'est pas une bibliothèque installer par défaut, il faut l'ajouter pour que le programme fonctionne.
    from PIL import Image, ImageTk
except:
    os.system('pip install Pillow')
from PIL import Image, ImageTk


################################################################### Les fonctions de mise en place du programme ###################################################################

def start(): #La fonction "start" permet de déclaré la plus part des variable global.
    global monde, fenetre, etatEditeur, toggleMouvement, freezeEscape, creditTexte, pbPlayer, bgMenuCredit, patchNotesTexte, bgMenuMAJ, directionsBinds, theKey, commandMondeSolo, exitCommand, imageResetSoloToggle, imageBoutonPlayTestToggle, imageNotExitTest, imageMonde1Test, imageMonde2Test, imageMonde3Test, imageNotExit, commandMondeEditeur, nombrePixelX, nombrePixelY, imageMonde1Del, imageMonde2Del, imageMonde3Del, bgmenuresultat, imageBoutonEditeurFinish, largeurFenetre, hauteurFenetre, canevas, lienIconeFenetre, etatJeu, nombreCaseY, nombreCaseX, racine, imageBoutonPlayTest, bgMenu, imageOK, imageInfoBouton, tailleImage, ratioImage, bgmenuSoloFrame, ratioFenetre, bgMenuEdition, nombreCase, imageBoutonEditeurGommeSelect, imageBoutonEditeurGomme, imageBoutonEditeurPoubelleMonde, imageBoutonEditeurBlocPorte, imageMonde1, imageMonde2, imageMonde3, imageResetSolo, imageBoutonEditeurItemCle, imageBoutonEditeurEditBloc, id_level, imageBoutonSolo, imageBoutonEditeur, ligneX, ligneY, imageBoutonEditeurNiveauHaut, imageBoutonEditeurNiveauBas, imageBoutonEditeurNiveauGauche, imageBoutonEditeurNiveauDroite, imageBoutonEditeurTP, imageBoutonEditeurRetour, imageWIP, imageBoutonEditeurPoubelle, imageExit, imageBoutonEditeurBlocSolide, couleurBloc, typeDuBloc, imageBoutonEditeurBlocSpawn, id_monde, imageBoutonEditeurInfos

    ################################################################### Mise en place de la fenetre et du canevas.

    fenetre = Tk() #Instance de la fenetre principal.

    largeurFenetre = fenetre.winfo_screenwidth() #largeurFenetre contient le nombre de pixel en largeur de l'écran actuel.
    hauteurFenetre = fenetre.winfo_screenheight() #hauteurFenetre contient le nombre de pixel en hauteur de l'écran actuel.

    fenetre.title("Electro Cube Adventure") #Nom de l'application.
    
    fenetre.attributes('-fullscreen', True) #La fenetre est en plein écran.
    canevas = Canvas(fenetre, width=largeurFenetre, height=hauteurFenetre,bg='#3b3b3b') #Instance du Canvas (avec comme paramètre la largeur, la hauteur, et la couleur (ici du gris)).


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
            "lastCoords":[[],[]],

            "runTime" : [0,0,0]

            "reset" : [True,True,True]

            }
    """


    monde = {   "niveaux":{"0,0":[]},
                "lastCoords":[[],[]],
                "runTime":[0,0,0],
                "reset" : [True,True,True]
             } #monde est un dictionnaire qui va contenir toutes les information sur un monde : les blocs dans un niveau, le record de temps du joueur sur le monde...


    etatJeu="init" #etatJeu est une variable str qui permet au programme de savoir où il en est dans son exécution.
    etatEditeur = "pose" #etatEditeur est une variable str qui permet à l'éditeur de savoir dans quel mode il est.

    #racine contient le chemain complet du dossier dans le quel est le .py du programme.
    racine = os.getcwd() 
    racine = racine.replace("\\", "/" )
    racine = racine+str("/")
    init_dossiers_et_fichiers(racine) #Appel de la fonction qui permet de recréer les dossier qui aurait pu être détruit.

    pbPlayer = [0,0,0] #pbPlayer est une liste de 3 entier qui contient le méilleur temps du joueur sur chaque monde.
    if os.path.exists(racine+"assets/data/origine/pb_Joueur.gac"):
        with open(racine+"assets/data/origine/pb_Joueur.gac", "rb") as fichierPB:
            pbPlayer = pickle.load(fichierPB)
    else: 
        with open(racine+"assets/data/origine/pb_Joueur.gac", "wb") as fichierMonde:
            pickle.dump(pbPlayer, fichierMonde)
    #Si le fichier pb_Joueur existe déjà alors il est charger pour récupérer les temps.

    #Les coordonnées virtuel sont des coordonnées d'une matrice créée en fonction du nombre de cases à l'écran (défini avec "nombreCase").
    id_level = [0,0] #Numéro du niveau dans le quel on est (quand on change de niveau on ajoute ou retire 1 ) [default : [0,0]].
    id_monde = 1 #Numéro du monde dans le quel on est.

    directionsBinds = {'z':"up",'q':"left",'d':"right",'s':"down"} #directionBinds est un dictionnaire qui contient les touches de direction (ex : quand "z" sera appuier, la direction sera "up").
    theKey = "" #theKey prend la valeur de la dernière touche enfoncer.

    nombreCaseX = 48 #Le nombre de case en X permet de donner facilement au programme le nombre de blocs max en X.
    nombreCaseY = 27
    nombrePixelX = largeurFenetre/nombreCaseX #nombrePixel = nombre de pixels par case sur l'écran (en fonction de la résolution de l'écran, le nombre de pixel change pour toujours avoir le même nombre de case à l'écran).
    nombrePixelY = hauteurFenetre/nombreCaseY
     #Le nombre de case en Y permet de donner facilement au programme le nombre de blocs max en Y.
    ligneX = [] #Liste des ID des lignes X crées.
    ligneY = [] #Liste des ID des lignes Y crées.

    #Ces trois variables contiennent l'appel de 3 fonctions. Ces variables seront modifier plus tard dans le programme.
    commandMondeSolo = lancement_solo
    exitCommand = exit_menu
    commandMondeEditeur = lancement_editeur

    couleurBloc = 'black' #Défini la couleur d'un bloc.
    typeDuBloc = 0 #Défini quel est le type de bloc (0 = solide, 1 = spawn, 2 = clé, 3 = porte, 4 = finish, 5 = TP).
    toggleMouvement = False #Variable qui permet d'utiliser ou non la fonction de déplacement.
    freezeEscape = False #Variable qui permet ou non de revenir en arrière avec la touche "echap".

    #Import des images
    ratioFenetre = largeurFenetre/2560 #Calcule d'un ratio entre la résolution utilisé par l'utilisateur et la résolution utilisé pour mettre en place toutes les position d'image.
    tailleImage = 100 #La taille des images carré.
    ratioImage = int(tailleImage*ratioFenetre) #Calcule d'un ratio pour les image grace au ratioFenetre.
    #Redimentionnement des images pour correspondre à la résolution voulue.
    #Pour les images carré, le .resize utilise comme valeur ratioImage.
    #Pour les images des menu, le .resize utilise comme valeur la largeur de la fenetre et la hauteur.
    #Ici il est obligatoir d'utiliser en premier ImageTk.PhotoImage car sinon, les image importer avec PIL ne sont pas reconue par tkinter.
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

    nombreCaseX = round(largeurFenetre/nombrePixelX) #Le nombre de case en X permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en X.
    nombreCaseY = round(hauteurFenetre/nombrePixelY) #Le nombre de case en Y permet de donner facilement au programme (pour déplacer le joueur d'un coté à un autre par exemple) le nombre de blocs max en Y.

    init_keys(fenetre) #Appel la fonction des binds.
    menu_principal() #Appe la fonction menu (affichage du main menu).

    #patchNoteTexte et creditTexte sont 2 variables str qui contiennent le dernier patch note et les crédits du jeu.
    with open(racine+"assets/patch_notes.txt", "r") as patchnote:
        patchNotesTexte = patchnote.read()
    with open(racine+"assets/credit.txt", "r") as credit:
        creditTexte = credit.read()

    if not 1.75 < largeurFenetre/hauteurFenetre < 1.8:
        tkinter.messagebox.showinfo("Attention", "La résolution de votre écran n'est pas adapter pour le jeu. Il est possible que vous rencontriez des problème d'affichage")

    fenetre.iconbitmap(lienIconeFenetre) #Change l'icone de la fenetre par l'icone du jeu.
    canevas.pack()
    fenetre.mainloop()

def init_dossiers_et_fichiers(racine): #Fonction qui permet d'appeller ea fonction pour recréer les fichier manquan.
    #Attribution des chemains.
    dossier_data = racine + "assets/data/"
    dossier_editeur = dossier_data + "editeur/"
    dossier_test_editeur = dossier_data + "test_editeur/"
    dossier_solo = dossier_data + "solo/"
    dossier_origine = dossier_data + "origine/"

    fichier_editeur_monde1 = dossier_editeur + "monde1.gac"
    fichier_editeur_monde2 = dossier_editeur + "monde2.gac"
    fichier_editeur_monde3 = dossier_editeur + "monde3.gac"

    fichier_origine_monde1 = dossier_origine + "monde1.gac"
    fichier_origine_monde2 = dossier_origine + "monde2.gac"
    fichier_origine_monde3 = dossier_origine + "monde3.gac"

    #Appel de la fonction de recréation.
    testEtCreeDossier(dossier_data)
    testEtCreeDossier(dossier_editeur)
    testEtCreeDossier(dossier_test_editeur)
    testEtCreeDossier(dossier_solo)
    testEtCreeDossier(dossier_origine)

    testEtCreeFichier(fichier_editeur_monde1)
    testEtCreeFichier(fichier_editeur_monde2)
    testEtCreeFichier(fichier_editeur_monde3)

    testEtCreeFichier(fichier_origine_monde1)
    testEtCreeFichier(fichier_origine_monde2)
    testEtCreeFichier(fichier_origine_monde3)

def testEtCreeDossier(chemin): #Fonction de recréation des dossier
    if not os.path.exists(chemin):os.mkdir(chemin)

def testEtCreeFichier(chemin): #Fonction de recréation des fichiers
    if not os.path.exists(chemin):
        with open(chemin, "wb") as fichierMonde:
            pickle.dump(monde, fichierMonde)

def init_keys(f): #Les Binds
    #Bind pour les directions
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

def menu_principal(): #Fonction pour mettre en place le menu pricipale.
    global menuPrincipalFrame, etatJeu
    etatJeu="menuPrincipal" #Modification de l'état du jeu.

    menuPrincipalFrame = Frame(fenetre, width=largeurFenetre/2+largeurFenetre/4, height=hauteurFenetre/2+hauteurFenetre/4 ,bg='black') #La frame du menu pricipal permet de mettre des information dessus et de tout faire disparètre en meme temps.
    menuPrincipalFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

    fondMenu = Label(menuPrincipalFrame, image=bgMenu) #fondMenu affiche l'image de fond du menu.
    fondMenu.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonSolo = Button(menuPrincipalFrame, image=imageBoutonSolo, relief='groove', bd=0, bg='black', command=menu_solo) #bouton solo est le bouton pour avoir accés au menu solo.
    boutonSolo.place(x=(largeurFenetre/2+largeurFenetre/4)/2-((largeurFenetre/2+largeurFenetre/4)/2)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonEditeur = Button(menuPrincipalFrame, image=imageBoutonEditeur, relief='groove', bd=0, bg='black', command=menu_edition)#bouton editeur est le bouton pour avoir accés au menu editeur.
    boutonEditeur.place(x=(largeurFenetre/2+largeurFenetre/4)/2+((largeurFenetre/2+largeurFenetre/4)/2)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonMAJ = Button(menuPrincipalFrame, image=imageInfoBouton, relief='groove', bd=0, bg='black', command=menu_note_maj) #boutonMAJ permet de d'avoir le patch notes.
    boutonMAJ.place(x=(largeurFenetre/2+largeurFenetre/4)-ratioImage*2, y=(hauteurFenetre/2+hauteurFenetre/4)-ratioImage*2, anchor=CENTER)

    boutonExit = Button(menuPrincipalFrame, image=imageExit, relief='groove', bd=0, bg='black', command=exit_menu) #boutonExit permet de quitter le jeu
    boutonExit.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonCredit = Button(menuPrincipalFrame, image=imageInfoBouton, relief='groove', bd=0, bg='black', command=menu_credit) #boutonCredit permet d'avoir les crédit
    boutonCredit.place(x=ratioImage*2, y=(hauteurFenetre/2+hauteurFenetre/4)-ratioImage*2, anchor=CENTER)

    Label(menuPrincipalFrame, text="Version 1.0", font=("Noto Mono", int(12*ratioFenetre)), bg='black', fg='white').place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)-10, anchor=CENTER)#Affichage de la version du jeu

def menu_edition(): #Fonction pour mettre en place le menu de l'éditeur.
    global menuEditionFrame,etatJeu, boutonEditeurMonde1, boutonEditeurMonde2, boutonEditeurMonde3, boutonExitEdit, boutonEditPlayTest
    etatJeu="menuEdition" #changement de l'état du jeu

    menuEditionFrame = Frame(fenetre, width=largeurFenetre/2+largeurFenetre/4, height=hauteurFenetre/2+hauteurFenetre/4 ,bg='black') #Frame du menu éditeur, pareil que pour le menu principal
    menuEditionFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

    fondMenuEdition = Label(menuEditionFrame, image=bgMenuEdition) #Affiche l'image au fond du menu
    fondMenuEdition.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonExitEdit = Button(menuEditionFrame, image=imageExit, relief='groove', bd=0, bg='black', command=exitCommand) #Permet de revenir au menu pricipal
    boutonExitEdit.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonEditeurMonde1 = Button(menuEditionFrame, image=imageMonde1, relief='groove', bd=0, bg='black', command=lambda:commandMondeEditeur(1)) #Permet de soit lancer l'éditeur soit de lancer le mode de test le monde 1.
    boutonEditeurMonde1.place(x=(largeurFenetre/2+largeurFenetre/4)/2-((largeurFenetre/2+largeurFenetre/4)/2)/4, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonEditeurMonde2 = Button(menuEditionFrame, image=imageMonde2, relief='groove', bd=0, bg='black', command=lambda:commandMondeEditeur(2)) #Permet de soit lancer l'éditeur soit de lancer le mode de test le monde 2.
    boutonEditeurMonde2.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/1.37, anchor=CENTER)

    boutonEditeurMonde3 = Button(menuEditionFrame, image=imageMonde3, relief='groove', bd=0, bg='black', command=lambda:commandMondeEditeur(3)) #Permet de soit lancer l'éditeur soit de lancer le mode de test le monde 3.
    boutonEditeurMonde3.place(x=(largeurFenetre/2+largeurFenetre/4)/2+((largeurFenetre/2+largeurFenetre/4)/2)/4, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonEditPlayTest = Button(menuEditionFrame, image=imageBoutonPlayTest, relief='groove', bd=0, bg='black', command=toggle_test_editeur) #Permet de changer les 3 bouton de monde pour lancer le mode de test ou l'éditeur.
    boutonEditPlayTest.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)-(hauteurFenetre/2+hauteurFenetre/4)/1.37, anchor=CENTER)

    boutonEditeurInfo = Button(menuEditionFrame, image=imageBoutonEditeurInfos, relief='groove', bd=0, bg='black', command=info_editeur) #Permet d'ouvir la doc de l'éditeur.
    boutonEditeurInfo.place(x=(largeurFenetre/2+largeurFenetre/4)-ratioImage*2, y=ratioImage*2, anchor=CENTER)

def menu_solo(): #Fonction pour mettre en place le menu du solo.
    global menuSoloFrame,etatJeu, boutonSoloMonde1, boutonSoloMonde2, boutonSoloMonde3, boutonExitSolo, boutonSoloReset
    etatJeu="menuSolo" #Changement de l'état du jeu

    menuSoloFrame = Frame(fenetre, width=largeurFenetre/2+largeurFenetre/4, height=hauteurFenetre/2+hauteurFenetre/4 ,bg='black') #Frame du menu solo, pareil que le menu principal.
    menuSoloFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

    fondmenuSoloFrame = Label(menuSoloFrame, image=bgmenuSoloFrame) #Affiche l'image au fond du menu.
    fondmenuSoloFrame.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonExitSolo = Button(menuSoloFrame, image=imageExit, relief='groove', bd=0, bg='black', command=exitCommand) #Permet de revenir au menu principal.
    boutonExitSolo.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonSoloMonde1 = Button(menuSoloFrame, image=imageMonde1, relief='groove', bd=0, bg='black', command=lambda:commandMondeSolo(1)) #Permet de soit lancer le solo soit de réinisialiser le monde 1.
    boutonSoloMonde1.place(x=(largeurFenetre/2+largeurFenetre/4)/2-((largeurFenetre/2+largeurFenetre/4)/2)/4, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonSoloMonde2 = Button(menuSoloFrame, image=imageMonde2, relief='groove', bd=0, bg='black', command=lambda:commandMondeSolo(2)) #Permet de soit lancer le solo soit de réinisialiser le monde 2.
    boutonSoloMonde2.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/1.37, anchor=CENTER)

    boutonSoloMonde3 = Button(menuSoloFrame, image=imageMonde3, relief='groove', bd=0, bg='black', command=lambda:commandMondeSolo(3)) #Permet de soit lancer le solo soit de réinisialiser le monde 3.
    boutonSoloMonde3.place(x=(largeurFenetre/2+largeurFenetre/4)/2+((largeurFenetre/2+largeurFenetre/4)/2)/4, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)

    boutonSoloReset = Button(menuSoloFrame, image=imageResetSolo, relief='groove', bd=0, bg='black', command=toggle_reset) #Permet de changer les 3 bouton de lancement.
    boutonSoloReset.place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)-(hauteurFenetre/2+hauteurFenetre/4)/1.37, anchor=CENTER)

def menu_resultat(): #Fonction pour mettre en place le menu des résultats.
    global menuResultatFrame

    menuResultatFrame = Frame(fenetre, width=largeurFenetre/2+largeurFenetre/4, height=hauteurFenetre/2+hauteurFenetre/4 ,bg='black') #Frame comme sur le menu pricipal
    menuResultatFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

    Label(menuResultatFrame, image=bgmenuresultat).place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER) #Affiche l'image de fond du menu.
    #Affichage des résulats.
    Label(menuResultatFrame, text=("Temps de la Run : "+str(monde["runTime"][id_monde-1])+" s"), font=("Noto Mono", int(30*ratioFenetre)), bg='black', fg='white').place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER)
    Label(menuResultatFrame, text=("Meilleur temps : "+str(pbPlayer[id_monde-1])+" s"), font=("Noto Mono", int(30*ratioFenetre)), bg='black', fg='white').place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2+100*ratioFenetre, anchor=CENTER)
    Label(menuResultatFrame, text=(messageScore), font=("Noto Mono", int(30*ratioFenetre)), bg='black', fg='white').place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2-100*ratioFenetre, anchor=CENTER)
    Button(menuResultatFrame, image=imageExit, relief='groove', bd=0, bg='black', command=exit_menu).place(x=(largeurFenetre/2+largeurFenetre/4)/2,y=(hauteurFenetre/2+hauteurFenetre/4)-ratioImage, anchor=CENTER) #boutonEditeurExit

def menu_note_maj(): #Fonction pour mettre en place le menu du patch notes.
    global menuNoteMAJFrame, etatJeu
    etatJeu = "menuNoteMAJ" #Changement de l'état du jeu.

    menuNoteMAJFrame = Frame(fenetre, width=largeurFenetre/2+largeurFenetre/4, height=hauteurFenetre/2+hauteurFenetre/4 ,bg='black') #Frame comme au menu pricipal.
    menuNoteMAJFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

    Label(menuNoteMAJFrame, image=bgMenuMAJ).place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER) #Image de fond.
    Button(menuNoteMAJFrame, image=imageExit, relief='groove', bd=0, bg='black', command=exit_menu).place(x=(largeurFenetre/2+largeurFenetre/4)/2,y=(hauteurFenetre/2+hauteurFenetre/4)-ratioImage, anchor=CENTER) #bouton pour revenir au menu pricipal.
    Label(menuNoteMAJFrame, text=patchNotesTexte, font=("Noto Mono", int(24*ratioFenetre)), bg="black", fg="white").place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER) #Texte du patch notes.

def menu_credit(): #Fonction pour mettre en place le menu des crédits.
    global menuNoteCreditFrame, etatJeu
    etatJeu = "menuCredit" #Changement de l'état du jeu.

    menuNoteCreditFrame = Frame(fenetre, width=largeurFenetre/2+largeurFenetre/4, height=hauteurFenetre/2+hauteurFenetre/4 ,bg='black') #Frame comme au menu pricipal.
    menuNoteCreditFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

    Label(menuNoteCreditFrame, image=bgMenuCredit).place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER) #Affichage de l'image de fond.
    Button(menuNoteCreditFrame, image=imageExit, relief='groove', bd=0, bg='black', command=exit_menu).place(x=(largeurFenetre/2+largeurFenetre/4)/2,y=(hauteurFenetre/2+hauteurFenetre/4)-ratioImage, anchor=CENTER) #bouton pour revenir au menu principal.
    Label(menuNoteCreditFrame, text=creditTexte, font=("Noto Mono", int(24*ratioFenetre)), bg="black", fg="white").place(x=(largeurFenetre/2+largeurFenetre/4)/2, y=(hauteurFenetre/2+hauteurFenetre/4)/2, anchor=CENTER) #Texte pour afficher les crédits.

def exit_menu(): #Fonction pour changer de menu.
    global etatJeu
    if not freezeEscape: #Si un retour au menu precedent est possible.
        match etatJeu: #Alors en fonction de etat jeu, il suffit de quitter le menu dans le quel on se trouve.
            case "menuPrincipal": fenetre.destroy()

            case "menuEdition":
                menuEditionFrame.destroy()
                etatJeu="menuPrincipal"

            case "menuSolo":
                menuSoloFrame.destroy()
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

            case _: exit_mode() #Si nous ne somme dans aucun menu alors nous somme dans un mode de jeu.

def exit_mode(): #Fonction pour s'avoir dans quel mode de jeu nous somme.
    global etatJeu
    match etatJeu:
        case "editeur": exit_editeur()
        case "solo": exit_solo()
        case "test_editeur": exit_test_editeur()

def close_menu(): #Fonction pour cacher les menu à l'entrée d'un mode de jeu.
    menuPrincipalFrame.place_forget()
    match etatJeu:
        case "editeur": menuEditionFrame.place_forget()
        case "solo": menuSoloFrame.place_forget()
        case "test_editeur": menuEditionFrame.place_forget()


################################################################### Fonctions de lancement des modes ###################################################################

def lancement_editeur(id): #Fonction du lancement de l'éditeur.
    global id_monde, id_level, etatJeu, fenetre_editeur, message_editeur, numeroNiveau, boutonGomme, textTypeBlocSelect, scrolledIDListe
    etatJeu = "editeur" #Changement de l'état du jeu a "editeur". Cela permet d'activer les autres fonctions destiner a l'éditeur
    close_menu() #Appel de la fonction close_menu
    set_grille_fond() #Appel de la fonction set_grille_fond
    id_monde = id #id_monde = id du monde souhaiter dans le menu de l'éditeur
    get_monde(id_monde) #Appel de la fonction get_monde
    id_level = [0,0] #id_level est mis à [0,0] ce qui correspond au niveau de base
    get_niveau(id_level) #Appel de la fonction get_niveau
    affichage_niveau() #Appel de la fonction affichage_niveau

    #Fenetre des infos / boutons
    fenetre_editeur = tk.Toplevel() #Création de la fenetre des fonction/boutons de l'éditeur
    fenetre_editeur.geometry("%dx%d%+d%+d" % (300*ratioFenetre,700*ratioFenetre,50,50)) #taille 1 bouton = taille que tu veux + 3 
    fenetre_editeur.resizable(False,False) #Fenetre non redimentionable
    fenetre_editeur.attributes('-topmost',1) #Fenetre toujours au premier plan
    fenetre_editeur.protocol("WM_DELETE_WINDOW", disable_event) #Fenetre non detruisable manuelement
    fenetre_editeur.config(background='#ffffff') #Couleur du fond de la fenetre = noir
    fenetre_editeur.iconbitmap(lienIconeFenetre) #Set de l'icone du jeu sur la fenetre de l'éditeur

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
    Button(fenetre_editeur, image=imageBoutonEditeurInfos, relief='groove', bd=0, bg='#ffffff', command=info_editeur).place(x=ratioImage/2,y=ratioImage/2, anchor=CENTER) #bouton_edit
    message_editeur = Label(fenetre_editeur, text="", font=("Noto Mono", int(25*ratioFenetre)), bg='#ffffff' ) #Affiche du type de bloc / erreur / info général
    message_editeur.place(x=ratioImage+ratioImage/2,y=ratioImage*6+ratioImage/2, anchor=CENTER) #message_editeur

    Label(fenetre_editeur, text="Edit Object", font=("Noto Mono", int(32*ratioFenetre)), bg="white").place(x=ratioImage*2+ratioImage/2+300*ratioFenetre,y=20*ratioFenetre, anchor=CENTER)
    Label(fenetre_editeur, text="Type Bloc : ", font=("Noto Mono", int(24*ratioFenetre)), bg="white").place(x=325*ratioFenetre, y=65*ratioFenetre)
    textTypeBlocSelect = Label(fenetre_editeur, text="None", font=("Noto Mono", int(24*ratioFenetre)), bg="white")
    textTypeBlocSelect.place(x=575*ratioFenetre, y=65*ratioFenetre)

    Label(fenetre_editeur, text="Liste ID", font=("Noto Mono", int(28*ratioFenetre)), bg="white").place(x=ratioImage*2+ratioImage/2+300*ratioFenetre,y=325*ratioFenetre, anchor=CENTER)

    scrolledIDListe = tkinter.scrolledtext.ScrolledText(master = fenetre_editeur,wrap = tk.WORD,width = int(60*ratioFenetre),height = int(20*ratioFenetre), font=(int(14*ratioFenetre)))
    scrolledIDListe.place(x=300*ratioFenetre,y=350*ratioFenetre)

def lancement_solo(id): #Fonction du lancement du solo.
    global id_monde, id_level, etatJeu, positionJoueur, joueur, temps, theKey
    etatJeu = "solo" #Changment de l'état jeu à "solo". Les fonctions du solo (comme les mouvement) vont pouvoir etre exécuter.
    id_monde = id #id_monde = id du monde souhaiter dans le menu du solo
    theKey = "" #reset de theKey pour ne pas casser les déplacement
    get_monde(id_monde) #Appel de la fonction get_monde
    try: id_level = [monde["lastCoords"][1][0], monde["lastCoords"][1][1]] #Si le monde à déjà été commancer, le dernier niveau est charger
    except: id_level = [0,0] #Sinon on commancer sur le premier
    get_niveau(id_level) #Appel de la fonction get_niveau
    for bloc in monde["niveaux"][niveau]: #Cherche si un bloc d'apparition du joueur existe dans le niveau [0,0] pour faire aparaitre 
        if bloc["type"] == 1: #Si il existe, les coordonées d'apparition sont mis à jour
            posjxstart = bloc["x"]
            posjystart = bloc["y"]
            break #Quand les coordonnées sont trouver, la boucle s'arrete pour ne pas chercher des coordonnées pour rien
    try: #Si le monde à déjà été commancer, les dernière coordonnées sont charger.
        posjxstart = monde["lastCoords"][0][0]
        posjystart = monde["lastCoords"][0][1]
    except: pass
    try: #Si tout est bon, le monde ce lance.
        posjxstart
        close_menu() #Appel de la fonction close_menu.
        affichage_niveau() #Appel de la fonction affichage_niveau.
        temps = 0 #Set du temps à 0.
        chrono() #Appel de la fonction chrono.
        set_direction() #Appel de la fonction set_direction.
        joueur = canevas.create_rectangle(0, 0, nombrePixelX, nombrePixelY, fill='blue', width=0) #Création du joueur
        canevas.moveto(joueur,posjxstart*nombrePixelX, posjystart*nombrePixelY) #Déplacement du joueur au coordonnées d'apparition
        positionJoueur = [posjxstart, posjystart] #0 = x & 1 = y #Actualisation des position du joueur sur la grille
    except: #Sinon, le monde ne se lance pas.
        etatJeu = "menuSolo"
        tkinter.messagebox.showerror("Erreur", "Il n'y a pas de bloc d'apparition dans ce monde") #Affichage d'un message d'erreur

def lancement_test_edition(id): #Fonction du lancement du mode de teste de l'éditeur
    global id_level, etatJeu, joueur, positionJoueur, temps, theKey, freezeEscape
    etatJeu = "test_editeur"
    originalPath = racine+"assets/data/editeur/monde"+str(id)+".gac" #"originalPath" contient le lien du dossier éditeur
    copyPath = racine+"assets/data/test_editeur/monde"+str(id)+".gac" #"copyPath" contient le lien du dossier test_editeur où vont etre copier les fichier de l'éditeur pour ne pas modifier les fichier dans l'éditeur
    if os.path.exists(originalPath): #Si le dossier contient déjà quelque chose, il est détruit puis recréer 
        shutil.copy(originalPath, copyPath)
    id_monde = id #id_monde = id du monde souhaiter dans le menu du solo
    theKey = "" #reset de theKey pour ne pas casser les déplacement
    get_monde(id_monde) #Appel la fonction get_monde
    try: id_level = [monde["lastCoords"][1][0], monde["lastCoords"][1][1]]
    except: id_level = [0,0]
    get_niveau(id_level)
    for bloc in monde["niveaux"][niveau]: #Cherche si un bloc d'apparition du joueur existe dans le niveau [0,0] pour faire aparaitre 
        if bloc["type"] == 1: #Si il existe, les coordonées d'apparition sont mis à jour
            posjxstart = bloc["x"]
            posjystart = bloc["y"]
            break #Quand les coordonnées sont trouver, la boucle s'arrete pour ne pas chercher des coordonnées pour rien
    try:
        posjxstart
        close_menu() #Appel de la fonction close_menu.
        affichage_niveau() #Appel de la fonction affichage_niveau
        temps = 0 #Set du temps à 0
        chrono() #Appel de la fonction chrono
        set_direction() #Set_direction
        joueur = canevas.create_rectangle(0, 0, nombrePixelX, nombrePixelY, fill='blue', width=0) #Création du joueur
        canevas.moveto(joueur,posjxstart*nombrePixelX, posjystart*nombrePixelY) #Déplacement du joueur au coordonnées d'apparition
        positionJoueur = [posjxstart, posjystart] #0 = x & 1 = y #Actualisation des position du joueur sur la grille
        freezeEscape = False #Réactivation du retour via "échap"
    except: #Sinon le lancement est anuler
        etatJeu = "menuEdition"
        tkinter.messagebox.showerror("Erreur", "Il n'y a pas de bloc d'apparition dans ce monde") #Affichage d'un message d'erreur

def exit_editeur(): #Fonction pour sortir de l'édtieur
    global etatJeu, etatEditeur
    del_grille_fond() #Appel de la fonction del_grille_fond
    save(id_monde) #Appel de la fonction save
    cacher_niveau() #Appel de la fonction cacher_niveau
    fenetre_editeur.destroy()
    if etatEditeur == "edit":
        etatEditeur = "pose"
    etatJeu="menuEdition"
    menuPrincipalFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)
    menuEditionFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER)

def exit_solo(): #Fonction pour quitter le mode solo
    global etatJeu, monde, toggleMouvement
    calcul_temps()
    #monde["lastCoords"][id_monde-1] = [[int(str(positionJoueur[0])),int(str(positionJoueur[1]))], id_level]
    monde["lastCoords"] = [[int(str(positionJoueur[0])), int(str(positionJoueur[1]))], [id_level[0], id_level[1]]]
    save(id_monde) #Apple de la fonction save
    cacher_niveau() #Appel de la fonction cacher_niveau
    fenetre.after_cancel(boucleTemps) #Arrête la boucle tu chrono
    fenetre.after_cancel(boucleDirection) #Arrête la boucle qui change la direction
    menuPrincipalFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER) #Place le menu principal
    menuSoloFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER) #Place le menu du Solo
    canevas.delete(joueur) #Supprime le joueur
    etatJeu = "menuSolo" #Changement de l'état jeu
    if toggleMouvement: #Permet de désactiver le mouvement si il y a
        toggleMouvement = False
    positionJoueur.clear()

def exit_test_editeur(): #Fonction pour quitter le mode de teste de l'éditeur
    global etatJeu, freezeEscape
    save(id_monde) #Appel de la fonction save
    cacher_niveau() #Appel de la fonction cacher_niveau
    etatJeu="menuEdition" #Changement de l'état jeu
    menuPrincipalFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER) #Affichage du menu principal
    menuEditionFrame.place(x=largeurFenetre/2, y=hauteurFenetre/2,anchor=CENTER) #Affichage du menu edition
    canevas.delete(joueur) #Suppretion du joueur
    positionJoueur.clear()
    freezeEscape = True

################################################################### Fonctions du mode édition ###################################################################

def type_bloc(tBloc): #Fonction qui permet de selectionner le type de bloc à poser
    global typeDuBloc, couleurBloc, message_editeur
    if tBloc == "solide":
        typeDuBloc = 0 #type = 0 donc le bloc est solide
        couleurBloc = 'black'
        message_editeur.config(text="Bloc solide")

    elif tBloc == "spawn":
        if id_level == [0,0]:
            typeDuBloc = 1 #type = 1 donc le bloc est le bloc d'apparition
            couleurBloc = 'cyan'
            message_editeur.config(text="Bloc spawn")
        else:
            message_editeur.config(text="[0,0] only")
            typeDuBloc = 0
            couleurBloc = 'black'

    elif tBloc == "key":
        typeDuBloc = 2 #type = 2 donc le bloc est une clé
        couleurBloc = 'orange'
        message_editeur.config(text="Item clé")

    elif tBloc == "porte":
        typeDuBloc = 3 #type = 3 donc le bloc est une porte
        couleurBloc = 'orange'
        message_editeur.config(text="Bloc porte")

    elif tBloc == "tp":
        typeDuBloc = 4 #type = 4 donc le bloc est un téléporteur
        couleurBloc = 'white'
        message_editeur.config(text="Bloc TP")
    
    elif tBloc == "finish":
        typeDuBloc = 5 #type = 5 donc le bloc est le bloc de fin
        couleurBloc = 'red'
        message_editeur.config(text="Bloc de fin")

def clic_gauche (event): #Fonction qui calcul la position de la souris sur la grille et appel d'autre fonctions
    if etatJeu == "editeur":
        xSourisGrille,ySourisGrille=event.x,event.y

        #Calcul de la position de la souris sur la grille invisible du jeu
        xSourisGrille = (xSourisGrille/nombrePixelX)
        xSourisGrille = int(xSourisGrille) 

        ySourisGrille = (ySourisGrille/nombrePixelY)
        ySourisGrille = int(ySourisGrille)

        match etatEditeur: #Appel de la fonction souhaiter en fonction de l'état de l'éditeur
            case "pose": pose_bloc(xSourisGrille,ySourisGrille)
            case "gomme": gomme(xSourisGrille,ySourisGrille)
            case "edit": edit_bloc(xSourisGrille,ySourisGrille)

def pose_bloc(x,y): #Fonction pour poser un bloc
    global monde
    indexBloc = 0 #Index du bloc dans la liste des blocs
    for bloc in monde["niveaux"][niveau]: #Si le bloc que l'on veut poser existe déjà, le nouveau ne peut pas etre poser
        if bloc["x"] == x and bloc ["y"] == y:
            return
        if bloc["type"] == 1 and typeDuBloc == 1 or bloc["type"] == 5 and typeDuBloc == 5: #Si le bloc est un bloc d'apparition ou de fin, l'ancien bloc est suprimer
            canevas.delete(bloc["idTk"])
            del monde["niveaux"][niveau][indexBloc]
        indexBloc += 1
    demiPixelX = 0
    demiPixelY = 0
    if typeDuBloc == 2: #Si le bloc est une clé, la taille est modifier
        demiPixelX = nombrePixelX/4
        demiPixelY = nombrePixelY/4
    if typeDuBloc == 1 and id_level != [0,0]:
        type_bloc("spawn")
    monde["niveaux"][niveau].append({"idAssoc" : 0, "idTk":canevas.create_rectangle(x*nombrePixelX+demiPixelX, y*nombrePixelY+demiPixelY, x*nombrePixelX+nombrePixelX-demiPixelX, y*nombrePixelY+nombrePixelY-demiPixelY, fill=couleurBloc), "x":x, "y":y, "type":typeDuBloc, "couleur":couleurBloc, "collect":0}) #Création du bloc
    save(id_monde) #Appel de la fonction pour poser le bloc

def del_last_bloc(): #Fonction pour supprimer les derniers blocs poser
    global monde
    if etatJeu == "editeur" and len(monde["niveaux"][niveau]) > 0:
        canevas.delete(monde["niveaux"][niveau][-1]["idTk"]) #Destruction du dernier bloc de la liste
        del monde["niveaux"][niveau][-1]
        save(id_monde)

def del_all_blocs(): #Fonciton pour détruire tous les blocs
    global monde
    cacher_niveau() #Destruction de l'affichage
    monde["niveaux"][niveau] = list() #Suppression des blocs exitants dans la liste du niveau
    save(id_monde)

def del_all_level(): #Fonciton pour détruire tous les niveau d'un monde
    global monde, id_level
    attention = tkinter.messagebox.askyesno("Attention", "Voulez vous détruire tout les blocs de ce niveau ?") #message d'alerte
    if attention:
        cacher_niveau() #Destruction de l'affichage
        for niveauTest in monde["niveaux"]:
            monde["niveaux"][niveauTest].clear() #Suppretion des blocs dans les niveaux
        id_level = [0,0]
        save(id_monde)

def toggle_gomme(): #Fonction pour activer la gomme
    global etatEditeur, boutonGomme
    if etatEditeur != "gomme" and etatEditeur != "edit":
        etatEditeur = "gomme"
        boutonGomme.configure(image = imageBoutonEditeurGommeSelect)
    elif etatEditeur == "gomme":
        etatEditeur = "pose"
        boutonGomme.configure(image = imageBoutonEditeurGomme)

def gomme(x,y): #Fonction pour détruire un bloc viser
    if etatJeu == "editeur":
        indexBloc = 0
        for bloc in monde["niveaux"][niveau]:
            if bloc["x"] == x and bloc["y"] == y: #Si bloc dans la liste correspond aux coordonnées de la souris, le bloc est détruit
                canevas.delete(bloc["idTk"])
                del monde["niveaux"][niveau][indexBloc]
                break
            indexBloc += 1

def set_edit(): #Fonction pour activer / désactiver le mode d'édition de bloc
    global etatEditeur
    if etatEditeur == "pose":
        etatEditeur = "edit"
        fenetre_editeur.geometry("%dx%d" % (800*ratioFenetre,700*ratioFenetre)) #Agrandissement de la fenetre

    elif etatEditeur == "edit":
        etatEditeur = "pose"
        fenetre_editeur.geometry("%dx%d" % (300*ratioFenetre,700*ratioFenetre)) #Taille de la fenetre normal

def edit_bloc(x,y): #Fonction de l'édition de bloc (partie selection)
    global selectBloc, selectNiveau
    for bloc in monde["niveaux"][niveau]:
        if bloc["x"] == x and bloc["y"] == y: #une fois le bloc trouver, on regarde le type
            selectNiveau = niveau
            selectBloc = bloc
            match bloc["type"]:
                case 0: #Si le type est 0, le bloc ne peut pas être modifier
                    textTypeBlocSelect.config(text="Bloc Solide")
                    config_edit(0)
                case 1: #Si le type est 1, le bloc ne peut pas être modifier
                    textTypeBlocSelect.config(text="Bloc Spawn")
                    config_edit(1)
                case 2: #Si le type est 2, le bloc peut être modifier
                    textTypeBlocSelect.config(text="Item Clé")
                    config_edit(2)
                case 3: #Si le type est 2, le bloc peut être modifier
                    textTypeBlocSelect.config(text="Bloc Porte")
                    config_edit(3)
                case 4: #Si le type est 2, le bloc peut être modifier
                    textTypeBlocSelect.config(text="Bloc TP")
                    config_edit(4)
                case 5: textTypeBlocSelect.config(text="Bloc de fin") #Si le type est 1, le bloc ne peut pas être modifier
            break

def config_edit(typeB): #Fonction de l'édition de bloc (partie modification)
    global entryIDcle,boutonIDCleValidation,couleurSet,textIDKey,textIDTP1,textIDTP2,entryID1,entryID2,boutonIDTPValidation, textTypeBlocSelect, scrolledIDListe, listeIDUsed
    try: #La fenetre d'édition est mise a jour à chaque fois qu'un bloc est selctionner, donc si le bloc ne peut pas être modifier, les paramètre doivent etre détruit
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

    if typeB == 2 or typeB == 3: #Si le type est une clé ou une porte
        entryIDcle = Entry(fenetre_editeur, bg="lightgrey", width=int(10*ratioFenetre), font=("Noto Mono", int(24*ratioFenetre))) #Entrée de texte pour l'id de la clé
        entryIDcle.place(x=575*ratioFenetre, y=110*ratioFenetre)
        boutonIDCleValidation = Button(fenetre_editeur, image=imageOK, relief='groove', bd=0, bg='black', command=get_key) #Bouton de validation
        boutonIDCleValidation.place(x=325*ratioFenetre,y=175*ratioFenetre)
        textIDKey = Label(fenetre_editeur, text="ID :", font=("Noto Mono", int(24*ratioFenetre)), bg="white")
        textIDKey.place(x=430*ratioFenetre,y=110*ratioFenetre) 
        couleurSet = Scale(fenetre_editeur, orient='horizontal', from_=1, to=7, resolution=1, tickinterval=2, length=180*ratioFenetre, label='Couleur', font=("Noto Mono", int(10*ratioFenetre)), bg="white", command=change_color) #Zone de changement de couleur
        couleurSet.place(x=575*ratioFenetre,y=150*ratioFenetre)
    elif typeB == 4: #Si le type est un téléporteur
        textIDTP1 = Label(fenetre_editeur, text="ID départ", font=("Noto Mono", int(24*ratioFenetre)), bg="white")
        textIDTP1.place(x=400*ratioFenetre,y=130*ratioFenetre,anchor=CENTER)
        textIDTP2 = Label(fenetre_editeur, text="ID arrivée", font=("Noto Mono", int(24*ratioFenetre)), bg="white")
        textIDTP2.place(x=700*ratioFenetre,y=130*ratioFenetre,anchor=CENTER)
        entryID1 = Entry(fenetre_editeur, bg="lightgrey", width=int(10*ratioFenetre), font=("Noto Mono", int(24*ratioFenetre))) #Entrée de texte pour l'id du bloc
        entryID1.place(x=400*ratioFenetre, y=210*ratioFenetre,anchor=CENTER)
        entryID2 = Entry(fenetre_editeur, bg="lightgrey", width=int(10*ratioFenetre), font=("Noto Mono", int(24*ratioFenetre))) #Entrée de texte pour l'id de destination
        entryID2.place(x=700*ratioFenetre, y=210*ratioFenetre,anchor=CENTER)
        boutonIDTPValidation = Button(fenetre_editeur, image=imageOK, relief='groove', bd=0, bg='black', command=get_tp) #Bouton de validation
        boutonIDTPValidation.place(x=550*ratioFenetre,y=240*ratioFenetre,anchor=CENTER)
    calcul_id_utilise() #Appel de la fonctoin calcul_id_utilise
    scrolledIDListe.delete("1.0","end") #Remise a 0 de la l'affichage des id utilisé
    for i in range(len(listeIDUsed)): #Affichage des id utilisé
        scrolledIDListe.insert(tk.INSERT,"ID : "+str(listeIDUsed[i]["idAssoc"])+", Type : "+str(listeIDUsed[i]["type"])+", Couleur : "+str(listeIDUsed[i]["couleur"])+", Niveau : "+str(listeLevelIDUsed[i])+"\n", listeIDUsed[i]["couleur"])
        colorTextID = listeIDUsed[i]["couleur"]
        if colorTextID == "white":
            colorTextID = "black"
        scrolledIDListe.tag_config(listeIDUsed[i]["couleur"], foreground=colorTextID)

def get_key(): #Fonction pour récupérer l'id donner à une clé
    global monde
    indexBloc = 0
    if not entryIDcle.get() or not entryIDcle.get().isnumeric(): #La valeur doit être numérique et non nul
        message_editeur.config(text="Entier requi")
        return
    id = int(entryIDcle.get()) #Si la valeur est float, elle est arondi à l'entier le plus bas
    for bloc in monde["niveaux"][niveau]:
        if bloc["x"] == selectBloc["x"] and bloc["y"] == selectBloc["y"]:
            monde["niveaux"][niveau][indexBloc]["idAssoc"] = id #Mise a jour de l'id
        indexBloc += 1

def get_tp(): #Fonction pour récupérer l'id donner à un téléporteur
    global monde, message_editeur
    indexBloc = 0
    if not entryID1.get() or not entryID2.get() or not entryID1.get().isnumeric() or not entryID2.get().isnumeric(): #La valeur doit être numérique et non nul
        message_editeur.config(text="Entier requi")
        return
    id = [int(entryID1.get()), int(entryID2.get())] #Si la valeur est float, elle est arondi à l'entier le plus bas
    for bloc in monde["niveaux"][niveau]:
        if bloc["x"] == selectBloc["x"] and bloc["y"] == selectBloc["y"]:
            monde["niveaux"][niveau][indexBloc]["idAssoc"] = id #Mise a jour de l'id
        indexBloc += 1

def change_color(c): #Fonction pour changé la couleur du bloc selectionner
    global monde
    match couleurSet.get(): #Lecture de la couleur choisi
        case 1: newColorBloc = 'orange'
        case 2: newColorBloc = 'yellow'
        case 3: newColorBloc = 'green'
        case 4: newColorBloc = 'blue'
        case 5: newColorBloc = 'pink'
        case 6: newColorBloc = 'purple'
        case 7: newColorBloc = 'brown'

    indexBloc = 0
    for bloc in monde["niveaux"][niveau]: #Modification de la couleur
        if bloc["x"] == selectBloc["x"] and bloc["y"] == selectBloc["y"]:
            monde["niveaux"][niveau][indexBloc]["couleur"] = newColorBloc
            canevas.itemconfig(bloc["idTk"], fill=bloc["couleur"])
            save(id_monde)
            break
        indexBloc += 1

def calcul_id_utilise(): #Fonction pour lister les id utiliser
    global listeIDUsed, listeLevelIDUsed
    listeIDUsed = []
    listeLevelIDUsed = []
    for niveauTest in monde["niveaux"]: #Liste tout les id utiliser dans le monde pour les répertorier dans l'affichage des id
        for bloc in monde["niveaux"][niveauTest]:
            if bloc["type"] == 2 or bloc["type"] == 3 or bloc["type"] == 4:
                listeIDUsed.append(bloc)
                listeLevelIDUsed.append(niveauTest)


################################################################### Fonctions du Solo ###################################################################

def on_key_pressed(k): #Fonction qui assigne à theKey la touche enfoncer
    global theKey
    theKey = k.char

def on_key_released(k): #Fonction qui permet d'arreter un mouvement si la bonne touche est relacher
    global toggleMouvement, theKey
    if etatJeu == "solo" or etatJeu == "test_editeur":
        if k.char == theKey:
            theKey = ""
            toggleMouvement = False
            fenetre.after_cancel(boubleMouvement) #Stop la boucle de mouvement

def set_direction(): #Fonction qui donne la direction à prendre en fonction du français
    global direction_mouvement, toggleMouvement, boucleDirection
    if etatJeu == "solo" or etatJeu == "test_editeur":
        direction_mouvement = directionsBinds.get(theKey) #La direction est donnée par le dictionnaire "directionsBinds"
        if not toggleMouvement:
            if directionsBinds.get(theKey) is not None:
                toggleMouvement = True
                mouvement_joueur() #Appel de la fonction mouvement
        boucleDirection = fenetre.after(1, set_direction)

def mouvement_joueur(): #Fonction pour déplacer le joueur
    global positionJoueur, joueur, id_level, boubleMouvement
    if direction_mouvement == "up": #Si la direction est egale à "up"
        posJTestX = positionJoueur[0] #Test de la prochaine position du joueur dans la grille pour x
        posJTestY = positionJoueur[1]-1 #Test de la prochaine position du joueur dans la grille pour y
        xyJ = 1 #Indique quel est l'axe qui est demander (0=x et 1=y)
        posJF = -1 #Donne de combien doit être changer les coordonnées du joueur en fonction de l'axe
        posMax = 0 #Donne la position max du joueur sur la grille 
        deplacement = [0, -nombrePixelY] #Donne de combien le joueur doit ce déplacer sur la grille
        tp = [positionJoueur[0],nombreCaseY-1]

    elif direction_mouvement == "down":
        posJTestX = positionJoueur[0]
        posJTestY = positionJoueur[1]+1
        xyJ = 1
        posJF = +1
        posMax = nombreCaseY-1
        deplacement = [0, +nombrePixelY]
        tp = [positionJoueur[0],0]

    elif direction_mouvement == "left":
        posJTestX = positionJoueur[0]-1
        posJTestY = positionJoueur[1]
        xyJ = 0
        posJF = -1
        posMax = 0
        deplacement = [-nombrePixelX, 0]
        tp = [nombreCaseX-1,positionJoueur[1]]

    elif direction_mouvement == "right":
        posJTestX = positionJoueur[0]+1
        posJTestY = positionJoueur[1]
        xyJ = 0
        posJF = +1
        posMax = nombreCaseX-1
        deplacement = [+nombrePixelX, 0]
        tp = [0,positionJoueur[1]]
    else: return

    indexBloc = 0
    ok = True
    for bloc in monde["niveaux"][niveau]: #Recherche du type du bloc
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

    if ok:
        if positionJoueur[xyJ] == posMax: #Si la position du joueur est egale à la limite de l'écran (ou de la map)
            id_level[xyJ] = id_level[xyJ]+int(posJF)
            cacher_niveau()
            get_niveau(id_level) #La fonction level_search est appeler
            affichage_niveau()
            positionJoueur = tp
            canevas.moveto(joueur,tp[0]*nombrePixelX,tp[1]*nombrePixelY)
        else:
            canevas.move(joueur, deplacement[0], deplacement[1]) #Le joueur est déplacer sur la case demander
            positionJoueur[xyJ] = positionJoueur[xyJ]+posJF #Les coordonnées du joueur sont actualiser
    boubleMouvement = fenetre.after(45, mouvement_joueur) #Boucle de la fonction

def ramasse_cle(indexBloc): #Fonction pour récupérer une clé
    global monde
    monde["niveaux"][niveau][indexBloc]["collect"] = 1
    canevas.delete(monde["niveaux"][niveau][indexBloc]["idTk"])

def ouvre_porte(indexBloc): #Fonction pour ouvrir une porte
    global monde
    for niveauTest in monde["niveaux"]:
        for bloc in monde["niveaux"][niveauTest]:
            if bloc["type"] == 2 and bloc["collect"] == 1 and bloc["idAssoc"] == monde["niveaux"][niveau][indexBloc]["idAssoc"]:
                monde["niveaux"][niveau][indexBloc]["collect"] = 1
                canevas.delete(monde["niveaux"][niveau][indexBloc]["idTk"]) #Destruction de la porte
                return True
    return False

def tp_joueur(indexBloc): #Fonction pour téléporter le joueur
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
                        canevas.moveto(joueur,positionJoueur[0]*nombrePixelX,positionJoueur[1]*nombrePixelY)
                        return
                except: return

def fin_niveau(): #Fonction pour mettre fin à un monde
    global monde, etatJeu, messageScore, pbPlayer
    if etatJeu == "solo":
        exit_solo() #Sortie du solo
        etatJeu = "solo"
        if monde["reset"][id_monde-1]: #Si le reset du niveau à été effectuer, le score est calculer et sauvgarder
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
        print(pbPlayer)

def chrono(): #Fonction du chrono
    global temps, boucleTemps
    temps += 1
    boucleTemps = fenetre.after(1000, chrono)

def calcul_temps(): #Fonction pour calculer le temps mis a faire un monde
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

def get_monde(id): #Permet de tourver le monde à charger
    global monde
    dossier_data = racine + "assets/data/"
    match etatJeu:
        case "editeur": dossier = dossier_data + "editeur/monde"+str(id)+".gac"
        case "solo": dossier = dossier_data + "solo/monde"+str(id)+".gac"
        case "test_editeur": dossier = dossier_data + "test_editeur/monde"+str(id)+".gac"
    with open(dossier, "rb") as fichierMonde:
        monde = pickle.load(fichierMonde)

def get_list_niveau(niveauTest): #Fonction pour récupérer l'id_level d'un str
    global id_level
    id_level = [int(niveauTest.split(",")[0]),int(niveauTest.split(",")[1])]

def set_grille_fond(): #Affiche la grille de l'éditeur
    ######################################################################## Le cadirage
    ligneCreer_x = nombrePixelX #Variable qui renseigne à quel x les lignes du cadriage doivent être placer
    ligneCreer_y = nombrePixelY #Variable qui renseigne à quel y les lignes du cadriage doivent être placer

    #Création des ligne de l'éditeur (le cadriage dans le fond qui permet de mieux savoir où les blocs seront placer)
    while ligneCreer_x <= largeurFenetre: #Temps que la bordure de l'écran n'est pas attein les lignes sont placer
        ligneX.append(canevas.create_line(ligneCreer_x, 0, ligneCreer_x, hauteurFenetre)) #Crée une ligne vertical en fonction de "ligneCreer_x"
        ligneCreer_x += nombrePixelX #Ajout du nombre de pixel n'esaissaire entre 2 ligne (la taille d'un bloc)

    while ligneCreer_y <= hauteurFenetre: #Temps que la bordure de l'écran n'est pas attein les lignes sont placer
        ligneY.append(canevas.create_line(0, ligneCreer_y, largeurFenetre, ligneCreer_y)) #Crée une ligne horizontal en fonction de "ligneCreer_y"
        ligneCreer_y += nombrePixelY #Ajout du nombre de pixel n'esaissaire entre 2 ligne (la taille d'un bloc)

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
        demiPixelX = 0
        demiPixelY = 0
        if bloc["type"] == 2:
            demiPixelX = nombrePixelX/4
            demiPixelY = nombrePixelY/4
        if bloc["collect"] == 0:
            monde["niveaux"][niveau][indexBloc]["idTk"] = (canevas.create_rectangle(bloc["x"]*nombrePixelX+demiPixelX, bloc["y"]*nombrePixelY+demiPixelY, bloc["x"]*nombrePixelX+nombrePixelX-demiPixelX, bloc["y"]*nombrePixelY+nombrePixelY-demiPixelY, fill=couleurBloc))
        indexBloc += 1
    couleurBloc = 'black'

def cacher_niveau(): #Masque le niveau
    for bloc in monde["niveaux"][niveau]:
        canevas.delete(bloc["idTk"])

def supp_niveau(): #Fonction pour supprimer un niveau
    global monde
    del monde["niveaux"][niveau]

def save(id): #Fonction pour sauvegarder un monde
    global monde
    dossier_data = racine + "assets/data/"
    match etatJeu:
        case "editeur": dossier = dossier_data + "editeur/monde"+str(id)+".gac"
        case "solo": dossier = dossier_data + "solo/monde"+str(id)+".gac"
        case "test_editeur": dossier = dossier_data + "test_editeur/monde"+str(id)+".gac"
    with open(dossier, "wb") as fichierMonde: #Save dans le fichier
        pickle.dump(monde, fichierMonde)

def change_level(direction): #Fonction pour changer de niveau
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

def toggle_reset(): #Fonction pour activer / désactiver le reset des monde du solo
    global boutonSoloMonde1, boutonSoloMonde2, boutonSoloMonde3, commandMondeSolo, exitCommand, boutonExitSolo, freezeEscape
    if commandMondeSolo != reset_solo:
        commandMondeSolo = reset_solo #Changement de fonction sur les bouton
        exitCommand = ""
        boutonSoloMonde1.config(image=imageMonde1Del) #Changement des images
        boutonSoloMonde2.config(image=imageMonde2Del)
        boutonSoloMonde3.config(image=imageMonde3Del)
        boutonSoloReset.config(image=imageResetSoloToggle)
        boutonExitSolo.config(image=imageNotExit, command=exitCommand)
        freezeEscape = True
    else:
        commandMondeSolo = lancement_solo
        exitCommand = exit_menu
        boutonSoloMonde1.config(image=imageMonde1)
        boutonSoloMonde2.config(image=imageMonde2)
        boutonSoloMonde3.config(image=imageMonde3)
        boutonSoloReset.config(image=imageResetSolo)
        boutonExitSolo.config(image=imageExit, command=exitCommand)
        freezeEscape = False

def reset_solo(n): #Fonction pour reset un monde du solo
    global monde
    attention = tkinter.messagebox.askyesno("Attention", "Voulez-vous réinitialisez se monde ?")
    if attention:
        originalPath = racine+"assets/data/origine/monde"+str(n)+".gac"
        copyPath = racine+"assets/data/solo/monde"+str(n)+".gac"
        shutil.copy(originalPath, copyPath)
        monde["reset"][n-1] = True
        toggle_reset()

def toggle_test_editeur(): #Fonction pour activer / désactiver le test mode de l'éditeur
    
    global boutonEditeurMonde1, boutonSoloMonde2, boutonSoloMonde3, commandMondeEditeur, exitCommand, boutonExitEdit, freezeEscape
    if commandMondeEditeur != lancement_test_edition:
        commandMondeEditeur = lancement_test_edition
        exitCommand = ""
        boutonEditeurMonde1.config(image=imageMonde1Test)
        boutonEditeurMonde2.config(image=imageMonde2Test)
        boutonEditeurMonde3.config(image=imageMonde3Test)
        boutonEditPlayTest.config(image=imageBoutonPlayTestToggle)
        boutonExitEdit.config(image=imageNotExitTest, command=exitCommand)
        freezeEscape = True
    else:
        commandMondeEditeur = lancement_editeur
        exitCommand = exit_menu
        boutonEditeurMonde1.config(image=imageMonde1)
        boutonEditeurMonde2.config(image=imageMonde2)
        boutonEditeurMonde3.config(image=imageMonde3)
        boutonEditPlayTest.config(image=imageBoutonPlayTest)
        boutonExitEdit.config(image=imageExit, command=exitCommand)
        freezeEscape = False

def wip():
    tkinter.messagebox.showinfo("WIP", "Work In Progress")


################################################################### Autre ###################################################################
start()