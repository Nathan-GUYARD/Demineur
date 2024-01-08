"""---------------------------------------------------------------------------------------------
Auteur: Nathan GUYARD
Date: 17/09/2022

Rôle: Permet a un joueur de jouer au démineur en choisissant les coordonées de la case 

Entrée: la case que le joueur veut retourné
Sortie: affiche le résultat de la partie et le jeu en cours avec pygame

---------------------------------------------------------------------------------------------"""

#importe les librairies
from Class_TableauJeuGraphic import*

#crée la class joueur
class Player:
    
    
    def __init__(self,param_fenetre):
        """ Défini le Joueur """
        
        self.paramFenetre = param_fenetre
        # crée le tableau du jeu
        self.tabJeu = TableauJeuGraphic(self.paramFenetre,7,7)
        
        # charge les images 
        rejouer = pygame.image.load("image/image_rejouer.png").convert()
        menu = pygame.image.load("image/image_menu.png").convert()
        
        # place les images au coordonnée
        self.tabJeu.fenetre.blit(rejouer,(900,300))
        self.tabJeu.fenetre.blit(menu,(900,600))
        
        # affiche a l'ecran les modifications
        pygame.display.flip()
        
        self.quiteGame = False
        self.exit = False
        
        # crée stock toutes les cases en ligne
        self.tabCase = []
        for i in range (len(self.tabJeu.tab)):
            for n in range (len(self.tabJeu.tab[i])):
                self.tabCase.append(self.tabJeu.tab[i][n])
            
        
        
    def choseCasePlayer (self):
        """ Le joueur choisi la case qu'il veut retourner """
        
        #détecte si la souris est utiliser
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONUP:
            #récupère les coordonnée de la souris
            pos_mouse = pygame.mouse.get_pos()
            
            #crée une boucle en parcourant les case
            remove=-1
            i=0
            while i < len(self.tabCase) and remove == -1:
                #regarde si la souris est sur une case
                if pos_mouse[0] >= self.tabCase[i].pos_x*105+50 and pos_mouse[1] >= self.tabCase[i].pos_y*105+50 and pos_mouse[0] <= self.tabCase[i].pos_x*105 + 150 and pos_mouse[1] <= self.tabCase[i].pos_y*105 + 150:
                    
                    #retourner la case selectionner
                    self.tabJeu.returnCase(self.tabCase[i].pos_x,self.tabCase[i].pos_y)
                    
                    #retire du tableau la case selectionner
                    remove=i
                    self.tabCase.pop(remove)
                            
                i=i+1
            
            # vérifie si un boutton est appuier
            self.quiteGame = self.button (pos_mouse[0],pos_mouse[1])
        
        if self.quiteGame == False:
            # vérifie si la croix est appuier
            self.quiteGame = self.quitGame(event)
        
        
        
    def button (self,x,y):
        """ Vérifie rejoue une partie ou retourn au menu si les boutton sont appuiés """
        
        condition = False
        # regarde si la souris est sur rejouer
        if x >= 900 and x <= 1200 and y >= 300 and y <= 500:
            # met fin a la boucle principale
            condition = True
            
            # affiche un fond noir
            self.tabJeu.fenetre.fill((0, 0, 0))
            
            # relance une partie
            newgame = Player(self.paramFenetre)
            self.exit = newgame.playGamePlayer()
            
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
        
        
        
    def playGamePlayer (self):
        """ Fonction principale du jeu """
        
        # crée une boucle ou ont choisi une case
        while self.tabJeu.fin == False and self.quiteGame==False:
            
            self.choseCasePlayer()
            
        
        # verifi si la fenetre existe
        if self.quiteGame==False:
            
            # retourne toutes les cases
            self.tabJeu.returnAll()
            pygame.time.delay(700)
            
        
            """print(self.nom,"a", self.tabJeu.point ,"point.")"""
            
            # attend une réponse pour continuer
            continuer = False
            while continuer == False:
                
                # détecte si la souris est utiliser
                event = pygame.event.poll()
                if event.type == pygame.MOUSEBUTTONUP:
                    # récupère les coordonnée de la souris
                    pos_mouse = pygame.mouse.get_pos()
                    
                    # détecte si un button est la croix
                    continuer = self.button (pos_mouse[0],pos_mouse[1])
                
                if continuer == False:
                    # vérifie si la croix est appuier
                    continuer = self.quitGame(event)
                
        return self.exit


    











