import random
import math

random.seed(0)

# range is [0,1] , either 0 or 1
def generateWhiteNoise(width,height):
	noise = [[r for r in range(width)] for i in range(height)]

	for i in range(0,height):
		for j in range(0,width):
			noise[i][j] = random.randint(0,1)

	return noise

# range is [0.1]
def generateWhiteNoiseNumpy(width,height,loc=0.5,sd=0.5):
	import numpy
	noise = numpy.random.normal(loc,sd,(height,width))
	for (x,y), value in numpy.ndenumerate(noise):
		if noise[x,y] < 0: noise[x,y] = 0
		if noise[x,y] > 1: noise[x,y] = 1

	return noise
