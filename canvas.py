import pygame
import sys 
from globals import to_math_coords, to_screen_coords

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
    def render(self):
        self.screen.fill((0,0,0))

        pygame.draw.line(self.screen,(255,255,255),to_screen_coords((0,0), self.screen.get_size()), to_screen_coords((100,100), self.screen.get_size()))
        # pygame.draw.circle(self.screen, (255,255,255), to_screen_coords((0,0), self.screen.get_size()),20,0)

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

