"""---------------------------------------------------------------------------------------------
Auteur: Nathan GUYARD
Date: 07/09/2022

Rôle: Permet a un joueur de jouer au démineur en choisissant les coordonée de la case 

Entrée: la case que le joueur veut retourné
Sortie: affiche le résultat de la partie et le jeu en cours dans la console

---------------------------------------------------------------------------------------------"""

# importe les librairy
import random
from Class_TableauJeu import*

class Player:
    
    
    def __init__(self,nomjoueur="Jouer"):
        """ Défini le Joueur """
        
        self.nom = nomjoueur
    
    
    
    def choseCasePlayer (self):
        """ Le joueur choisi la case qu'il veut retourner """
        
        # demande les coordonnée au coordonnée au joueur
        str_x = input("\nEntrer la coordonnée x : ")
        str_y = input("Entrer la coordonnée y : ")
        
        # vérification si le joueur a appuier sur espace
        while str_x == "" or str_y =="":
            print("Aucune coordonnée.\n")
            
            # redemande les coordonnée au coordonnée au joueur
            str_x = input("\nEntrer la coordonnée x : ")
            str_y = input("Entrer la coordonnée y : ")
        
        # diminue de 1 pour que le joueur commence par 1 puis devient 0
        x = int(str_x) -1
        y = int(str_y) -1
        
        # vérifie si la coordonée est bonne
        if x >=0 and x < self.tabJeu.nbCase_x and y >=0 and y < self.tabJeu.nbCase_y:
            
            # vérifie si la case n'est pas retourné
            if self.tabJeu.tab[y][x].retourner == False:
                self.tabJeu.returnCase(x,y)
            
            else:
                print("Case déjà retourner")
                # redemande les coordonnée
                self.choseCasePlayer()
        else:
            print("Mauvaise coordonnée")
            # redemande les coordonnée
            self.choseCasePlayer()
    
    
    
    def playGamePlayer (self):
        """ Fonction principale du jeu """
        
        # demande au joueur les parametre de la partie
        str_x = input("\nTaille x : ")
        str_y = input("Taille y : ")
        str_chance = input("Entrer le pourcentage moyen de bombe entre 10 et 30 : ")
        
        # si rien n'est écrit lance la partie avec les paramètres de bases
        if str_x == "" or str_y == "" or str_chance == "":
            self.tabJeu = TableauJeu()
    
        else:
            # lance la partie avec les paramètres du joueur
            self.tabJeu = TableauJeu(int(str_x),int(str_y),int(str_chance))
        
        # affiche le tableau quand rien n'est retourner
        self.tabJeu.printTableau()
        
        # boucle tant que la partie n'est pas fini
        while self.tabJeu.fin == False:
            self.choseCasePlayer()
            
        
        # retourne toute les cases
        self.tabJeu.returnAll()
        print(self.nom,"a", self.tabJeu.point ,"point.")
        
        # demande au joueur s'il veux rejouer
        rejouer=input("\nVeux tu rejouer : ")
        # boucle jusqu'a qu la réponse n'est pas la bonne
        while rejouer != "y" and rejouer !="yes" and rejouer != "n" and rejouer != "no":
            print("Il faut répondre par yes ou y pour rejouer et par no ou n pour arrêter\n")
            # redemande au joueur s'il veux rejouer
            rejouer=input("Veux tu rejouer : ")
        
        # si il veux rejouer relancer une partie
        if rejouer == "y" or rejouer == "yes":
            self.playGamePlayer()
    
    

# joue 1 Partie
joueur = Player("Philippe")
joueur.playGamePlayer()





