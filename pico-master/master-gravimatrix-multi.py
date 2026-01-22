
from pyparsing import line
import serial
import time
import numpy as np


def key_to_pixel_map(key_number, cols):
    row = key_number // cols
    column = (key_number % cols)
    return row, column

# Parameters
G = 1.0          # Gravitational constant
dt = 0.1         # Time step
softening = 0.5   # Softening length (epsilon)

# Initial positions (x, y), velocities (vx, vy), and masses
pos = None
vel = None


ser = serial.Serial('/dev/tty.usbmodem2103', 115200, timeout=0.1)

cols = 6
rows = 5
number_pixels = cols * rows

bin_edges = [np.arange(0, rows+1), np.arange(0, cols+1)]

cell_value = [0] * number_pixels

timestep = 0

# Create random collection of 10 particles
# pos = np.array([[0, 0]])
# vel = np.array([[0., 0.]])
# for i in range(10):
#     row = np.random.randint(0, rows)
#     col = np.random.randint(0, cols)
#     pos = np.append(pos, np.array([[float(row)+0.5, float(col)+0.5]]), axis=0)
#     vel = np.append(vel, np.array([[0., 0.]]), axis=0)

# erase everything
blank = ",".join(str(0) for n in cell_value)
ser.write(f"{blank}\n".encode("utf-8"))

while True:
    cell_id = None
    # if ser.in_waiting > 0:
    #     line = ser.readline().decode('utf-8').strip()
    #     try:
    #         cell_id = int(line)
    #     except ValueError:
    #         pass

    line = ser.readline().decode('utf-8').strip()
    try:
        cell_id = int(line)
    except ValueError:
        pass
    
    if cell_id is not None:
        # get the row and column
        row, col = key_to_pixel_map(cell_id, cols=cols)

        # add a particle to that position...
        if pos is None:
            pos = np.array([[float(row)+0.5, float(col)+0.5]])
            vel = np.array([[0., 0.]])
        else:
            pos = np.append(pos, np.array([[float(row)+0.5, float(col)+0.5]]), axis=0)
            vel = np.append(vel, np.array([[0, 0]]), axis=0)
    
        print(row, col)

    if pos is not None:

        timestep += 1
        print(f"Timestep {timestep}, Number of particles: {len(pos)}")

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
       
        # make a histogram of the positions
        grid, _,  _ = np.histogram2d(pos[:, 0], pos[:, 1], bin_edges)

        # flatten the grid to match cell_value
        cell_value = grid.flatten().astype(int).tolist()
    
        # send back the cell_values
        cell_value_str = ",".join(str(n) for n in cell_value)
        ser.write(f"{cell_value_str}\n".encode("utf-8"))