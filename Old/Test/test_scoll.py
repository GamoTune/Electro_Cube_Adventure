#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk
import os

fenetre = Tk()

largeurFenetre = 2560
hauteurFenetre = 1440
fenetre.geometry("750x750")

canvas= Canvas(fenetre, width= 750, height= 750)
canvas.pack()


racine = os.getcwd()
racine = racine.replace("\\", "/" )
racine = racine+str("/")




ratioFenetre = largeurFenetre/(2560*2) #Calcule d'un ratio entre la résolution utilisé par l'utilisateur et la résolution utilisé pour mettre en place toutes les position d'image
tailleImage = 100
ratioImage = int(tailleImage*ratioFenetre)








imageBloc = ImageTk.PhotoImage(Image.open(racine+"assets/images/bouton_bloc_solide.png").resize((ratioImage, ratioImage)))

x = 0
y = 0


for i in range(6):
    imageListeID = canvas.create_image(0,75*i,anchor=NW,image=imageBloc)
    IDListeID = Label(canvas, text="ID n° "+str(i), font="Arial, 18").place(x=150,y=75*i+20, anchor=CENTER)
















fenetre.mainloop()