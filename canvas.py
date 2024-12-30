import pygame
import sys 
from globals import to_math_coords, to_screen_coords
from attractor import Attractor 
class Canvas: 
    def __init__(self, size): 
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Lorenz")
        self.clock = pygame.time.Clock()
        self.running = True 
        self.time = 0
        self.screen_size = self.screen.get_size()
        self.attractor = Attractor((0,0),10,12)
    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
    def render(self):
        self.screen.fill((0,0,0))


        pygame.display.flip()
        self.clock.tick(60)
    def update(self): 
        pass
    def run(self):
        while(self.running):
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()

