from tkinter import *

        # Ajoutez ici l'action que vous souhaitez effectuer
# Initilisation de l'interface graphique
window = Tk()
window.geometry('1280x700')
window.title('Tic Tac Toe')
window['bg'] = '#D2DBFF'
window.attributes("-fullscreen", False)  # en fullscreen

# Créer un canva pour y placer la grilles, les croix et les cercles
can = Canvas(window, width=1280, height=700, bg="#D2DBFF", highlightthickness=0, relief='ridge')
grid = PhotoImage(file='img/grid.png')
can.create_image(640, 350, image=grid, state='normal')
can.place(x='0', y='0')

# Créer et placer les images des croix et ronds
cross = PhotoImage(file='img/cross.png')
circle = PhotoImage(file='img/circle.png')

#--------------------haut ------------------------------------------------------

x_haut_gauche = 480
x_haut = 640
x_haut_droit = 800
y_haut = 185
#--------------------milieu ------------------------------------------------------
x_mileu_gauche = 480
x_milieu = 640
x_milieu_droit = 800

y_milieu = 350
#--------------------bas------------------------------------------------------
x_bas_gauche = 480
x_bas = 640
x_bas_droit = 800

y_bas = 510


class joueur:
    def __init__(self) -> None:
        self.create()

    def create(self):
        self.pseudo = input("Veuillez entrer votre nom")

class jeu :
    def __init__(self) -> None:
        self.create()
       
    
    def create(self):
        print("Le jeu commence")
        


class croix:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = cross
        self.object_id = None
        self.create()

    def create(self):
        self.object_id = can.create_image(self.x, self.y, image=self.image, state='normal')
        print("une croix a été créer")

les_croix_existantes =[]

class cercles:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = circle
        self.object_id = None
        self.create()

    def create(self):
        self.object_id = can.create_image(self.x, self.y, image=self.image, state='normal')
        print("un cercle a été créer")

les_cercles_existants =[]

def verifie_existance_croix(x,y):
    for croix in les_croix_existantes:
        if croix.x == x and croix.y == y:
            return True
    return False

def verifie_existance_cercle(x,y):
    for cercle in les_cercles_existants:
        if cercle.x == x and cercle.y == y:
            return True
    return False



def ajouter_croix(x):
    les_croix_existantes.append(x)
    global etat
    etat = True
    print(etat)

def ajouter_cercle(x):
    les_cercles_existants.append(x)
    global etat
    etat = False
    print(etat)

etat = False

def on_canvas_click(event):

    global etat
    # Obtenir les coordonnées du clic
    x, y = event.x, event.y

    # Définir une plage autour de la croix où un clic est considéré comme proche
    distance_proximite = 50

    # Vérifier si le clic est à proximité de la croix
    print(f"Clic à proximité de + {x} + {y}")
    
    if not verifie_existance_croix(x_haut_gauche,y_haut):
        if abs(x - x_haut_gauche) <= distance_proximite and abs(y - y_haut) <= distance_proximite :
            if etat == False:
                nouvelle_croix = croix(x_haut_gauche,y_haut)
                ajouter_croix(nouvelle_croix)
        
            elif etat == True:
                nouveau_cercle = cercles(x_haut_gauche,y_haut)
                ajouter_cercle(nouveau_cercle)        
    if not verifie_existance_croix(x_haut,y_haut):
        if abs(x - x_haut) <= distance_proximite and abs(y - y_haut) <= distance_proximite:
            if etat == False:
                nouvelle_croix = croix(x_haut,y_haut)
                ajouter_croix(nouvelle_croix)
            elif etat == True:
                nouveau_cercle = cercles(x_haut,y_haut)
                ajouter_cercle(nouveau_cercle)        
    if not verifie_existance_croix(x_haut_droit,y_haut):  
        if abs(x - x_haut_droit) <= distance_proximite and abs(y - y_haut) <= distance_proximite:
            if etat == False:
                nouvelle_croix = croix(x_haut_droit,y_haut)    
                ajouter_croix(nouvelle_croix)
            elif etat == True:
                nouveau_cercle = cercles(x_haut_droit,y_haut)
                ajouter_cercle(nouveau_cercle)        
#------------------------------------------------------------------------------------------------------------
    if not verifie_existance_croix(x_mileu_gauche,y_milieu):
        if abs(x - x_mileu_gauche) <= distance_proximite and abs(y - y_milieu) <= distance_proximite:
            if etat == False:
                nouvelle_croix = croix(x_mileu_gauche,y_milieu)
                ajouter_croix(nouvelle_croix)
            elif etat == True:
                nouveau_cercle = cercles(x_mileu_gauche,y_milieu)
                ajouter_cercle(nouveau_cercle)      

    if not verifie_existance_croix(x_milieu,y_milieu):  
        if abs(x - x_milieu) <= distance_proximite and abs(y - y_milieu) <= distance_proximite:
            if etat == False:
                nouvelle_croix = croix(x_milieu,y_milieu)
                ajouter_croix(nouvelle_croix)
            elif etat == True:
                nouveau_cercle = cercles(x_milieu,y_milieu)
                ajouter_cercle(nouveau_cercle)
    if not verifie_existance_croix(x_milieu_droit,y_milieu): 
        if abs(x - x_milieu_droit) <= distance_proximite and abs(y - y_milieu) <= distance_proximite:
            if etat == False:
                nouvelle_croix = croix(x_milieu_droit,y_milieu)
                ajouter_croix(nouvelle_croix)
            elif etat == True:
                nouveau_cercle = cercles(x_milieu_droit,y_milieu)
                ajouter_cercle(nouveau_cercle)


#------------------------------------------------------------------------------------------------------------
    if not verifie_existance_croix(x_bas_gauche,y_bas): 
        if abs(x - x_bas_gauche) <= distance_proximite and abs(y - y_bas) <= distance_proximite:
            if etat == False:
                nouvelle_croix = croix(x_bas_gauche,y_bas)
                ajouter_croix(nouvelle_croix)
            elif etat == True:
                nouveau_cercle = cercles(x_bas_gauche,y_bas)
                ajouter_cercle(nouveau_cercle)

    if not verifie_existance_croix(x_bas,y_bas): 
        if abs(x - x_bas) <= distance_proximite and abs(y - y_bas) <= distance_proximite:
            if etat == False:
                nouvelle_croix = croix(x_bas,y_bas)
                ajouter_croix(nouvelle_croix)
            elif etat == True:
                nouveau_cercle = cercles(x_bas,y_bas)
                ajouter_cercle(nouveau_cercle)

    if not verifie_existance_croix(x_bas_droit,y_bas):   
        if abs(x - x_bas_droit) <= distance_proximite and abs(y - y_bas) <= distance_proximite:
            if etat == False:
                nouvelle_croix = croix(x_bas_droit,y_bas)
                les_croix_existantes.append(nouvelle_croix)
            elif etat == True:
                nouveau_cercle = cercles(x_bas_droit,y_bas)
                ajouter_cercle(nouveau_cercle)
    
    if verifie_existance_croix(x_bas,y_bas) and verifie_existance_croix(x_bas_gauche,y_bas) and verifie_existance_croix(x_bas_droit,y_bas) or\
          verifie_existance_croix(x_haut_gauche,y_milieu) and verifie_existance_croix(x_milieu,y_milieu) and verifie_existance_croix(x_milieu_droit,y_milieu) or\
          verifie_existance_croix(x_haut_gauche,y_haut) and  verifie_existance_croix(x_haut,y_haut) and  verifie_existance_croix(x_haut_droit,y_haut)or\
          verifie_existance_croix(x_haut_gauche,y_haut) and verifie_existance_croix(x_mileu_gauche,y_milieu) and verifie_existance_croix(x_bas_gauche,y_bas)or\
          verifie_existance_croix(x_milieu,y_haut) and verifie_existance_croix(x_milieu,y_milieu) and verifie_existance_croix(x_bas,y_bas) or\
          verifie_existance_croix(x_haut_droit,y_haut) and verifie_existance_croix(x_milieu_droit,y_milieu) and verifie_existance_croix(x_bas_droit,y_bas)or\
          verifie_existance_croix(x_bas_gauche,y_bas) and verifie_existance_croix(x_milieu,y_milieu) and verifie_existance_croix(x_haut_droit,y_haut)or\
         verifie_existance_croix(x_haut_gauche,y_haut) and verifie_existance_croix(x_milieu,y_milieu) and verifie_existance_croix(x_bas_droit,y_bas):
        print("fin de jeu")
        

    if verifie_existance_cercle(x_bas,y_bas) and verifie_existance_cercle(x_bas_gauche,y_bas) and verifie_existance_cercle(x_bas_droit,y_bas) or\
          verifie_existance_cercle(x_haut_gauche,y_milieu) and verifie_existance_cercle(x_milieu,y_milieu) and verifie_existance_cercle(x_milieu_droit,y_milieu) or\
          verifie_existance_cercle(x_haut_gauche,y_haut) and  verifie_existance_cercle(x_haut,y_haut) and  verifie_existance_cercle(x_haut_droit,y_haut)or\
          verifie_existance_cercle(x_haut_gauche,y_haut) and verifie_existance_cercle(x_mileu_gauche,y_milieu) and verifie_existance_cercle(x_bas_gauche,y_bas)or\
          verifie_existance_cercle(x_milieu,y_haut) and verifie_existance_cercle(x_milieu,y_milieu) and verifie_existance_cercle(x_bas,y_bas) or\
          verifie_existance_cercle(x_haut_droit,y_haut) and verifie_existance_cercle(x_milieu_droit,y_milieu) and verifie_existance_cercle(x_bas_droit,y_bas)or\
          verifie_existance_cercle(x_bas_gauche,y_bas) and verifie_existance_cercle(x_milieu,y_milieu) and verifie_existance_cercle(x_haut_droit,y_haut)or\
         verifie_existance_cercle(x_haut_gauche,y_haut) and verifie_existance_cercle(x_milieu,y_milieu) and verifie_existance_cercle(x_bas_droit,y_bas):
        print("fin de jeu")
       
can.bind("<Button-1>", on_canvas_click)

# Faire tourner l'interface en boucle
window.mainloop()
