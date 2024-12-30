import pygame
import sys 


class Canvas: 
    def __init__(self, size): 
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Lorenz")
        self.clock = pygame.time.Clock()
        self.running = True 
    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False

    def run(self):
        while(self.running):
            pass 

        
        pygame.quit()
        sys.exit()

