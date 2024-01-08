"""---------------------------------------------------------------------------------------------
Auteur: Nathan GUYARD
Date: 07/09/2022

Rôle: Crée un Tableau du Démineur, on peux choisir une case et l'afficher

Entrée: la taille de la grille
Sortie: affiche la grille dans le terminal

---------------------------------------------------------------------------------------------"""

# importe les librairy
import random
from Class_Case import*


class TableauJeu:
    
    
    def __init__(self,nb_casex=5,nb_casey=5,chance=17):
        """ Crée un Tableu du jeu """
        
        # vérirfie si le nombre de case est suffisant
        if nb_casex <= 1 or nb_casey <= 1:
            nb_casex = 5
            nb_casey = 5
        
        # regarde si la chance est compris en 10 et 30%
        if chance < 10 or chance>30:
            chance = 17
        
        # défini le nombre de case du tableau
        self.nbCase_x = nb_casex
        self.nbCase_y = nb_casey
        self.totalCase = self.nbCase_x * self.nbCase_y
        
        self.fin=False
        # défini le nombre de point
        self.point = 0
        
        # crée le tableau
        self.createTableauCase()
        # défini le nombre de bombe des cases
        self.nbBombeAutourCase()
    
    
    
    def createTableauCase(self,chance=10):
        """ Crée le tableau de toutes les cases du jeu """
        
        self.tab=[]
        self.tabBombe=[]
        
        # boucle sur la taille y du tableau
        for y in range (self.nbCase_y):
            self.tab.append([])
            
            # boucle sur la taille x du tableau
            for x in range (self.nbCase_x):
                isBombe = False
                
                # défini si la case est une bombe
                if random.randint(0,99)<chance:
                    isBombe = True
                    
                    #ajoute la bombe au tableau des bombes
                    self.tabBombe.append([x,y])
                
                # ajoute au tableau une case
                self.tab[y].append(Case(isBombe))
        
        # calcule le nombre de case non retourner qui ne sont pas des bombes
        self.caseReste = self.nbCase_x * self.nbCase_y - len(self.tabBombe)
        
        # vérifie si il y a asser de bombes
        if len(self.tabBombe) < 0.13*self.totalCase or len(self.tabBombe) > 0.26*self.totalCase:
            self.createTableauCase()
            
        
        
    def nbBombeAutourCase(self):
        """ Défini le nombre de bombe autour de chaques cases """
        
        # boucle sur le nombre de bombe
        for i in range (len(self.tabBombe)):
            
            # met dans des tableaux les coordonnées x et y nécessaire
            tab_bombe_xy=[self.tabBombe[i][0],self.tabBombe[i][1]]
            tabmin_xy=[-1,-1]
            tabmax_xy=[1,1]
            tabcase_xy=[self.nbCase_x,self.nbCase_y]
            
            # boucle 1 fois pour les x et une fois pour les y
            for n in range (2):
                # regarde si il n'existe pas de case avant la bombe 
                if tab_bombe_xy[n] <= 0:
                    tabmin_xy[n] = 0
                
                # regarde si il n'existe pas de case après la bombe 
                elif tab_bombe_xy[n] >= tabcase_xy[n] -1:
                    tabmax_xy[n] = 0
                
            x = tabmin_xy[0]
            # boucle tout autour des x valide de la bombe à 1 de distance
            while x <= tabmax_xy[0] :
                y = tabmin_xy[1]
                
                # boucle tout autour des y valide de la bombe à 1 de distance
                while y <= tabmax_xy[1]:
                    
                    #augmente le nombre de bombe a une case autour de la bombe
                    self.tab[tab_bombe_xy[1] + y][tab_bombe_xy[0] + x].nbBombe += 1
                    
                    y=y+1
                    
                x=x+1
        
        print("\nIl y a ", len(self.tabBombe),"bombes.\n")
            
        
        
    def printTableau(self):
        """ Affiche le jeu dans la console """
        
        # boucle sur la coordonnée y
        for y in range (self.nbCase_y):
            
            # boucle sur la coordonnée x
            for x in range (self.nbCase_x):
                
                # affiche la case du tableau
                print(self.tab[y][x].face,end="")
                
                if x < self.nbCase_x - 1:
                    print(" | ",end="")
                    
            print("\n \n",end="")
            
        print("")
    
    
    
    def returnCase(self,x,y):
        """ Retourne une case """
        
        # vérifie si la case est n'est pas une bombe
        if self.tab[y][x].bombe==False:
            # change la valeur de la face de la case
            self.tab[y][x].face = " "+str(self.tab[y][x].nbBombe)+" "
            
            # diminue de 1 le nombre de bombe restant et augmante de 1 le nombre de point
            self.caseReste = self.caseReste - 1
            self.point = self.point + 1
            
            # affiche le nombre de case restant
            print("\nIl reste ", self.caseReste ," case, vous avez ", self.point ," points.\n")
            # affiche le nouveau tableau
            self.printTableau()
            
            # si il n'y a plus de case a retourner
            if self.caseReste == 0:
                # met fin a la partie
                self.fin = True
                self.point += 10
                
                print("Gagné !!!\n")
                        
        else:
            # si c'est une bombe la face deviebt une croix
            self.tab[y][x].face = " X "
            
            # affiche le nouveau tableau
            self.printTableau()
            print("\nPerdu !!!\n")
            
            # met fin a la partie
            self.fin = True
        
        # retourne la carte
        self.tab[y][x].retourner = True           



    def returnAll(self):
        """ Retournes toute les cases du jeu """
        
        # boucle sur la coordonnée y
        for y in range (self.nbCase_y):
            
            # boucle sur la coordonnée x
            for x in range (self.nbCase_x):
                
                # vérifie si la case n'est pas retourné
                if self.tab[y][x].bombe==False:
                    self.tab[y][x].face = " "+str(self.tab[y][x].nbBombe)+" "
                        
                else:
                    self.tab[y][x].face = " X "
            
            # retourne la case
            self.tab[y][x].retourner = True
            
        # affiche le tableau completement retourné
        self.printTableau()
        
