from tkinter import *

# Initilisation de l'interface graphique
from tkinter import Canvas

window = Tk()
window.geometry('1280x700')
window.title('Tic Tac Toe')
window['bg'] = '#D2DBFF'
window.attributes("-fullscreen", True)  # en fullscreen

# Créer un canvas pour y placer la grille, les croix et les cercles
can = Canvas(window, width=1280, height=700, bg="#D2DBFF", highlightthickness=0, relief='ridge')
grid = PhotoImage(file='img/grid.png')
can.create_image(640, 350, image=grid, state='normal')
can.place(x='0', y='0')

# Label pour message de victoire croix
txtWinCroix = Label(window, text="Les croix gagnent !", fg="red", bg="#D2DBFF",
                    font=("Rockwell", 25), width=16)

# Label pour message de victoire cercles
txtWinCercles = Label(window, text=f"Les cercles gagnent !", fg="red", bg="#D2DBFF",
                      font=("Rockwell", 25), width=18)

# Label pour message match nul
txtNul = Label(window, text="Match nul !", fg="red", bg="#D2DBFF",
               font=("Rockwell", 25), width=16)

# Créer les images des croix et ronds
cross = PhotoImage(file='img/cross.png')
circle = PhotoImage(file='img/circle.png')

# Haut
x_haut_gauche = 480
x_haut = 640
x_haut_droit = 800
y_haut = 185

# Milieu
x_mileu_gauche = 480
x_milieu = 640
x_milieu_droit = 800
y_milieu = 350

# Bas
x_bas_gauche = 480
x_bas = 640
x_bas_droit = 800
y_bas = 510


class Croix:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = cross
        self.object_id = None
        self.create()

    def create(self):
        self.object_id = can.create_image(self.x, self.y, image=self.image, state='normal')


les_croix_existantes = []


class Cercles:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = circle
        self.object_id = None
        self.create()

    def create(self):
        self.object_id = can.create_image(self.x, self.y, image=self.image, state='normal')


les_cercles_existants = []


def replay():
    can.delete("all")
    can.create_image(640, 350, image=grid, state='normal')
    can.place(x='0', y='0')

    global count
    count = 0
    les_cercles_existants.clear()
    les_croix_existantes.clear()

    txtWinCroix.place_forget()
    txtWinCercles.place_forget()
    txtNul.place_forget()
    replayB.place_forget()


replayB = Button(text="Rejouer", command=replay, height=2, width=10)


def verifie_existance_croix(x, y):
    for croix in les_croix_existantes:
        if croix.x == x and croix.y == y:
            return True
    return False


def verifie_existance_cercle(x, y):
    for cercle in les_cercles_existants:
        if cercle.x == x and cercle.y == y:
            return True
    return False


def ajouter_croix(x):
    les_croix_existantes.append(x)
    global etat
    etat = True

    global count
    count += 1


def ajouter_cercle(x):
    les_cercles_existants.append(x)
    global etat
    etat = False

    global count
    count += 1


etat = False
count = 0


def on_canvas_click(event):
    global etat
    # Obtenir les coordonnées du clic
    x, y = event.x, event.y

    # Définir une plage autour de la croix où un clic est considéré comme proche
    distance_proximite = 50

    if not verifie_existance_croix(x_haut_gauche, y_haut):
        if abs(x - x_haut_gauche) <= distance_proximite and abs(y - y_haut) <= distance_proximite:
            if not etat:
                nouvelle_croix = Croix(x_haut_gauche, y_haut)
                ajouter_croix(nouvelle_croix)

            elif etat:
                nouveau_cercle = Cercles(x_haut_gauche, y_haut)
                ajouter_cercle(nouveau_cercle)

    if not verifie_existance_croix(x_haut, y_haut):
        if abs(x - x_haut) <= distance_proximite and abs(y - y_haut) <= distance_proximite:
            if not etat:
                nouvelle_croix = Croix(x_haut, y_haut)
                ajouter_croix(nouvelle_croix)
            elif etat:
                nouveau_cercle = Cercles(x_haut, y_haut)
                ajouter_cercle(nouveau_cercle)

    if not verifie_existance_croix(x_haut_droit, y_haut):
        if abs(x - x_haut_droit) <= distance_proximite and abs(y - y_haut) <= distance_proximite:
            if not etat:
                nouvelle_croix = Croix(x_haut_droit, y_haut)
                ajouter_croix(nouvelle_croix)
            elif etat:
                nouveau_cercle = Cercles(x_haut_droit, y_haut)
                ajouter_cercle(nouveau_cercle)

    if not verifie_existance_croix(x_mileu_gauche, y_milieu):
        if abs(x - x_mileu_gauche) <= distance_proximite and abs(y - y_milieu) <= distance_proximite:
            if not etat:
                nouvelle_croix = Croix(x_mileu_gauche, y_milieu)
                ajouter_croix(nouvelle_croix)
            elif etat:
                nouveau_cercle = Cercles(x_mileu_gauche, y_milieu)
                ajouter_cercle(nouveau_cercle)

    if not verifie_existance_croix(x_milieu, y_milieu):
        if abs(x - x_milieu) <= distance_proximite and abs(y - y_milieu) <= distance_proximite:
            if not etat:
                nouvelle_croix = Croix(x_milieu, y_milieu)
                ajouter_croix(nouvelle_croix)
            elif etat:
                nouveau_cercle = Cercles(x_milieu, y_milieu)
                ajouter_cercle(nouveau_cercle)

    if not verifie_existance_croix(x_milieu_droit, y_milieu):
        if abs(x - x_milieu_droit) <= distance_proximite and abs(y - y_milieu) <= distance_proximite:
            if not etat:
                nouvelle_croix = Croix(x_milieu_droit, y_milieu)
                ajouter_croix(nouvelle_croix)
            elif etat:
                nouveau_cercle = Cercles(x_milieu_droit, y_milieu)
                ajouter_cercle(nouveau_cercle)

    if not verifie_existance_croix(x_bas_gauche, y_bas):
        if abs(x - x_bas_gauche) <= distance_proximite and abs(y - y_bas) <= distance_proximite:
            if not etat:
                nouvelle_croix = Croix(x_bas_gauche, y_bas)
                ajouter_croix(nouvelle_croix)
            elif etat:
                nouveau_cercle = Cercles(x_bas_gauche, y_bas)
                ajouter_cercle(nouveau_cercle)

    if not verifie_existance_croix(x_bas, y_bas):
        if abs(x - x_bas) <= distance_proximite and abs(y - y_bas) <= distance_proximite:
            if not etat:
                nouvelle_croix = Croix(x_bas, y_bas)
                ajouter_croix(nouvelle_croix)
            elif etat:
                nouveau_cercle = Cercles(x_bas, y_bas)
                ajouter_cercle(nouveau_cercle)

    if not verifie_existance_croix(x_bas_droit, y_bas):
        if abs(x - x_bas_droit) <= distance_proximite and abs(y - y_bas) <= distance_proximite:
            if not etat:
                nouvelle_croix = Croix(x_bas_droit, y_bas)
                les_croix_existantes.append(nouvelle_croix)
            elif etat:
                nouveau_cercle = Cercles(x_bas_droit, y_bas)
                ajouter_cercle(nouveau_cercle)

    if verifie_existance_croix(x_bas, y_bas) and verifie_existance_croix(x_bas_gauche,
                                                                         y_bas) and verifie_existance_croix(x_bas_droit,
                                                                                                            y_bas) or \
            verifie_existance_croix(x_haut_gauche, y_milieu) and verifie_existance_croix(x_milieu,
                                                                                         y_milieu) and verifie_existance_croix(
        x_milieu_droit, y_milieu) or \
            verifie_existance_croix(x_haut_gauche, y_haut) and verifie_existance_croix(x_haut,
                                                                                       y_haut) and verifie_existance_croix(
        x_haut_droit, y_haut) or \
            verifie_existance_croix(x_haut_gauche, y_haut) and verifie_existance_croix(x_mileu_gauche,
                                                                                       y_milieu) and verifie_existance_croix(
        x_bas_gauche, y_bas) or \
            verifie_existance_croix(x_milieu, y_haut) and verifie_existance_croix(x_milieu,
                                                                                  y_milieu) and verifie_existance_croix(
        x_bas, y_bas) or \
            verifie_existance_croix(x_haut_droit, y_haut) and verifie_existance_croix(x_milieu_droit,
                                                                                      y_milieu) and verifie_existance_croix(
        x_bas_droit, y_bas) or \
            verifie_existance_croix(x_bas_gauche, y_bas) and verifie_existance_croix(x_milieu,
                                                                                     y_milieu) and verifie_existance_croix(
        x_haut_droit, y_haut) or \
            verifie_existance_croix(x_haut_gauche, y_haut) and verifie_existance_croix(x_milieu,
                                                                                       y_milieu) and verifie_existance_croix(
        x_bas_droit, y_bas):
        txtWinCroix.place(x="490", y="640")
        replayB.place(x="820", y="640")

    elif count == 9:
        txtNul.place(x="490", y="640")
        replayB.place(x="820", y="640")

    if verifie_existance_cercle(x_bas, y_bas) and verifie_existance_cercle(x_bas_gauche,
                                                                           y_bas) and verifie_existance_cercle(
        x_bas_droit, y_bas) or \
            verifie_existance_cercle(x_haut_gauche, y_milieu) and verifie_existance_cercle(x_milieu,
                                                                                           y_milieu) and verifie_existance_cercle(
        x_milieu_droit, y_milieu) or \
            verifie_existance_cercle(x_haut_gauche, y_haut) and verifie_existance_cercle(x_haut,
                                                                                         y_haut) and verifie_existance_cercle(
        x_haut_droit, y_haut) or \
            verifie_existance_cercle(x_haut_gauche, y_haut) and verifie_existance_cercle(x_mileu_gauche,
                                                                                         y_milieu) and verifie_existance_cercle(
        x_bas_gauche, y_bas) or \
            verifie_existance_cercle(x_milieu, y_haut) and verifie_existance_cercle(x_milieu,
                                                                                    y_milieu) and verifie_existance_cercle(
        x_bas, y_bas) or \
            verifie_existance_cercle(x_haut_droit, y_haut) and verifie_existance_cercle(x_milieu_droit,
                                                                                        y_milieu) and verifie_existance_cercle(
        x_bas_droit, y_bas) or \
            verifie_existance_cercle(x_bas_gauche, y_bas) and verifie_existance_cercle(x_milieu,
                                                                                       y_milieu) and verifie_existance_cercle(
        x_haut_droit, y_haut) or \
            verifie_existance_cercle(x_haut_gauche, y_haut) and verifie_existance_cercle(x_milieu,
                                                                                         y_milieu) and verifie_existance_cercle(
        x_bas_droit, y_bas):
        txtWinCercles.place(x="470", y="640")
        replayB.place(x="820", y="640")

    elif count == 9:
        txtNul.place(x="490", y="640")
        replayB.place(x="820", y="640")


if count < 9:
    can.bind("<Button-1>", on_canvas_click)

# Faire tourner l'interface en boucle
window.mainloop()
