# similar to pico-test but send values to master-cell


import board
import neopixel
import time
import keypad
from rainbowio import colorwheel
import usb_cdc

serial = usb_cdc.data

print(dir(board))


number_pixels = 30

pixels = neopixel.NeoPixel(board.GP0, number_pixels, brightness=1)

for i in range(255):
    pixels.fill(colorwheel(i))
    time.sleep(0.001)

for i in range(number_pixels):
    pixels[i] = (0, 10, 0)
    time.sleep(0.01)

pixels.fill((0,0,0))

keys = keypad.KeyMatrix(
    row_pins=(board.GP18, board.GP19, board.GP20, board.GP21, board.GP22),
    column_pins=(board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7,),
    columns_to_anodes=False,
)


pixel_mapping = [0,1,2,3,4,5,11,10,9,8,7,6,12,13,14,15,16,17, 23, 22, 21, 20, 19, 18, 24, 25, 26, 27, 28, 29]


while True:

    # send key press
    key_event = keys.events.get()
    if key_event:

        if key_event.pressed:

            key_number = key_event.key_number

            print(key_number)
            serial.write(f"{key_number}\n".encode("utf-8"))
        
    # Check for incoming data
    if serial.in_waiting:
        incoming = serial.readline().decode("utf-8").strip()

        cell_values = [int(x) for x in incoming.split(",")]

        for i in range(number_pixels):
            pixel_number = pixel_mapping[i]
            if cell_values[i] == 0:
                pixels[pixel_number] = (0,0,0)
            else:   
                pixels[pixel_number] = colorwheel(cell_values[i]*10)



