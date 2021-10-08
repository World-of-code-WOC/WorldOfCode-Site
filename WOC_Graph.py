import os
import sys
import time
import numpy as np

import pygame
from pygame.locals import *

v = locals()

def Convertisseur_valeur_px(min_x, max_x, min_y, max_y, Valeur):
    
    (X, Y) = Valeur

    return round(20 + ((X - min_x)*(SIZE[0]-40))/(max_x - min_x)), round(20 + ((max_y - Y)*(SIZE[1]-40))/(max_y - min_y))

def Convertisseur_px_valeur(min_x, max_x, min_y, max_y, P):
    """
    P : Position en px
    """
    
    (px, py) = P
    
    return round((min_x + ((px - 20)*(max_x - min_x))/(SIZE[0] - 40)), 4), round((min_y + ((SIZE[1] - 20 - py)*(max_y - min_y))/(SIZE[1] - 40)), 4)

def Analyse_Data(x, y):
    
    min_max_x = (min(x), max(x))
    min_max_y = (min(y), max(y))
    
    return min_max_x, min_max_y

def Calcul_Axes(min_max_x, min_max_y):
    
    v["min_x"] = min_max_x[0] - (min_max_x[1] - min_max_x[0])*0.1
    v["max_x"] = min_max_x[1] + (min_max_x[1] - min_max_x[0])*0.1
    v["min_y"] = min_max_y[0] - (min_max_y[1] - min_max_y[0])*0.1
    v["max_y"] = min_max_y[1] + (min_max_y[1] - min_max_y[0])*0.1

    return min_x, max_x, min_y, max_y
    
def Tracer_Axes(min_x, max_x, min_y, max_y):
    
    pos_O = Convertisseur_valeur_px(min_x, max_x, min_y, max_y, (0, 0))

    if min_x < 0 < max_x:
        
        pygame.draw.line(fenetre, Color(255, 255, 255), (pos_O[0], 20), (pos_O[0], SIZE[1]-20))
        
    if min_y < 0 < max_y:
        
        pygame.draw.line(fenetre, Color(255, 255, 255), (20, pos_O[1]), (SIZE[0]-20, pos_O[1]))
        
    pygame.display.flip()
    
def Plot(X, Y, Couleur = Color(0, 0, 255)):
    
    min_max_x, min_max_y = Analyse_Data(X, Y)
    min_x, max_x, min_y, max_y = Calcul_Axes(min_max_x, min_max_y)
    Tracer_Axes(min_x, max_x, min_y, max_y)
    
    for i in range(len(X)):
        
        pygame.draw.circle(fenetre, Couleur, Convertisseur_valeur_px(min_x, max_x, min_y, max_y, (X[i], Y[i])), 3)
        # pygame.draw.line(fenetre, Couleur, Convertisseur_valeur_px(min_x, max_x, min_y, max_y, (X[i], Y[i])), Convertisseur_valeur_px(min_x, max_x, min_y, max_y, (X[i], Y[i])), 2)
        
    pygame.display.flip()

# WOC Graph.

pygame.init()

SIZE = (1200, 600)

fenetre = pygame.display.set_mode(SIZE)

pygame.font.init()
Police = pygame.font.SysFont('Consola', 20)

pygame.draw.rect(fenetre, Color(255, 255, 255), (19, 19, SIZE[0]-39, SIZE[1]-39), 1)

X = np.linspace(1, 10, 10000)
Y = np.cos(X)


Plot(X, Y, Color(255, 255, 0))
Plot(X, np.sin(X), Color(255, 0, 255))
Plot(X, X-2, Color(0, 255, 255))

# Configurer le paramétrage de l'intervalle de tracé s'il y a plusieurs courbes


pygame.display.flip()

i = 1
while i:

    for event in pygame.event.get():
        
        if event.type == QUIT:
            i = 0
            sys.exit(0)
            
    time.sleep(0.01)    
            
    pos_x, pos_y = pygame.mouse.get_pos()

    if 20 < pos_x < SIZE[0] - 20 and 20 < pos_y < SIZE[1] - 20:
    
        pygame.draw.rect(fenetre, Color(0, 0, 0), (SIZE[0] - 130, 0, 130, 19))
        fenetre.blit(Police.render(str(Convertisseur_px_valeur(v["min_x"], v["max_x"], v["min_y"], v["max_y"], (pos_x, pos_y))), False, (255, 255, 255)), (SIZE[0] - 130, 2))
        pygame.display.flip()