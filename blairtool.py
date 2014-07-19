def out_file_name():
	import inspect
	# this is gonna work on my machine only
	return "out/" + inspect.stack()[-1][1].replace('./', "").replace(".\\", "").replace(".py",".png")

def init_pygame():
	import pygame, sys
	pygame.init()
	surface_size= surface_width, surface_height = int(sys.argv[1]),int(sys.argv[2])
	size = width, height = 320,320 
	black = 0, 0, 0
	screen = pygame.display.set_mode(size)
	my_surface = pygame.Surface(surface_size)
	screen.fill(black)
	pygame.display.flip()
	return my_surface, surface_width, surface_height


