import pickle

niveau = {}

numeroNiveau = [0,0]
lien = "assets/data/test.txt"
load = []
Up = 1
y = 0


def up ():
    global load
    global lien
    lien = "assets/data/test"+str(numeroNiveau[0])+str(numeroNiveau[1])+".txt"
    print(lien)
    try:
        with open(lien, "rb") as fichier:
            load = pickle.load(fichier)
        print("lecture du niveau")
    except:
        print("Creation d'un nouveau niveau")
        numeroNiveau[0]+= 1
        save()

def save ():
    with open("assets/data/test"+str(numeroNiveau[0])+str(numeroNiveau[1])+".txt", "wb") as fichierNiveau:
        pickle.dump(Up,fichierNiveau)


up()