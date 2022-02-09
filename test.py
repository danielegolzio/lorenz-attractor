import pygame

# pygame init
pygame.init()

dimensions = (1920,1080)
width = dimensions[0]//2
height = dimensions[1]//2

screen = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()

fps = 20
scale = 15

# constants
o = 10.0 # sigma
p = 28.0 # rho
B = 8.0 / 3.0 # beta

class particle:
    def __init__(self, t):
        self.t = t

    def pos(self, x, y, z):
        dx = (o * (y - x)) * self.t
        x = x + dx

        dy = ((x * (p - z)) - y) * self.t
        y = y + dy

        dz = ((x * y) - (B * z)) * self.t
        z = z + dz

        return x, y, z

p1 = particle(0.01)
p2 = particle(0.05)
x, y, z = 0.01, 0, 0

# for i in range(500):
#     x, y, z = p1.pos(x, y, z)
#     print(x, y, z)

run = True
screen.fill((0,0,0))

while run:
    clock.tick(fps)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    x, y, z = p2.pos(x, y, z)
    prev_coords = (int((x*scale)+500+width//2),int((y*scale)+height//2)+height//2)
    pygame.draw.circle(screen, (255, 0, 0), prev_coords, 1)

    x, y, z = p1.pos(x, y, z)

    coords = (int((x*scale)+500+width//2),int((y*scale)+height//2)+height//2)

    pygame.draw.circle(screen, (255, 255, 255), coords, 1)
    pygame.display.update()

pygame.quit()

