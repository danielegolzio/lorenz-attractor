import lorenz.particle as P
import pygame as pg

def main():
    fps = 200
    screen = pg.display.set_mode(P.dimensions)
    clock = pg.time.Clock()

    population = 100
    scale = 15
    point_size = 1
    angle = 0

    p = [P.Particle((0.01+(i*(0.01/population))),[0.1,0,0], scale) for i in range(population)]

    while True:
        angle += 0.005
        screen.fill((0,0,0))
        for i in range(len(p)):
            p[i].calc()
            p[i].rotateY(angle)
            point = p[i].project()
            pg.draw.circle(screen, (255,255,255), point, point_size)

        [exit() for i in pg.event.get() if i.type == pg.QUIT]
        pg.display.set_caption(f"{round(clock.get_fps())} FPS")
        pg.display.flip()
        clock.tick(fps)

if __name__ == '__main__':
    main()