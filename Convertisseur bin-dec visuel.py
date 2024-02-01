from tkinter import *
from tkinter import messagebox

fen = Tk()
fen.geometry("500x500")
fen.resizable(width=True, height=True)
fen.configure(background="black")
fen.title("Convertisseur")

def bintodec():
    resulat = int(Entry.get(),2)
    Texte.config(text=resulat, fg="white")    


def dectobin():
    valeur = int(Entry.get())
    resulat = bin(valeur)
    Texte.config(text=resulat, fg="white")

def exit():
    quit()

Texte = Label(fen, text="Nombre à convertir", bg="black",fg="white", font=('Futura','25'), width=20, height=20)
Texte.place(x=70, y=0)

Entry = Entry(fen)
Entry.place(x="150", y="100")
Entry.focus()

Bouton = Button(fen, text="DEC -> BIN", command=dectobin)
Bouton.place(x="100", y="180")

Bouton = Button(fen, text="BIN -> DEC", command=bintodec)
Bouton.place(x="300", y="180")

Bouton = Button(fen, text="Exit", command=exit)
Bouton.place(x="220", y="210")

fen.mainloop()