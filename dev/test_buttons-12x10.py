
import board
import keypad

def key_to_pixel_map(key_number, cols):
    row = key_number // cols
    column = (key_number % cols)
    return row, column

# Define number of rows and columns
cols = 12
rows = 10




row_pins = (board.D26, board.D19, board.D13, board.D6, board.D5, board.D0, board.D11, board.D9, board.D10, board.D22)
row_pins = (board.D26, board.D19, board.D13, board.D6, board.D5, board.D0,)
# row_pins = (board.D26, board.D19)
column_pins = (board.D14, board.D15, board.D23, board.D24, board.D25, board.D8, board.D7, board.D1, board.D12, board.D16, board.D20, board.D21)
column_pins = (board.D14, board.D15, board.D23, board.D24, board.D25, board.D12, board.D16, board.D20, board.D21)
# column_pins = (board.D14, board.D15)


cols = len(column_pins)
rows = len(row_pins)


print(len(row_pins))
print(len(column_pins))

# THIS NEEDS TO BE UPDATED
keys = keypad.KeyMatrix(
    row_pins=row_pins,
    column_pins=column_pins,
    columns_to_anodes=False,
)


    
# Simulation loop
while True:

    key_event = keys.events.get()
    if key_event:

        if key_event.pressed:

            # get the row and column
            row, col = key_to_pixel_map(key_event.key_number, cols=cols)

            print('added at', row, col)

            
