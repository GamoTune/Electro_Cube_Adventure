#test_time

import time
from tkinter import *

fenetre = Tk()



def heure():
    global timer_id
    print(time.localtime()[5])
    # Planifie l'exécution de la fonction heure() dans 1000 ms (1 seconde)
    # et récupère son identifiant de planification (timer_id)
    timer_id = fenetre.after(1000, heure)
    
    # Si vous voulez arrêter la boucle après un certain nombre d'itérations, 
    # vous pouvez ajouter une condition de sortie ici (par exemple avec un compteur)
    
    # Si vous voulez arrêter la boucle immédiatement, vous pouvez utiliser un bouton
    # ou une autre action utilisateur pour appeler la fonction suivante :
def stop():
    fenetre.after_cancel(timer_id)


heure()

stop()

fenetre.mainloop()


