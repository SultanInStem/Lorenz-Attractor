import pygame 
class Attractor: 
    def __init__(self, initial_pos, omega, rho):
        self.pos = initial_pos 
        self.omega = omega 
        self.rho = rho
        self.points = [] 
    def draw(self, screen): 
        for i in range(0, len(self.points) - 1):
            pygame.draw.line(screen,(255,255,255), self.points[i], self.points[i + 1])
    def update(self): 
        pass 

