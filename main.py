import pygame
import random
import typer

def main(
    version: str = typer.Argument("xy",help=("Change image plane          ")),
    population: int = typer.Argument("1",help=("Change number of particles  ")),
    size: int = typer.Argument("1",help=("Change size of particle     ")),
    speed: int = typer.Argument("60",help=("Change speed of particle    "))
):
    # pygame initialize
    pygame.init()

    dimensions = (1920,1080)
    width = dimensions[0]//2
    height = dimensions[1]//2

    screen = pygame.display.set_mode(dimensions)
    clock = pygame.time.Clock()

    screen.fill((0,0,0))

    if size != None:
        size = size
    else:
        size = 1

    # constants
    o = 10.0 # sigma
    rho = 28.0 # rho
    B = 8.0 / 3.0 # beta

    # particle class
    class particle():
        def __init__(self, t, x, y, z, color, scale, version):
            self.t = t
            self.x = x
            self.y = y
            self.z = z
            self.color = color
            self.scale = scale
            self.version = version

        def calc(self):
            dx = (o * (self.y - self.x)) * self.t
            self.x = self.x + dx

            dy = ((self.x * (rho - self.z)) - self.y) * self.t
            self.y = self.y + dy

            dz = ((self.x * self.y) - (B * self.z)) * self.t
            self.z = self.z + dz

        def draw(self):
            if self.version == "xy" or self.version == "yx":
                coords = (int((self.x*self.scale)+500+width//2),int((self.y*self.scale)+height//2)+height//2)
            elif self.version == "zy" or self.version == "yz":
                coords = (int((self.z*self.scale)+80+width//2),int((self.y*self.scale)+height//2)+height//2)
            elif self.version == "xz" or self.version == "zx":
                coords = (int((self.x*self.scale)+500+width//2),int((self.z*self.scale)+height//4))
            else:
                coords = (int((self.x*self.scale)+500+width//2),int((self.y*self.scale)+height//2)+height//2)

            pygame.draw.circle(screen, self.color, coords, size)
            pygame.display.update()

    if speed != None:
        fps = speed
    else:
        fps = 60

    if version == "xy" or version == "yx":
        scale = 15
    elif version == "zy" or version == "yz":
        scale = 15
    elif version == "xz" or version == "zx":
        scale = 17
    else:
        scale = 15
    
    if population != None:
        population = population
    else:
        population = 1

    p = [particle((0.01+(i*(0.01/population))), 0.01, 0, 0, (random.randint(50,255),random.randint(50,255),random.randint(50,255)), scale, version) for i in range(population)]

    run = True
    while run:
        screen.fill((0,0,0))
        clock.tick(fps)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False

        for i in range(len(p)):
            p[i].calc()
            p[i].draw()

pygame.quit()

if __name__ == "__main__":
    typer.run(main)