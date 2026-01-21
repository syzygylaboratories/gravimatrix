

from pyparsing import line
import serial
import time

ser = serial.Serial('/dev/tty.usbmodem2103', 115200, timeout=1)


number_pixels = 30

cell_value = [0] * number_pixels



while True:
    line = ser.readline().decode('utf-8').strip()

    try:
        cell_id = int(line)
    except ValueError:
       cell_id = None

    if cell_id is not None:
        print(cell_id)
        cell_value[cell_id] += 1
        print(cell_value)

    # send back the cell_values
    cell_value_str = ",".join(str(n) for n in cell_value)
    ser.write(f"{cell_value_str}\n".encode("utf-8"))
    time.sleep(0.1)