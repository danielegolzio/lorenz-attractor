import numpy as np
import pygame as pg
import ctypes

def main():
    pg.init()

    user32 = ctypes.windll.user32
    dimensions = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
    dimensions = 500, 500
    width = dimensions[0]
    height = dimensions[1]

    screen = pg.display.set_mode(dimensions)
    clock = pg.time.Clock()
    fps = 100

    screen.fill((0, 0, 0))

    size = 1
    population = 1
    scale = 12
    o = 10.0 # sigma
    rho = 28.0 # rho
    B = 8.0 / 3.0 # beta

    # particle class
    class particle:
        def __init__(self, t, x, y, z, color, scale):
            self.t = t
            self.x = x
            self.y = y
            self.z = z
            self.color = color
            self.scale = scale
        
        def calc(self):
            dx = (o * (self.y - self.x)) * self.t
            self.x = self.x + dx

            dy = ((self.x * (rho - self.z)) - self.y) * self.t
            self.y = self.y + dy

            dz = ((self.x * self.y) - (B * self.z)) * self.t
            self.z = self.z + dz

        def project(self):
            point = np.array(self.x, self.y, self.z)
            P = np.matrix(
                [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
            )
            projected = np.dot(P, point)
            projected = projected.tolist()
            self.x = projected[0]
            self.y = projected[1]

        def draw(self):
            x = (self.x * self.scale) + (width // 2)
            y = (self.y * self.scale) + (height // 2) 
            pg.draw.circle(screen, self.color, (x, y), size)

    p = [particle((0.01 + (i * (0.01 / population))), 0.01, 0, 0, (255, 255, 255), scale) for i in range(population)]

    run = True
    while run:
        clock.tick(fps)
        screen.fill((0,0,0))
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False

    for i in range(len(p)):
        p[i].calc()
        p[i].project()
        #p[i].draw()


if __name__ == "__main__":
    main()