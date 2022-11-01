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
    population = 100
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
            self.xproj = 0
            self.yproj = 0
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
            x, y, z = self.x, self.y, self.z
            point = np.array([x, y, z])
            P = np.matrix(
                [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
            )
            projected = np.dot(P, point)
            projected = projected.tolist()
            self.xproj = projected[0][0]
            self.yproj = projected[0][1]

        def rotateX(self, angle):
            x, y, z = self.x, self.y, self.z
            point = np.array([x, y, z])
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
            x, y, z = self.x, self.y, self.z
            point = np.array([x, y, z])
            rotateY = np.matrix(
            [[np.cos(angle), 0, -np.sin(angle)],
            [0, 1, 0],
            [np.sin(angle), 0, np.cos(angle)]]
            )
            rotated = np.dot(rotateY, point)
            rotated = rotated.tolist()
            rotated = [rotated[0][0], rotated[0][1], rotated[0][2]]
            self.x, self.y, self.z = rotated

        def rotateZ(self, angle):
            x, y, z = self.x, self.y, self.z
            point = np.array([x, y, z])
            rotateZ = np.matrix(
                [[np.cos(angle), np.sin(angle), 0],
                [-np.sin(angle), np.cos(angle), 0],
                [0, 0, 1]]
            )
            rotated = np.dot(rotateZ, point)
            rotated = rotated.tolist()
            rotated = [rotated[0][0], rotated[0][1], rotated[0][2]]
            self.x, self.y, self.z = rotated

        def draw(self):
            x = (self.xproj * self.scale) + (width // 2)
            y = (self.yproj * self.scale) + (height // 2)
            # x = (self.x * self.scale)
            # y = (self.y * self.scale)
            pg.draw.circle(screen, self.color, (x, y), self.size)

    p = [Particle((0.01+(i*(0.01/population))),0.01,0,0,(255,255,255),scale, size) for i in range(population)]

    while True:
        angle += 0.0005
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