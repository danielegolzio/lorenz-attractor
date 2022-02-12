import pygame
import random
from colors import colors
import random

# pygame initialize
pygame.init()

dimensions = (1920,1080)
width = dimensions[0]//2
height = dimensions[1]//2

screen = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()

run = True
screen.fill((0,0,0))

fps = 60
scale = 15

# constants
o = 10.0 # sigma
rho = 28.0 # rho
B = 8.0 / 3.0 # beta

# particle class
class particle():
    def __init__(self, t, x, y, z, color):
        self.t = t
        self.x = x
        self.y = y
        self.z = z
        self.color = color

    def calc(self):
        dx = (o * (self.y - self.x)) * self.t
        self.x = self.x + dx

        dy = ((self.x * (rho - self.z)) - self.y) * self.t
        self.y = self.y + dy

        dz = ((self.x * self.y) - (B * self.z)) * self.t
        self.z = self.z + dz

    def draw(self):
        coords = (int((self.x*scale)+500+width//2),int((self.y*scale)+height//2)+height//2)
        pygame.draw.circle(screen, self.color, coords, 5)
        pygame.display.update()

population = 12

# p = [particle((0.01+(i*0.001)), 0.01, 0, 0, (random.choice(colors))) for i in range(population)]
p = [particle((0.01+(i*(0.01/population))), 0.01, 0, 0, (random.randint(50,255),random.randint(50,255),random.randint(50,255))) for i in range(population)]


while run:
    screen.fill((0,0,0))
    clock.tick(fps)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    for i in range(len(p)):
        p[i].calc()
        p[i].draw()