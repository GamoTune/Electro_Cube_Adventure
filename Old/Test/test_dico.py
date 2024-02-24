import pickle


dico1 = {"coordsBlocs" : [], "porte" : [], "tpJoueur" : []}
list1 = [4,4,5,6,7,8]


list2 = []


dico1["coordsBlocs"].append(list1)




def load ():
    global list2
    global dico1


    list2.clear()


    with open("E:\\Programmes\\data\\level_test1.txt", "rb") as fichier:
        dico1 = pickle.load(fichier)
    print(dico1)
    print(dico1["coordsBlocs"])
    list2 = dico1["coordsBlocs"].pop(0)

    print(list2[0])
    


def save ():
    with open("E:\\Programmes\\data\\level_test1.txt", "wb") as fichierNiveau:
        pickle.dump(dico1, fichierNiveau)




save()
load()