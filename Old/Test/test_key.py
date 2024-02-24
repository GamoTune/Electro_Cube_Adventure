from tkinter import *

global tk_root , tk_canvas, theKey, playerX, playerY, playerVx, playerVy

def init_Tk():
    global tk_root, tk_canvas
    tk_root = Tk()
    tk_canvas = Canvas(tk_root, width=900, height=500) 
    tk_canvas.pack()

#___________________________________________________________________________________________________________ 
def init_keys():
    global theKey,upKeyCount
    theKey = "up"
    upKeyCount = 20
    tk_root.bind('<Key>', lambda i: on_key_pressed(i))
    tk_root.bind('<KeyRelease>', lambda i: on_key_released(i))

def on_key_pressed(e):
    global theKey
    theKey = e.char

def on_key_released(e):
    global theKey, upKeyCount
    if e.char == theKey:
        theKey = "up"
#___________________________________________________________________________________________________________ 
def init_player():
    global playerX, playerY, playerVx, playerVy, playerW, playerH, directions,instance_rectangle
    directions = {'z':[0,-1],'q':[-1,0],'d':[1,0],'s':[0,1],'up':[0,0],' ':[0,0]}
    playerX = 0
    playerY = 0
    playerVx = 0
    playerVy = 0
    playerW=10
    playerH=10
    instance_rectangle=tk_canvas.create_rectangle(playerX, playerY, playerX+playerW, playerY+playerW,outline="#000", fill="#000")

#___________________________________________________________________________________________________________ 
def updatePlayer():
    global playerX, playerY, playerVx, playerVy, theKey, instance_rectangle
    vitesse = 0.5
     
    if directions.get(theKey) is not None:
        playerVx = directions[theKey][0]*vitesse
        playerVy = directions[theKey][1]*vitesse

    playerX += playerVx
    playerY += playerVy

    if playerX>tk_root.winfo_width(): playerX=-playerW+1
    if playerX<-playerW: playerX=tk_root.winfo_width()-1
    if playerY>tk_root.winfo_height(): playerY=-playerH+1
    if playerY<-playerH: playerY=tk_root.winfo_height()-1

    tk_canvas.moveto(instance_rectangle,playerX,playerY)
    tk_root.after(1, updatePlayer)
#___________________________________________________________________________________________________________ 
init_Tk()
init_keys()

init_player()
updatePlayer()
tk_root.mainloop()