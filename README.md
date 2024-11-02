# Lorenz attractor
<img src="https://i.ibb.co/F7QW7Tn/1.png" alt="xy plane" width=200 height=200><img src="https://i.ibb.co/0mbYDgH/1.png" alt="xz plane" width=200 height=200>
## Getting started

### Installation
- Clone repo and install dependencies with pip
```
git clone https://github.com/poonchoi/lorenz-attractor
```
```
pip install -r requirements.txt
```
## Usage
- To view lorenz attractor, run
```
cd v1
python main.py [arguments]
``` 
```
Arguments:
    [POPULATION]    Number of particles         [default = 1]
    [SIZE]          Size of particle            [default = 1]
    [PLANE]         Change plane of image       [default = xy]
    [SPEED]         Change speed of particle    [default = 60]

Options:
    --help          Show all arguments          [default = False]
    -f, --funky     Random plane per particle   [default = False]
    -t, --trail     Show particle trail         [default = False]
    -r, --random    Random plane                [default = False]
```
# Lorenz Attractor library
## Usage

```
it's located under lorenz-attractor/lorenz

you can either use particle.py (made by me) or particle_besir.py (if you know you know)

Particle class makes one point that follows the lorenz attractor (in 3D)

open 3D_example.py to see example usage of particle class
```

