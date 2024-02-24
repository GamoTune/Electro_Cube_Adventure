from tkinter import *


def move(event):
    global img
    global image_editeur
    global image_in

    x1,y1,x2,y2=canevas.bbox("ball")
    canevas.moveto(image_editeur,event.x-100/2,event.y-100/2)
    print(canevas.coords(case1)[0])
    print(canevas.coords(image_editeur)[0])
    
    if canevas.coords(case1)[0] <= canevas.coords(image_editeur)[0]+100/2 <canevas.coords(case1)[0]+taille and canevas.coords(case1)[1] <= canevas.coords(image_editeur)[1]+100/2 <canevas.coords(case1)[1]+taille:
            canevas.moveto(image_editeur,505,105)
            image_in = 1
            print(image_in)
    else:
        image_in = 0
        print(image_in)




def desto (event):
    fenetre.destroy()




fenetre = Tk()

largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()

fenetre.title('Dessin d\'un rectangle')
fenetre.attributes('-fullscreen', True)
canevas = Canvas(fenetre, width=largeur, height=hauteur,bg='grey')


def creer_carre (event):

    global carreNoirX
    global case1
    global pad
    global img
    global image_editeur
    global ximage

    pad = 0
    while pad != nombreBouton:
        case1 = canevas.create_rectangle(carreNoirX,carreNoirY,carreNoirX+taille,carreNoirY+taille, fill='black')
        carreNoirX += taille+10
        pad += 1
        image_editeur = canevas.create_image(ximage,yimage, anchor=NW,image=img, tags=("ball"))
        ximage += 110





img = PhotoImage(file="assets/images/bouton_editeur.png")

image_in = 0
carreNoirX = 100
carreNoirY = 100
taille = 110
pad = 0
ximage = 500
yimage = 500

nombreBouton = float(input("nombre bouton : "))




fenetre.bind("<B1-Motion>", move)
fenetre.bind("<Escape>", desto)
fenetre.bind("<Key-a>", creer_carre)



canevas.pack()
fenetre.mainloop()