import numpy as np
import board
import keypad
import neopixel
from time import sleep
# from adafruit_seesaw import digitalio, rotaryio, seesaw
from utils import rainbow, key_to_pixel_map

ORDER = neopixel.GRB

# Define number of rows and columns
cols = 12
rows = 10
npixels = cols * rows


# Parameters
G = 1.0          # Gravitational constant
dt = 0.1         # Time step
softening = 0.5   # Softening length (epsilon)

pixels = neopixel.NeoPixel(board.D18, npixels, brightness=1)

# set all pixels to 0
pixels.fill((0, 0, 0))

# Initial positions (x, y), velocities (vx, vy), and masses
pos = None
vel = None

# Define x and y velocities, these are updated by the rotary encoder
vel_x = 0.0
vel_y = 0.0




# Define bin edges
bin_edges = [np.arange(0, rows+1), np.arange(0, cols+1)]

# THIS NEEDS TO BE UPDATED
row_pins = (board.D26, board.D19, board.D13, board.D6, board.D5, board.D0, board.D11, board.D9, board.D10, board.D22)
column_pins = (board.D14, board.D15, board.D23, board.D24, board.D12, board.D25, board.D16, board.D20, board.D21, board.D27, board.D17, board.D4)

# THIS NEEDS TO BE UPDATED
keys = keypad.KeyMatrix(
    row_pins=row_pins,
    column_pins=column_pins,
    columns_to_anodes=False,
)

# Begin with pixels off.
pixels.fill((0, 0, 0))  

    
# Simulation loop
while True:

    key_event = keys.events.get()
    if key_event:

        if key_event.pressed:

            # get the row and column
            row, col = key_to_pixel_map(key_event.key_number, cols=cols)

            print('added at', row, col)

            # add a particle to that position...

            if pos is None:
                pos = np.array([[float(row)+0.5, float(col)+0.5]])
                vel = np.array([[vel_x, vel_y]])
            else:
                pos = np.append(pos, np.array([[float(row)+0.5, float(col)+0.5]]), axis=0)
                vel = np.append(vel, np.array([[vel_x, vel_y]]), axis=0)
        
            print(pos)

    if pos is not None:

        N = len(pos)

        acc = np.zeros_like(pos)
        for i in range(N):
            for j in range(N):
                if i != j:
                    r = pos[j] - pos[i]
                    dist2 = np.dot(r, r) + softening**2
                    acc[i] += G * r / dist2**1.5

        vel += acc * dt
        pos += vel * dt
        # print('-----------')
        # print(acc)
        # print(vel)
        # print(pos)

        # make a histogram of the positions
        grid, _,  _ = np.histogram2d(pos[:, 0], pos[:, 1], bin_edges)

        # make a flattened version
        flattened_grid = grid.flatten()

        # loop over the cells and set the pixel value appropriately

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
            
            # pixels[i] = (255 * value / N, 0, 0)
            if value > 0:
                pixels[pixel] = rainbow(value * 10)
            else:
                pixels[pixel] = (0, 0, 0)

        sleep(0.01)
