# NUMPY We just want to compare the two white noise functions
import sys, pygame, noisey, random, blairtool

pygame.init()
surface_size= surface_width, surface_height = int(sys.argv[1]),int(sys.argv[2])
size = width, height = 320,320 
black = 0, 0, 0

screen = pygame.display.set_mode(size)
my_surface = pygame.Surface(surface_size)

def rando():
	return int(random.uniform(1,255))

def noisyColor(n):
	return pygame.Color(rando()*n,rando()*n,rando()*n,1)

def pixel(surface, color, pos):
	surface.fill(color, (pos, (1, 1)))


screen.fill(black)
pygame.display.flip()
my_surface.blit(screen, (0,0))

my_noise = noisey.generateWhiteNoiseNumpy(surface_width, surface_height)
for i in range(0,surface_height):
	for j in range(0,surface_width):
		pixel(my_surface, noisyColor(my_noise[i][j]), (i,j))
pygame.image.save(my_surface,blairtool.out_file_name())
