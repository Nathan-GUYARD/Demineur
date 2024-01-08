"""---------------------------------------------------------------------------------------------
Auteur: Nathan GUYARD
Date: 17/09/2022

Rôle: Crée une case qui contient ses informations

Entrée: les position x,y et si c'est une bombe
Sortie: affiche la case (le nombre de bombe autour d'elle si ce n'est pas une bombe)

---------------------------------------------------------------------------------------------"""

# importe les librairy
import pygame
from pygame.locals import *

class CaseGraphic:
    
    
    def __init__(self,x,y,fenetre,isBombe=False):
        """ Crée une Case """
        
        # défini les coordonnée x et y
        self.pos_x = x
        self.pos_y = y
        
        # initialise si la case est une bombe et qu la bombe n'est pas retourné
        self.bombe = isBombe
        self.retourner = False
        
        # initailise le nombre de bombes et affiche la face
        self.nbBombe = 0
        self.updateImage("image/image_dontreturn.png",fenetre)
    
    
    
    def updateImage (self,image,fenetre):
        """ Affiche la case """
        
        # charge l'image
        self.face_graphic = image
        self.load_face = pygame.image.load(self.face_graphic).convert()
        
        # défini les coordonnée de l'image
        fenetre.blit(self.load_face,(self.pos_x*105+50,self.pos_y*105+50))
        
        # affiche les modifications
        pygame.display.flip()
        
    