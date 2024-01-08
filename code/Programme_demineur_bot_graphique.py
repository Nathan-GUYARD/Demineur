"""---------------------------------------------------------------------------------------------
Auteur: Nathan GUYARD
Date: 17/09/2022

Rôle: Permet à un Bot de jouer au démineur en choisissant les coordonée de la case 

Entrée: la case que le bot veut retourné
Sortie: affiche le résultat de la partie et le jeu en cours avec pygame

---------------------------------------------------------------------------------------------"""

# importe les librairy
from Class_TableauJeuGraphic import*


class Bot:
    
    
    def __init__(self,param_fenetre):
        """ Crée un bot """
        
        self.paramFenetre = param_fenetre
        # crée le tableau de la partie
        self.tabPartie = TableauJeuGraphic(self.paramFenetre,7,7)
        
        # charge les images
        rejouer = pygame.image.load("image/image_rejouer.png").convert()
        menu = pygame.image.load("image/image_menu.png").convert()
        
        
        
        # défini les coordonnée des images
        self.tabPartie.fenetre.blit(rejouer,(900,300))
        self.tabPartie.fenetre.blit(menu,(900,600))
        
        #affiche les modification
        pygame.display.flip()
        pygame.time.delay(1000)
        
        self.exit = False
        
        
        
    def playGameBot (self):
        """ Fonction principale du jeu """
        
        # boucle tant que la partie n'est pas fini
        while self.tabPartie.fin == False:
            # le bot choisi une case
            self.choseCaseBot()                     
                            
        pygame.time.delay(500)
        #retourn toute les cases
        self.tabPartie.returnAll()        
        
        continuer = False
        #boucle jusqu'à qu'un boutton est appuier 
        while continuer == False:
            
            # détecte si la souris est utiliser
            event = pygame.event.poll()
            if  event.type == pygame.MOUSEBUTTONUP :
                # récupère les coordonnée de la souris
                pos_mouse = pygame.mouse.get_pos()
                
                # détecte si un button est appuié
                continuer = self.button (pos_mouse[0],pos_mouse[1])
            
            if continuer == False:
                # vérifie si la croix est appuier
                continuer = self.quitGame(event)
               
        return self.exit
        
        
        
    def choseCaseBot(self):
        """ Le bot choisi une coordonnée aléatoire """
        
        # choisi des coordonnées au hazard
        x = random.randint(0,self.tabPartie.nbCase_x-1)
        y = random.randint(0,self.tabPartie.nbCase_y-1)
        
        # vérifie si la case n'est pas retourner
        if self.tabPartie.tab[y][x].retourner == False:
            # retourne la case
            self.tabPartie.returnCase(x,y)
            pygame.time.delay(100)
            
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
                        pygame.time.delay(100)
                        
                        # regarde si la case est un 0 et retourne toutes les cases autour
                        self.smartChose0(x + x2, y + y2)
                                
                    y2 = y2 + 1    
                x2 = x2 + 1



    def button (self,x,y):
        """ Vérifie rejoue une partie ou retourn au menu si les boutton sont appuiés """
        
        condition = False
        # regarde si la souris est sur rejouer
        if x >= 900 and x <= 1200 and y >= 300 and y <= 500:
            # met fin a la boucle principale
            condition = True
            
            # affiche un fond noir
            self.tabPartie.fenetre.fill((0, 0, 0))
            
            # relance une partie
            newgame = Bot(self.paramFenetre)
            self.exit = newgame.playGameBot()
            
        # regarde si la souris est sur le boutton menu
        elif x >= 900 and x <= 1200 and y >= 600 and y <= 800:
            # met fin a la boucle principale
            condition = True 
        
        return condition
            
        
        
    def quitGame(self,event):
        """ Vérifie si la crois est appuier et ferme la fenetre """
        
        condition = False
        # détecte si la croix est appuier
        if event.type == pygame.QUIT :
            # met fin a la boucle principale
            condition = True
            # ferme la fenetre
            pygame.quit()
            self.exit = True
            
        return condition 
                
            
    
    
    
    
    
