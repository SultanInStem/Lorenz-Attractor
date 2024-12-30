import pygame
import sys 


class Canvas: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Lorenz")