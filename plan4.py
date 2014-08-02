# Basically...
import sys, pygame, noisey, random, blairtool
random.seed()

my_surface, surface_width, surface_height = blairtool.init_pygame()
def hotness(val):
	if val == 0: return pygame.Color(255,255,255,100)
	else: return pygame.Color(0,0,0,100)

def pixel(surface, color, pos):
	surface.fill(color, (pos, (1, 1)))

def get_cool_surface(noise):
	surf = pygame.Surface((len(noise),len(noise[0])))
	surf.convert()
	surf.convert_alpha()
	surf.set_alpha(55555)
	for i in range(0,len(noise[0])):
		for j in range(0,len(noise)):
			pixel(surf, hotness(noise[i][j]), (j,i))
	return surf

my_noise = noisey.generateWhiteNoise(surface_width, surface_height)
my_small_noise = noisey.generateWhiteNoise(4,4)
my_surface = get_cool_surface(my_noise)
asdf = get_cool_surface(my_small_noise)
asdf = pygame.transform.scale(asdf,(surface_width,surface_height))
my_surface.blit(asdf,(0,0), special_flags=pygame.BLEND_RGBA_ADD)
pygame.image.save(my_surface,blairtool.out_file_name())
