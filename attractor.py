import pygame 
from globals import to_math_coords, to_screen_coords
import colorsys 
class Attractor: 
    def __init__(self, initial_pos, sigma, rho, beta, scale):
        self.pos = initial_pos 
        self.sigma = sigma 
        self.rho = rho
        self.beta = beta
        self.points = [initial_pos] 
        self.scale = scale
        self.max_z = initial_pos[2]
        self.min_z = initial_pos[2]
    def z_to_color(self, normalized_z): 
        r, g, b = colorsys.hsv_to_rgb(0.7 * (1 - normalized_z), 1, 1) 
        return (int(r * 255), int(g * 255), int(b * 255))
    def draw(self, screen): 
        screen_size = screen.get_size()
        for i in range(0, len(self.points)):
            pos = to_screen_coords(self.points[i], screen_size, self.scale)[:2]
            z = self.points[i][2]
            normalized_z = (z - self.min_z) / (self.max_z - self.min_z + 1e-5)
            color = self.z_to_color(normalized_z)
            pygame.draw.circle(screen, color, pos, 1, 0)
    def update(self, dt):
        current_x = self.pos[0]
        current_y = self.pos[1] 
        current_z = self.pos[2]
        dx = self.sigma * (current_y - current_x) * dt
        dy = (current_x * (self.rho - current_z) - current_y) * dt
        dz = (current_x * current_y - self.beta * current_z) * dt 
        x = current_x + dx 
        y = current_y + dy
        z = current_z + dz 
        self.pos = (x,y,z)
        self.points.append(self.pos) 

        self.min_z = min(self.min_z, z)
        self.max_z = max(self.max_z, z)
    def zoom_out(self): 
        self.scale /= 1.1 
    def zoom_in(self): 
        self.scale *= 1.1

