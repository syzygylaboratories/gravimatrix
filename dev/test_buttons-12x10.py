
import board
import keypad
import neopixel
import numpy as np

def key_to_pixel_map(key_number, cols):
    row = key_number // cols
    column = (key_number % cols)
    return row, column

# Define number of rows and columns
cols = 12
rows = 10

npixels = cols * rows
pixels = neopixel.NeoPixel(board.D18, npixels, brightness=1)


row_pins = (board.D26, board.D19, board.D13, board.D6, board.D5, board.D0, board.D11, board.D9, board.D10, board.D22)
column_pins = (board.D14, board.D15, board.D23, board.D24, board.D12, board.D25, board.D16, board.D20, board.D21, board.D27, board.D17, board.D4)


# THIS NEEDS TO BE UPDATED
keys = keypad.KeyMatrix(
    row_pins=row_pins,
    column_pins=column_pins,
    columns_to_anodes=False,
)

pixels.fill((0, 0, 0))


on = np.zeros(cols*rows)

# Simulation loop
while True:

    key_event = keys.events.get()
    if key_event:

        if key_event.pressed:

            # get the row and column
            row, col = key_to_pixel_map(key_event.key_number, cols=cols)

            print('added at', row, col)

            # the ordering of the cells is different from the LEDs
            if row < rows // 2:
                if row % 2 == 1:
                    col = cols - col - 1
            else:
                if row % 2 == 0:
                    col = cols - col - 1
                
            pixel = row * cols + col

            if on[pixel] == 0:
                pixels[pixel] = (255, 0, 0)
                on[pixel] = 1
            else:
                pixels[pixel] = (0, 0, 0)
                on[pixel] = 0

            
