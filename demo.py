from neopixel import NeoPixel
import time

def create_gradient(start_color, end_color, steps):
    gradient = []
    for step in range(steps):
        interpolated_color = (
            int(start_color[0] + (end_color[0] - start_color[0]) * step / (steps - 1)),
            int(start_color[1] + (end_color[1] - start_color[1]) * step / (steps - 1)),
            int(start_color[2] + (end_color[2] - start_color[2]) * step / (steps - 1))
        )
        gradient.append(interpolated_color)
    return gradient

def create_advanced_gradient(colors, steps):
    intervals = len(colors) - 1
    steps_per_interval = steps // intervals
    
    gradient = []
    for i in range(intervals):
        start_color = colors[i]
        end_color = colors[i+1]
        for step in range(steps_per_interval + (steps % intervals > i)):
            interpolated_color = (
                int(start_color[0] + (end_color[0] - start_color[0]) * step / steps_per_interval),
                int(start_color[1] + (end_color[1] - start_color[1]) * step / steps_per_interval),
                int(start_color[2] + (end_color[2] - start_color[2]) * step / steps_per_interval)
            )
            gradient.append(interpolated_color)
    return gradient

np = NeoPixel(1, 30)

#Simple demo
width = 8
for i in range(4):
    for j in range(np.n):
        np.fill((0, 0, 0))
        for k in range(width):
            if j + k < np.n:
                np[j + k] = (255, 255, 255)
        np.write()
        time.sleep(0.025)
np.fill((0, 0, 0))
np.write()

#Return demo
for i in range(2):
    for j in range(np.n):
        np.fill((0, 0, 0))
        np[j] = (255, 255, 255)
        np.write()
        time.sleep(0.025)
    for j in range(np.n):
        np.fill((0, 0, 0))
        np[np.n - j - 1] = (255, 255, 255)
        np.write()
        time.sleep(0.025)
np.fill((0, 0, 0))
np.write()

#Gradient demo
width = 15
color_gradient = create_gradient((255, 125, 255), (125, 255, 255), width)
for i in range(4):
    for j in range(np.n):
        np.fill((0, 0, 0))
        for k in range(width):
            np[(j + k) % np.n] = color_gradient[k]
        np.write()
        time.sleep(0.025)
np.fill((0, 0, 0))
np.write()

#Advanced gradient demo
width = 15
colors = [(0, 255, 255), (127, 0, 255), (255, 0, 0), (127, 255, 0)]
color_gradient = create_advanced_gradient(colors, width)
for i in range(4):
    for j in range(np.n):
        np.fill((0, 0, 0))
        for k in range(width):
            np[(j + k) % np.n] = color_gradient[k]
        np.write()
        time.sleep(0.025)
np.fill((0, 0, 0))
np.write()
