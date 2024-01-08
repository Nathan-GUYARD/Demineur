"""---------------------------------------------------------------------------------------------
Auteur: Nathan GUYARD
Date: 17/09/2022

Rôle: Crée un Tableau du Démineur, on peux choisir une case et afficher le jeu avec pygame

Entrée: la taille de la grille
Sortie: affiche la jeu avec pygame

---------------------------------------------------------------------------------------------"""

# importe les librairy
import random
from Class_CaseGraphic import*


class TableauJeuGraphic:
    
    
    def __init__(self,param_fenetre,nb_casex=5,nb_casey=5,chance=17):
        """ Crée un Tableu du jeu """
        
        # défini le nombre de case
        self.nbCase_x = nb_casex
        self.nbCase_y = nb_casey
        self.totalCase = self.nbCase_x * self.nbCase_y
        
        self.fin=False
        # défini le nombre de point
        self.point = 0
        
        # stock toutes les images
        self.tab_image=["image/image_0.png","image/image_1.png","image/image_2.png","image/image_3.png","image/image_4.png","image/image_5.png","image/image_6.png","image/image_7.png","image/image_8.png"]
        
        # défini les parametre de la fenetre
        self.fenetre = param_fenetre[0]
        
        # défini les parametre de font
        self.paramFont = [param_fenetre[1],param_fenetre[2]]
        
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
                    
                    #ajoute la bombe au tableau des bombe
                    self.tabBombe.append([x,y])
                
                # ajoute au tableau une case
                self.tab[y].append(CaseGraphic(x,y,self.fenetre,isBombe))
        
        # calcule le nombre de case non retourner qui ne sont pas des bombes
        self.caseReste = self.nbCase_x * self.nbCase_y - len(self.tabBombe)
        
        # vérifie si il y a asser de bombes
        if len(self.tabBombe) < 0.13*self.totalCase or len(self.tabBombe) > 0.26*self.totalCase:
            self.createTableauCase()
        
        # affiche le nombre de bombes de la partie
        surfaceBombe = self.paramFont[1].render("Il y a "+ str(len(self.tabBombe)) +" bombes", True, (255, 255, 255))
        self.fenetre.blit(surfaceBombe, (340, 850))
        
        
        
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
            
        
        
    def returnCase(self,x,y):
        """ Retourne une case """
        
        # vérifie si la case est n'est pas une bombe
        if self.tab[y][x].bombe==False:
            
            # change la valeur de la face de la case
            self.tab[y][x].updateImage(self.tab_image[self.tab[y][x].nbBombe],self.fenetre)
            
            # diminue de 1 le nombre de bombe restant et augmante de 1 le nombre de point
            self.caseReste = self.caseReste - 1
            self.point = self.point + 1
            
            # si il n'y a plus de case a retourner
            if self.caseReste == 0:
                # met fin a la partie
                self.fin = True
                self.point += 10
                
                # affiche que le joueur a gagner
                surfaceWin = self.paramFont[0].render("Gagné !!!", True, (0, 255, 0))
                self.fenetre.blit(surfaceWin, (900, 100))
                
                pygame.display.flip()
        
        else:
            # change la valeur de la face de la case
            self.tab[y][x].updateImage("image/image_bombe.png",self.fenetre)
            
            # affiche que le joueur a perdu
            surfaceLose = self.paramFont[0].render("Perdu !!!", True, (255, 0, 0))
            self.fenetre.blit(surfaceLose, (900, 100))
            
            pygame.display.flip()    
            
            # met fin a la partie
            self.fin = True
        
        # affiche le nombre de point le nombre de case restant
        self.surfacePoint = self.paramFont[1].render("Il reste "+ str(self.caseReste) +" cases, vous avez " + str(self.point) +" points.", True, (255, 255, 255))
        
        # affiche une surface noire au coordonnée du texte
        surfaceNoir = pygame.Surface((self.surfacePoint.get_width(), self.surfacePoint.get_height()))
        surfaceNoir.fill((0, 0, 0))
        
        # affiche sur la surface noire le texte
        surfaceNoir.blit(self.surfacePoint, (0, 0))
        # affiche la surface noire et le texte
        self.fenetre.blit(surfaceNoir, (850, 200))
        
        pygame.display.flip()
        
        # retourne la case
        self.tab[y][x].retourner = True           



    def returnAll(self):
        """ Retourne toutes les cases du jeu """
        
        # boucle sur la coordonnée y
        for y in range (self.nbCase_y):
            
            # boucle sur la coordonnée x
            for x in range (self.nbCase_x):
                
                # vérifie si la case n'est pas retourné
                if self.tab[y][x].bombe==False:
                    # change la face de la case
                    self.tab[y][x].updateImage(self.tab_image[self.tab[y][x].nbBombe],self.fenetre)
                    
                else:
                    # change la face de la case
                    self.tab[y][x].updateImage("image/image_bombe.png",self.fenetre)
            
            # retourne la case
            self.tab[y][x].retourner = True
            



