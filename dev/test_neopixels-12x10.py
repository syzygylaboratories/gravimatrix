import board
import neopixel
import numpy as np
from time import sleep


ORDER = neopixel.GRB


ncols = 12
nrows = 10
npixels = ncols * nrows

pixels = neopixel.NeoPixel(board.D18, npixels, brightness=1)

# set all pixels to 0 (black)
pixels.fill((0, 0, 0))

sleep(1)

# set all pixels to max (white)
pixels.fill((255, 255, 255))

sleep(2)

# set all pixels to min
pixels.fill((0, 0, 0))

rows = 10
cols = 12

grid = np.ones((cols, rows))
flattened_grid = grid.flatten()






for cell, value in enumerate(flattened_grid):

    # the ordering of the cells is different from the LEDs
    row = cell // cols
    col = cell % cols

    if row < rows // 2:
        if row % 2 == 1:
            col = cols - col - 1
    else:
        if row % 2 == 0:
            col = cols - col - 1
        
    pixel = row * cols + col

    pixels[pixel] = (255, 0, 0)
    sleep(0.05)
    pixels[pixel] = (0, 0, 0)

