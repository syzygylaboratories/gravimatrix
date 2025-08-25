import numpy as np
import board
import neopixel
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

# loop over each pixel in order lighting them up
for i in range(npixels):

    pixels[i] = (255, 0, 0)
    sleep(0.1)

