import numpy as np
from plotoptix import TkOptiX
from PIL import Image

im = Image.open(r"samples\color spectrum.png")
px = im.load()

colors = []
cont = 0
for row in range(0, im.height):
    for col in range(0, im.width):
        pix = px[col, row]
        newCol = (round(pix[0] / 255, 2), round(pix[1] / 255, 2), round(pix[2] / 255, 2))
        colors.append(newCol)
        if cont % 100000 == 0:
            print(cont, end=' ')
        cont += 1
colors = np.unique(colors, axis=0)
print(len(colors))
optix = TkOptiX() # create and configure, show the window later
optix.set_param(max_accumulation_frames=30)  # accumulate up to 30 frames (override default of 4 frames)
optix.set_background(0.10)  # white background
optix.set_data(name="colors",
               pos=colors,
               r=0.005,
               u=[0.005, 0, 0],
               w=[0, 0, 0.005],
               c=[[r, g, b, 0.01] for r, g, b in colors],  # map_to_colors(cubes, 'Spectral')
               geom="Parallelepipeds")  # ParticleSet
optix.set_coordinates()  # show coordinates box
optix.show()
optix.setup_light("light1", color=10 * np.array([0.99, 0.9, 0.7]), radius=2)
print("done")
