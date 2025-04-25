# Drag the Dot Through the Pipe

A simple Python game using Pygame where you drag a blue dot through a pipe without touching the edges.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Step 1: Install Mesa drivers
```bash
sudo apt update
sudo apt install libgl1-mesa-glx libgl1-mesa-dri mesa-utils
```

3. Step 2: Test OpenGL
After installing the drivers, you can test OpenGL with:

```bash
glxinfo | grep OpenGL
```
If glxinfo isn't found:

```bash
sudo apt install mesa-utils
```

## Build Docker
```bash
docker build -t game_labs .
```

## Run Docker
```bash
docker run --rm -it \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --device /dev/snd \
    game_labs
```

# game-labs
# game-labs
