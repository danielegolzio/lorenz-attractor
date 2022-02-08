# Lorenz attractor

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
    [VERSION]   Change plane of image - xy, xz, yz
    [COLOR]     Change color of the line with first letter of ROYGBIV
    [SPEED]     Change speed of drawing - default = 60
```



- To generate an image, run
```
python main.py [NUM_OF_IMAGES] [OPTION]...
```
```
Arguments:
    NUM_OF_IMAGES [required]   Number of images you want to generate
 
Options:
  -b, --bar     Show progress bar when generating images
  -s, --show    Open image folder on completion
  --help        Show all options
```
