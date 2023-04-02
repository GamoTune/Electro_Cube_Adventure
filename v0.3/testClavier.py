from tkinter import *

def init_Tk():
    global tk_root, tk_canvas, taille
    tk_root = Tk()
    tk_canvas = Canvas(tk_root, width=900, height=500) 
    tk_canvas.pack()
    taille = 48

#___________________________________________________________________________________________________________ 
def init_keys():
    global theKey
    theKey = "up"
    tk_root.bind('<Key>', lambda k: on_key_pressed(k))
    tk_root.bind('<KeyRelease>', lambda k: on_key_released(k))

def on_key_pressed(k):
    global theKey
    theKey = k.char

def on_key_released(k):
    global theKey
    if k.char == theKey:
        theKey = "up"
#___________________________________________________________________________________________________________ 
def init_player():
    global playerX, playerY, playerVecteurX, playerVecteurY, playerTailleX, playerTailleY, directions, joueur
    directions = {'z':[0,-1],'q':[-1,0],'d':[1,0],'s':[0,1],'up':[0,0],' ':[0,0]}
    playerX = 0
    playerY = 0
    playerVecteurX = 0
    playerVecteurY = 0
    playerTailleX=taille
    playerTailleY=taille
    joueur=tk_canvas.create_rectangle(playerX, playerY, playerX+playerTailleX, playerY+playerTailleX, outline="#000", fill="#000")

#___________________________________________________________________________________________________________ 
def updatePlayer():
    global playerX, playerY, playerVecteurX, playerVecteurY, theKey, joueur
    vitesse = taille

    if directions.get(theKey) is not None:
        playerVecteurX = directions[theKey][0]*vitesse
        playerVecteurY = directions[theKey][1]*vitesse

    playerX += playerVecteurX
    playerY += playerVecteurY

    if playerX>tk_root.winfo_width(): playerX=-playerTailleX+1
    if playerX<-playerTailleX: playerX=tk_root.winfo_width()-1
    if playerY>tk_root.winfo_height(): playerY=-playerTailleY+1
    if playerY<-playerTailleY: playerY=tk_root.winfo_height()-1

    tk_canvas.moveto(joueur,playerX,playerY)
    tk_root.after(35, updatePlayer)
#___________________________________________________________________________________________________________ 
init_Tk()
init_keys()

init_player()
updatePlayer()
tk_root.mainloop()
