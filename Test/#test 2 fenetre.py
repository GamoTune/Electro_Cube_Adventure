#test 2 fenetre

import tkinter as tk

def New_Window():
    Window = tk.Toplevel()
    canvas = tk.Canvas(Window, height=HEIGHT, width=WIDTH)
    canvas.pack()


HEIGHT = 300
WIDTH = 500


ws = tk.Tk()
ws.title("Python Guides")
canvas = tk.Canvas(ws, height=HEIGHT, width=WIDTH)
canvas.pack()

button = tk.Button(ws, text="Click ME", bg='White', fg='Black',command=lambda: New_Window())

button.pack()
ws.mainloop()