import pygame
import sys 
from globals import to_math_coords, to_screen_coords
from attractor import Attractor 
class Canvas: 
    def __init__(self, size): 
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Lorenz Attractor")
        self.clock = pygame.time.Clock()
        self.running = True 
        self.dt = 0.01
        self.screen_size = self.screen.get_size()
        self.attractor = Attractor(initial_pos=(1,0,0), omega=10, rho=28, beta=8/3, scale=10)
    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
    def render(self):
        self.screen.fill((0,0,0))

        self.attractor.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)
    def update(self):
        self.attractor.update(self.dt) 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: 
            self.attractor.zoom_in()
        elif keys[pygame.K_DOWN]: 
            self.attractor.zoom_out()
    def run(self):
        while(self.running):
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()

