"""---------------------------------------------------------------------------------------------
Auteur: Nathan GUYARD
Date: 18/09/2022

Rôle: Permet de choisir le mode de jeu

Entrée: la case que le joueur veut retourné
Sortie: affiche le résultat de la partie et le jeu en cours avec pygame

---------------------------------------------------------------------------------------------"""

# importe les librairies
from Programme_demineur_bot_graphique import*
from Programme_Demineur_graphique import*


pygame.init()
pygame.font.init()

pygame.display.set_caption("Démineur")

# crée une fenetre
fenetre = pygame.display.set_mode((1250, 920))
# crée les parametre de font
fontWinLose = pygame.font.Font(pygame.font.get_default_font(), 70)
fontNormal = pygame.font.Font(pygame.font.get_default_font(), 20)

param_fenetre = [fenetre,fontWinLose,fontNormal]

# charge les images
playsolo = pygame.image.load("image/image_PlaySolo.png").convert()
playbot = pygame.image.load("image/image_PlayBot.png").convert()

# crée une boucle
selectGame = False
while selectGame == False :
    
    # affiche un fond noir
    fenetre.fill((0, 0, 0))
    # place les images au coordonnée
    fenetre.blit(playsolo,(400,100))
    fenetre.blit(playbot,(400,500))  
    
    # affiche a l'ecran toute les modifications
    pygame.display.flip()
    
    # détecte si la souris est utiliser
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONUP:
        #récupère les coordonnée de la souris
        pos_mouse = pygame.mouse.get_pos()
        
        # lance le mode Joueur
        if pos_mouse[0] >= 400 and pos_mouse[0] <= 800 and pos_mouse[1] >= 100 and pos_mouse[1] <= 400:
            # affiche un fond noir
            fenetre.fill((0, 0, 0))
            
            joueur = Player(param_fenetre)   
            selectGame = joueur.playGamePlayer()
            
        # lance le mode Bot    
        elif pos_mouse[0] >= 400 and pos_mouse[0] <= 800 and pos_mouse[1] >= 500 and pos_mouse[1] <= 800:
            # affiche un fond noir
            fenetre.fill((0, 0, 0))
            
            bot = Bot(param_fenetre)
            selectGame = bot.playGameBot()
    
    
    if event.type == pygame.QUIT :
        # met fin a la boucle principale
        selectGame = True
        # ferme la fenetre
        pygame.quit()
        
    

    