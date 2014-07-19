# some refactoring and this time I generate very FEW colored pixels
import sys, pygame, noisey, random, blairtool
random.seed()

my_surface, surface_width, surface_height = blairtool.init_pygame()

def rando():
	return int(random.uniform(2,254))

def noisyColor(_n):
	n = int(round(_n))
	return pygame.Color(rando()*n,rando()*n,rando()*n,1)

def pixel(surface, color, pos):
	surface.fill(color, (pos, (1, 1)))

my_noise = noisey.generateWhiteNoiseNumpy(surface_width, surface_height, 0.0, 0.2)
for i in range(0,surface_height):
	for j in range(0,surface_width):
		pixel(my_surface, noisyColor(my_noise[i][j]), (j,i))

pygame.image.save(my_surface,blairtool.out_file_name())
