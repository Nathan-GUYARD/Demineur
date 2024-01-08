"""---------------------------------------------------------------------------------------------
Auteur: Nathan GUYARD
Date: 07/09/2022

Rôle: Crée une case qui contient ses informations

Entrée: les position x,y et si c'est une bombe
Sortie: la face de la case (le nombre de bombe autour d'elle si ce n'est pas une bombe)

---------------------------------------------------------------------------------------------"""

class Case:
    
    
    def __init__(self,isBombe=False):
        """ Crée une Case """
        
        # initialise si la case est une bombe et qu la bombe n'est pas retourné
        self.bombe = isBombe
        self.retourner = False
        
        # initailise le nombre de bombes et la face
        self.nbBombe = 0
        self.face = "[ ]"
        
        
        
    