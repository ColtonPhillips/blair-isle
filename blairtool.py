import pygame, random

def off_or_on_color(val):
	if val == 0: return pygame.Color(255,255,255,255)
	else: return pygame.Color(0,0,0,255)

def random_rgba_val():
	return int(random.uniform(0,255))

def random_color():
	return pygame.Color(random_rgba_val(),random_rgba_val(),random_rgba_val(),255)

def out_file_name():
	import inspect
	# this is gonna work on my machine only
	return "out/" + inspect.stack()[-1][1].replace('./', "").replace(".\\", "").replace(".py",".png")

def init_pygame():
	import sys
#	random.seed()
	pygame.init()
	surface_size= surface_width, surface_height = int(sys.argv[1]),int(sys.argv[2])
	size = width, height = 320,320 
	black = 0, 0, 0
	screen = pygame.display.set_mode(size)
	my_surface = pygame.Surface(surface_size)
	screen.fill(black)
	pygame.display.flip()
	
	return my_surface, surface_width, surface_height


