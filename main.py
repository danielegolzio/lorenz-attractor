import numpy as np
import pygame
import typer
from colors import colors

def main(
    color: str = typer.Argument(None)
):

    if color == "r":
        colorI = 0
    elif color == "o":
        colorI = 1
    elif color == "y":
        colorI = 2
    elif color == "g":
        colorI = 3
    elif color == "b":
        colorI = 4
    elif color == "i":
        colorI = 5
    elif color == "v":
        colorI = 6
    else:
        colorI = 7

    pygame.init()
    dimensions = (1920, 1080)
    width = dimensions[0]//2
    height = dimensions[1]//2
    screen = pygame.display.set_mode(dimensions)
    clock = pygame.time.Clock()
    fps = 75

    o = 10.0 # sigma
    p = 28.0 # rho
    B = 8.0 / 3.0 # beta
    x = 0.01
    y = 0
    z = 0
    scale = 15

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
        
        pygame.draw.line(screen, colors[colorI], prev_coords, coords)
        pygame.display.update()

pygame.quit()

if __name__ == "__main__":
    typer.run(main)