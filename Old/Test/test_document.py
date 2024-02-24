import pickle



# enregistrement fichier
niveau=[14, 1, 15, 1, 16, 1, 17, 1, 18, 1, 19, 1, 20, 1, 21, 1, 22, 1, 23, 1, 24, 1, 25, 1, 25, 2, 25, 3, 25, 4, 25, 5, 25, 6, 24, 6, 24, 7, 25, 7, 25, 8, 25, 9, 24, 9, 23, 9, 22, 9, 21, 9, 20, 9, 19, 9, 18, 9, 17, 9, 16, 9, 15, 9, 14, 9, 14, 8, 14, 7, 14, 6, 14, 5, 14, 4, 14, 3, 14, 2, 17, 3]
with open("F:\\Programmes\\data\\dataNombreMoy.txt", "wb") as fichierNiveau:
    #Répertoir du fichier (exemple : F:\\Programmes\\data\\dataNombreMoy.txt"
    pickle.dump(niveau, fichierNiveau)

#lecture du fichier
with open("F:\\Programmes\\data\\dataNombreMoy.txt", "rb") as infile:
    nouveauNiveau = pickle.load(infile)
print("Reconstructed object", nouveauNiveau)



# le "wb" et "rb" c pour écriture / lecture