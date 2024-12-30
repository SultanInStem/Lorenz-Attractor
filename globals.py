def to_math_coords(point, screen_size):
    math_x = point[0] - (screen_size[0] // 2) 
    math_y = point[1] - (screen_size[1] // 2)
    return (math_x, math_y, point[2]) 

def to_screen_coords(point, screen_size, scale): 
    screen_x = int((screen_size[0] // 2) + point[0] * scale)
    screen_y = int((screen_size[1] // 2) - point[1] * scale)
    return (screen_x, screen_y, point[2]) 