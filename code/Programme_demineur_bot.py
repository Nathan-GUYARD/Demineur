"""---------------------------------------------------------------------------------------------
Auteur: Nathan GUYARD
Date: 15/09/2022

Rôle: Permet à un Bot de jouer au démineur en choisissant les coordonée de la case 

Entrée: la case que le bot veut retourné
Sortie: affiche le résultat de la partie et le jeu en cours dans la console

---------------------------------------------------------------------------------------------"""

# importe les librairy
import time
from Class_TableauJeu import*


class Bot:
    
    
    def __init__(self,nomBot = "Bot"):
        """ Crée un bot """
        
        self.nom = nomBot
        
        # crée le tableau de la partie
        self.tabPartie = TableauJeu()
    
    
    
    def playGameBot (self):
        """ Fonction principale du jeu """
        
        # boucle tant que la partie n'est pas fini
        while self.tabPartie.fin == False:
            self.choseCaseBot()
        
        # affiche tout le tableau
        self.tabPartie.returnAll()
        print(self.nom, "a", self.tabPartie.point ,"point.")
    
    
    
    def choseCaseBot(self):
        """ Le bot choisi une coordonnée aléatoire """
        
        # choisi des coordonnées au hazard
        x = random.randint(0,self.tabPartie.nbCase_x-1)
        y = random.randint(0,self.tabPartie.nbCase_y-1)
        
        # vérifie si la case n'est pas retourner
        if self.tabPartie.tab[y][x].retourner == False:
            # retourne la case
            self.tabPartie.returnCase(x,y)
            time.sleep(0.5)
            
            # regarde si la case est un 0 et retourne toutes les cases autour
            self.smartChose0(x,y)
            
        else:
            # reselectionne une case si elle n'est pas bonne
            self.choseCaseBot()
    
    
    
    def smartChose0(self,x,y):
        """ Le bot retourne les cases autour des cases qui ont 0 bombe autour d'eux """
        
        # vérifie si la case est pas un 0
        if self.tabPartie.tab[y][x].nbBombe == 0:
            
            # met dans des tableaus les coordonnées x et y nécessaire
            tabmin_xy=[-1,-1]
            tabmax_xy=[1,1] 
            tabcase_xy=[self.tabPartie.nbCase_x,self.tabPartie.nbCase_y]
            tab_xy=[x,y]
            
            # boucle 1 fois pour les x et une fois pour les y
            for n in range (2):
                # regarde si il n'existe pas de case avant la case sélectionner
                if tab_xy[n] <= 0:
                    # la case qui vas regarder est au minimum en 0 par raport la case sélectionner
                    tabmin_xy[n] = 0
                
                # regarde si il n'existe pas de case après la case sélectionner
                elif tab_xy[n] >= tabcase_xy[n] -1:
                    # la case qui vas regarder est au maximum en 0 par raport la case sélectionner
                    tabmax_xy[n] = 0
                
            x2 = tabmin_xy[0]
            # boucle tout autour des x valide de la case à 1 de distance
            while x2 <= tabmax_xy[0] :
                y2 = tabmin_xy[1]
                
                # boucle tout autour des y valide de la case à 1 de distance
                while y2 <= tabmax_xy[1]:
                    
                    # vérifie si la case n'est pas retourner
                    if self.tabPartie.tab[tab_xy[1] + y2][tab_xy[0] + x2].retourner == False:
                        # retourne la case
                        self.tabPartie.returnCase(x + x2, y + y2)
                        
                        time.sleep(0.5)
                        # regarde si la case est un 0 et retourne toutes les cases autour
                        self.smartChose0(x + x2, y + y2)
                                
                    y2 = y2 + 1
                x2 = x2 + 1
                
                


# joue 1 Partie
bot = Bot("Gérard")
bot.playGameBot()

    
    
    