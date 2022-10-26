import colorsys
import numpy as np
import pygame as pg
import ctypes

def main():
    pg.init()
    dimensions = 800, 600
    width = dimensions[0]
    height = dimensions[1]
    screen = pg.display.set_mode(dimensions)
    clock = pg.time.Clock()
    fps = 60

    size = 1
    angle = 0
    population = 10
    scale = 6
    o = 10.0 # sigma
    rho = 28.0 # rho
    B = 8.0 / 3.0 # beta

    class Particle:
        def __init__(self, t, x, y, z, color, scale, size):
            self.t = t
            self.x = x
            self.y = y
            self.z = z
            self.color = color
            self.scale = scale
            self.size = size
        
        def calc(self):
            dx = (o * (self.y - self.x)) * self.t
            self.x = self.x + dx

            dy = ((self.x * (rho - self.z)) - self.y) * self.t
            self.y = self.y + dy

            dz = ((self.x * self.y) - (B * self.z)) * self.t
            self.z = self.z + dz

        def project(self):
            point = np.array([self.x, self.y, self.z])
            P = np.matrix(
                [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
            )
            projected = np.dot(P, point)
            projected = projected.tolist()
            self.x = projected[0][0]
            self.y = projected[0][1]

        def rotateX(self, angle):
            point = np.array([self.x, self.y, self.z])
            rotateX = np.matrix(
                [[1, 0, 0],
                [0, np.cos(angle), np.sin(angle)],
                [0, -np.sin(angle), np.cos(angle)]]
            )
            rotated = np.dot(rotateX, point)
            rotated = rotated.tolist()
            rotated = [rotated[0][0], rotated[0][1], rotated[0][2]]
            self.x, self.y, self.z = rotated
        
        def rotateY(self, angle):
            point = np.array([self.x, self.y, self.z])
            rotateY = np.matrix(
            [[np.cos(angle), 0, -np.sin(angle)],
            [0, 1, 0],
            [np.sin(angle), 0, np.cos(angle)]]
            )
            rotated = np.dot(rotateY, point)
            rotated = rotated.tolist()
            rotated = [rotated[0][0], rotated[0][1], rotated[0][2]]
            self.x, self.y, self.z = rotated

        def draw(self):
            x = (self.x * self.scale) + (width // 2)
            y = (self.y * self.scale) + (height // 2)
            pg.draw.circle(screen, self.color, (x, y), self.size)

    p = [Particle((0.01+(i*(0.01/population))),0.01,0,0,(255,255,255),scale, size) for i in range(population)]
    while True:
        angle -= 0.0001
        screen.fill((0,0,0))
        for i in range(len(p)):
            p[i].calc()
            p[i].rotateX(angle)
            # p[i].rotateY(angle)
            p[i].project()
            p[i].draw()

        [exit() for i in pg.event.get() if i.type == pg.QUIT]
        pg.display.set_caption(f"{round(clock.get_fps())} FPS")
        pg.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    main()