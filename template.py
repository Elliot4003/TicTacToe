import tkinter as tk
from tkinter import messagebox

class Morpion:
    def __init__(self):
        self.joueur_actuel = 'X'  # Set the first player to 'X'
        self.plateau = [[' ']*3 for _ in range(3)]
        
        self.fenetre = tk.Tk()
        self.fenetre.title("Morpion")
        
        self.boutons = [[None]*3 for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                self.boutons[i][j] = tk.Button(self.fenetre, text='', font=('normal', 20), width=5, height=2, command=lambda i=i, j=j: self.clic_bouton(i, j))
                self.boutons[i][j].grid(row=i, column=j)
                
    def clic_bouton(self, i, j):
        if self.plateau[i][j] == ' ':
            self.plateau[i][j] = self.joueur_actuel
            self.boutons[i][j].config(text=self.joueur_actuel)
            
            if self.verifier_victoire():
                messagebox.showinfo("Fin de la partie", f"Le joueur {self.joueur_actuel} a gagné !")
                self.recommencer_partie()
            elif self.verifier_match_nul():
                messagebox.showinfo("Fin de la partie", "Match nul !")
                self.recommencer_partie()
            else:
                self.joueur_actuel = 'O' if self.joueur_actuel == 'X' else 'X'
                
    def verifier_victoire(self):
        # Vérifier les lignes, colonnes et diagonales pour une victoire
        for i in range(3):
            if self.plateau[i][0] == self.plateau[i][1] == self.plateau[i][2] != ' ':
                return True
            if self.plateau[0][i] == self.plateau[1][i] == self.plateau[2][i] != ' ':
                return True
        if self.plateau[0][0] == self.plateau[1][1] == self.plateau[2][2] != ' ':
            return True
        if self.plateau[0][2] == self.plateau[1][1] == self.plateau[2][0] != ' ':
            return True
        return False
    
    def verifier_match_nul(self):
        # Vérifier s'il y a un match nul
        return all(self.plateau[i][j] != ' ' for i in range(3) for j in range(3))
    
    def recommencer_partie(self):
        # Réinitialiser le plateau pour recommencer
        for i in range(3):
            for j in range(3):
                self.plateau[i][j] = ' '
                self.boutons[i][j].config(text='')
        
if __name__ == "__main__":
    jeu = Morpion()
    jeu.fenetre.mainloop()