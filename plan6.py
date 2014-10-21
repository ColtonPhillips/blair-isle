# goal: create a map. for real this time.

import sys, pygame, noisey, random, blairtool, os
random.seed()

my_surface, surface_width, surface_height = blairtool.init_pygame()

def pixel(surface, color, pos):
	surface.fill(color, (pos, (1, 1)))

def get_weighted_area(noise, width=surface_width, height=surface_height):
	w_area = [[0 for r in range(width)] for i in range(height)]
	max_noise = 0
	noise_width = len(noise[0])
	noise_height = len(noise)
	for i in range(width):
		for j in range(height):
			my_x = int((float(i) / float(width)) * float(noise_width))
			my_y = int((float(j) / float(height)) * float(noise_height))
			w_area[j][i] = noise[my_y][my_x]
			if (w_area[j][i] > max_noise):
				max_noise = w_area[j][i]
	
#	for i in range(width):
#		for j in range(height):
#			w_area[j][i] /= max_noise
	return w_area		

# THE ALGORITHM

my_noise = noisey.generatePerlinNoise(2	,2 )
my_weight = get_weighted_area(my_noise)

i = 1
while (i < surface_width/2):
	my_small_noise = noisey.generatePerlinNoise(i,i)
	my_new_weight = get_weighted_area(my_small_noise)
	import numpy as np
	my_weight = np.add(my_weight, my_new_weight)
	i = i * 2

#now we have my_weight. Let's normalize it to 0-1	

max_val = 0.0
min_val = 99999999.0

for i in range(surface_width):
	for j in range(surface_height):
		if my_weight[j][i] > max_val:
				max_val = my_weight[j][i]
		if my_weight[j][i] < min_val:
				min_val = my_weight[j][i]

for i in range(surface_width):
	for j in range(surface_height):
		my_weight[j][i] = (my_weight[j][i]-min_val)/(max_val-min_val)
		
# there. now the data is normalized. :D
# lets fucking draw it!
color_surface = pygame.image.load(os.path.join('input','color_sheet.png'))
color_width = float(color_surface.get_width()) - 1
for i in range(0,surface_height):
	for j in range(0,surface_width):
		my_color = color_surface.get_at((int(my_weight[j][i]*color_width),0))
		pixel(my_surface, my_color ,(j,i))

pygame.image.save(my_surface,blairtool.out_file_name())
