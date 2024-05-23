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

np = NeoPixel(0, 30)

width = 20
color_gradient = create_gradient((255, 125, 255), (125, 255, 255), width)

while True:
    for i in range(np.n):
        np.fill((0, 0, 0))
        for j in range(width):
            np[(i + j) % np.n] = color_gradient[j]
        np.write()
        time.sleep(0.025)
