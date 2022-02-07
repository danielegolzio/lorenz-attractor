import numpy as np
import pygame

def lorenz():

    pygame.init()
    dimensions = (1920, 1080)
    width = dimensions[0]//2
    height = dimensions[1]//2
    screen = pygame.display.set_mode(dimensions)
    clock = pygame.time.Clock()
    fps = 75
    white = (255,255,255)

    o = 10.0 # sigma
    p = 28.0 # rho
    B = 8.0 / 3.0 # beta
    x = 0.01
    y = 0
    z = 0
    scale = 16
    t = 0

    run = True
    screen.fill((0,0,0))
    while run:
        clock.tick(fps)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
        
        prev_coords = (int((x*scale)+500+width//2),int((y*scale)+height//2)+height//2)

        t = 0.01
        dx = (o * (y - x)) * t
        x = x + dx

        dy = ((x * (p - z)) - y) * t
        y = y + dy

        dz = ((x * y) - (B * z)) * t
        z = z + dz
        
        coords = (int((x*scale)+500+width//2),int((y*scale)+height//2)+height//2)
        
        # pygame.draw.circle(screen, white, coords, 2)
        # pygame.draw.circle(screen, white, prev_coords, 2)
        pygame.draw.line(screen, white, prev_coords, coords)
        pygame.display.update()
pygame.quit()

if __name__ == "__main__":
    lorenz