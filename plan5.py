# Mumble number 5
# Look pal. I have no idea if this is even what I want, ya know?
# But Heck, it just plain looks like it's working!
import sys, pygame, noisey, random, blairtool
random.seed()

my_surface, surface_width, surface_height = blairtool.init_pygame()

def pixel(surface, color, pos):
	surface.fill(color, (pos, (1, 1)))

def get_cool_surface(noise):
	surf = pygame.Surface((len(noise),len(noise[0])))
	surf.convert()
	surf.convert_alpha()
	surf.set_alpha(40)
	for i in range(0,len(noise[0])):
		for j in range(0,len(noise)):
			if (noise[i][j] > 0.5):
				pixel(surf, blairtool.random_color(), (j,i))
	return surf


#my_noise = noisey.generatePerlinNoise(2,2)
my_noise = noisey.generatePerlinNoise(800,800)
my_surface = get_cool_surface(my_noise)
pygame.image.save(my_surface,blairtool.out_file_name())
quit()
my_surface = pygame.transform.scale(my_surface, (surface_width, surface_height))

i = 1
while (i < surface_width/2):
	my_small_noise = noisey.generatePerlinNoise(i,i)
	surf = get_cool_surface(my_small_noise)
	surf = pygame.transform.scale(surf,(surface_width,surface_height))
	my_surface.blit(surf,(0,0))
	i = i * 2

pygame.image.save(my_surface,blairtool.out_file_name())
