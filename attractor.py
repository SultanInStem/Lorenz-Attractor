import pygame 
from globals import to_math_coords, to_screen_coords
class Attractor: 
    def __init__(self, initial_pos, omega, rho, beta, scale):
        self.pos = initial_pos 
        self.omega = omega 
        self.rho = rho
        self.beta = beta
        self.points = [initial_pos] 
        self.scale = scale
    def draw(self, screen): 
        screen_size = screen.get_size()
        for i in range(0, len(self.points) - 1):
            print(self.points[i])
            pos = to_screen_coords(self.points[i], screen_size, self.scale)[:2]
            pygame.draw.circle(screen, (255,255,255), pos, 1, 0)
    def update(self, dt):
        current_x = self.pos[0]
        current_y = self.pos[1] 
        current_z = self.pos[2]
        dx = self.omega * (current_y - current_x) * dt
        dy = (current_x * (self.rho - current_z) - current_y) * dt
        dz = (current_x * current_y - self.beta * current_z) * dt 
        x = current_x + dx 
        y = current_y + dy
        z = current_z + dz 
        self.pos = (x,y,z)
        self.points.append(self.pos)
    def zoom_out(self): 
        self.scale /= 1.1 
    def zoom_in(self): 
        self.scale *= 1.1

