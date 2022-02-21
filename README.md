# Lorenz attractor
<img src="https://i.ibb.co/F7QW7Tn/1.png" alt="xy plane" width=200 height=200><img src="https://i.ibb.co/0mbYDgH/1.png" alt="xz plane" width=200 height=200><img src="https://i.ibb.co/MDZPTmq/1.png" alt="yz plane" width=200 height=200>
## Getting started

### Installation
- Clone repo and install dependencies with pip
```
git clone https://github.com/poonchoi/lorenz-attractor.git
```
```
pip install -r requirements.txt
```
## Usage
- To view lorenz attractor, run
```
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

