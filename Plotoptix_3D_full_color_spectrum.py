import numpy as np
from plotoptix import TkOptiX
from PIL import Image

color_range = 101
arredondamento = 10
particle_size = 0.2 / color_range

colors = []
cont = 0
for red in range(0, color_range):
    red = round(red / color_range, arredondamento)
    for green in range(0, color_range):
        green = round(green / color_range, arredondamento)
        for blue in range(0, color_range):
            blue = round(blue / color_range, arredondamento)
            if red == green == blue:
                colors.append([red, green, blue])
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
               r=particle_size,
               u=[particle_size, 0, 0],
               w=[0, 0, particle_size],
               c=colors,  # map_to_colors(cubes, 'Spectral')
               geom="ParticleSet")  #Parallelepipeds
optix.set_coordinates()  # show coordinates box
optix.show()
optix.setup_light("light1", color=100, radius=2)  # 10 * np.array([0.99, 0.9, 0.7])
print("done")

