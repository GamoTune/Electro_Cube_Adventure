from tkinter import *
def move_left(event):
    x1,y1,x2,y2=c1.bbox("ball")
    if(x1<=0):
        return
    else:
        c1.moveto(ball,event.x,event.y)
        print("Left") #Only for test purpose.Remove if not needed.
def move_right(event):
    x1,y1,x2,y2=c1.bbox("ball")
    if(x2>=c1.winfo_width()-5):
        return
    else:
        c1.moveto(ball,event.x,event.y)
        print("Right")  #Only for test purpose.Remove if not needed.
def move_up(event):
    x1,y1,x2,y2=c1.bbox("ball")
    if(y1<=0):
        return
    else:
        c1.moveto(ball,event.x,event.y) 
        print("Up")    #Only for test purpose.Remove if not needed. 
def move_down(event):
    x1,y1,x2,y2=c1.bbox("ball")
    if(y2>=c1.winfo_height()-5):
        return
    else:
        c1.moveto(ball,event.x,event.y)  
        print("Down")  #Only for test purpose.Remove if not needed.
################## Main Program ####################
root=Tk()
root.title('Move Image')
c1=Canvas(root,bg='white')
image=PhotoImage(file='assets/images/bouton_editeur.png')
ball=c1.create_image(0,0,image=image,anchor=NW,tags=("ball"))
c1.pack(fill="both",expand=True)
root.bind('<B1-Motion>', move_right)
root.bind('<B1-Motion>', move_left)
root.bind('<B1-Motion>', move_up)
root.bind('<B1-Motion>', move_down)
root.mainloop()