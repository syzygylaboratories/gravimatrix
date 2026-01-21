

import serial
import time

ser = serial.Serial('/dev/tty.usbmodem2103', 115200, timeout=1)

while True:
    line = ser.readline().decode('utf-8').strip()
    if line:
        print("Received:", line)

    ser.write(b"Hello from computer\n")    
    time.sleep(1)