# Créé par Malingue_1risc, le 20/03/2024 en Python 3.7

from tkinter import *
from math import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   Programme principal ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Créer un objet "fenêtre"
fenetre = Tk()

# configuration de la fenetre
fenetre.geometry("500x375+10+10")                     # dimension et position par defaut
fenetre.title("Calculatrice - 1RISC")                 # titre de la fenetre
fenetre.minsize(400, 300)                             # taille minimum de la fenetre
fenetre.maxsize(1024,768)                             # taille maximum de la fenetre

# Fonction d'initialisation de la fenêtre
def clear():
    entreeDec.delete(0, END)
    input_op.set("")
    input_second.set("")
    input_premier.set("")


# Ajouter un texte avec Label() et le positionner avec place(coordonnées x et y)
texteDec = Label(fenetre, text="Entrer votre Calcul" , fg="red")
texteDec.place(x=200, y=50)

# Récupérer une donnée de la fenêtre
input_premier = StringVar()     # 'StringVar()' est utilisé pour obtenir la valeur d'une entrée

entreeDec = Entry(fenetre, width = 50)
entreeDec.place(x=100, y=70)

# Ajouter un texte avec Label() et le positionner avec place(coordonnées x et y)
texteDec = Label(fenetre, text="Entrer votre 2" , fg="red")
texteDec.place(x=200, y=90)

# Récupérer une donnée de la fenêtre
input_second = StringVar()     # 'StringVar()' est utilisé pour obtenir la valeur d'une entrée

entreeDec = Entry(fenetre, width = 50)
entreeDec.place(x=100, y=110)

# Ajouter un texte avec Label() et le positionner avec place(coordonnées x et y)
texteDec = Label(fenetre, text="Entrer votre opération" , fg="red")
texteDec.place(x=180, y=150)

# Récupérer une donnée de la fenêtre
input_op = StringVar()     # 'StringVar()' est utilisé pour obtenir la valeur d'une entrée

entreeDec = Entry(fenetre, width = 40)
entreeDec.place(x=120, y=170)


# Ajouter un texte avec Label() et le positionner avec place(coordonnées x et y)
texteBin = Label(fenetre, text="Votre résultat" , fg="red")
texteBin.place(x=200, y=230)


# Récupérer une donnée de la fenêtre
entreeBin1 = Entry(fenetre, font = ('arial', 12, 'bold'), textvariable = input_premier, width = 50)
entreeBin2 = Entry(fenetre, font = ('arial', 12, 'bold'), textvariable = input_second, width = 50)
entreeBin1.place(x=20, y=250)
entreeBin2.place(x=20, y=250)

# Bouton de remise à zéro
bouton_RAZ = Button(fenetre, text = "Reset", command = clear, bg="cyan")
bouton_RAZ.place(x=200, y=350)

# Bouton de sortie
bouton_Quiter = Button(fenetre, text = "Leave", command = fenetre.destroy, bg="red")
bouton_Quiter.place(x=260, y=350)


# Démarrer la boucle Tkinter (!!! à placer à la fin !!!)
fenetre.mainloop()

if input_op == "+":
    print (int(entreeBin1)+int(entreeBin2))

elif input_op == "-":
    print(int(entreeBin1)-int(entreeBin2))

elif input_op == "/":
    print(int(entreeBin1)/int(entreeBin2))

elif input_op == "*":
    print(int(entreeBin1)*int(entreeBin2))
