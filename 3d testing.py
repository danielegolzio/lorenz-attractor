from ursina import *

app = Ursina()

p = Entity(model="sphere", scale=(0.1, 0.1, 0.1), position=(0, 0, 0))
# dx = (o * (self.y - self.x)) * self.t
# self.x = self.x + dx

# dy = ((self.x * (rho - self.z)) - self.y) * self.t
# self.y = self.y + dy

# dz = ((self.x * self.y) - (B * self.z)) * self.t
# self.z = self.z + dz

o = 10.0  # sigma
rho = 28.0  # rho
B = 8.0 / 3.0  # beta
t = 0.001
scale = 0.1


def update():
    dx = (o * (p.y - p.x)) * t
    dy = ((p.x * (rho - p.z)) - p.y) * t
    dz = ((p.x * p.y) - (B * p.z)) * t
    p.x += dx
    p.y += dy
    p.z += dz
    p.x += held_keys["d"] * time.dt
    p.x -= held_keys["a"] * time.dt


app.run()
