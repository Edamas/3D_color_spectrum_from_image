import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

size_factor = 100

image = 'samples/f08924dda7324d118f8e824592dee046.jpg'

im = Image.open(image)
px = im.load()
print('Image loaded:', image)
height = im.height
width = im.width
total_pixels = height * width
print('Image size:', im.height, 'x', im.width, '\ttotal:', total_pixels)

print('Processing image pixels:')
count = 0
rgb_count = {}
for row in range(height):
    for col in range(width):
        r, g, b = px[col, row]
        rgb = (r / 255, g / 255, b / 255)
        if rgb not in rgb_count:
            rgb_count[rgb] = 1
        else:
            rgb_count[rgb] += 1
        if 10 * count % total_pixels == 0:
            print(f'{100 * count // total_pixels}%', end=' ')
        count += 1

print('Processing data.')
x = [x[0] for x in rgb_count]
y = [y[1] for y in rgb_count]
z = [z[2] for z in rgb_count]
colors = list(rgb_count.keys())
max_count = np.max(list(rgb_count.values()))
sizes = [(rgb_count[rgb] / max_count) * size_factor for rgb in rgb_count]
print('Highest frequency:', max_count, 'for color(s):', [key for key, value in rgb_count.items() if value == max_count])

print('Generating graph.')
plt.gcf().set_dpi(300)
ax = plt.axes(projection='3d', label='rgb')
ax.scatter(x,
           y,
           z,
           c=colors,
           s=sizes,
           alpha = 0.3
           )
plt.title(image.split('/')[-1].split('\\')[-1])
plt.show()
print('Done!')
