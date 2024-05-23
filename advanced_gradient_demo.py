from neopixel import NeoPixel
import time

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

np = NeoPixel(0, 30)

width = 20
colors = [(0, 255, 255), (127, 0, 255), (255, 0, 0), (127, 255, 0)]
color_gradient = create_advanced_gradient(colors, width)

while True:
    for i in range(np.n):
        np.fill((0, 0, 0))
        for j in range(width):
            np[(i + j) % np.n] = color_gradient[j]
        np.write()
        time.sleep(0.025)
