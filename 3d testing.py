from p5 import *


def setup():
    size(720, 720)


def draw():
    no_stroke()
    background(205, 102, 94)
    rotate_x(frame_count * 0.02)
    rotate_y(frame_count * 0.01)
    blinn_phong_material()
    cone(200, 300)
    locX = mouse_x - width / 2
    locY = mouse_y - height / 2
    light_specular(0, 0, 255)
    point_light(360, 360 * 1.5, 360, locX, locY, 400)


# def draw():
#     stroke(114)
#     background(0, 0, 0)
#     rotate_x(-mouse_y * 0.02)
#     rotate_z(frame_count * 0.02)
#     rotate_z(-mouse_x * 0.02)
#     cone(300, 500)


if __name__ == "__main__":
    run(mode="P3D")
