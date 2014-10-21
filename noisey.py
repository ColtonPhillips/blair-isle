import random
import math

#random.seed()

# range is [0,1] , either 0 or 1
def generateWhiteNoise(width,height):
	noise = [[r for r in range(width)] for i in range(height)]

	for i in range(0,height):
		for j in range(0,width):
			noise[i][j] = random.randint(0,1)

	return noise

# range is [0,1]
def generateWhiteNoiseNumpy(width,height,loc=0.5,sd=0.5):
	import numpy
	noise = numpy.random.normal(loc,sd,(height,width))
	for (x,y), value in numpy.ndenumerate(noise):
		if noise[x,y] < 0: noise[x,y] = 0
		if noise[x,y] > 1: noise[x,y] = 1

	return noise

#noise3(x, y, z, octaves=1, persistence=0.5, lacunarity=2.0repeatx=1024, repeaty=1024, repeatz=1024, base=0.0)
def generatePerlinNoise(width,height,octaves=16,persistance=0.7,lacunarity=3.0,repeatx=10024,repeaty=10024,base=0):
	base = random.randint(0,1024)
	print (base)
	big_number = float(max(width,height) + 2)
	from noise import pnoise3
	my_noise = [[r for r in range(width)] for i in range(height)]
	_r = random.random()
	for i in range(0,height):
		for j in range(0,width):
			#my_noise[i][j] = (1.0 + pnoise3(float(i)/big_number, float(j)/big_number, _r, octaves,persistance,lacunarity,repeatx,repeaty,base)) / 2.0
			my_noise[i][j] = (1.0 + pnoise3(float(i)/big_number, float(j)/big_number, _r,octaves,persistance, lacunarity,repeatx,repeaty,base)) / 2.0
	return my_noise		
