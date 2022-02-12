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
    [VERSION]       Change plane of image       [default = xy]
    [POPULATION]    Number of particles         [default = 1]
    [SIZE]          Size of particle            [default = 1]
    [SPEED]         Change speed of particle    [default = 60]

Options:
    -t, --trail     Show particle trail         [default = False]   
```
