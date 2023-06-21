import pygame, sys
from frog import Frog
from bus import Bus
from log import Log

pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])

# Style note: Use uppercase letters and underscores for constants
SCREEN_DIM = WIDTH, HEIGHT = 600, 500 # Tuples and unpacking
SCREEN = pygame.display.set_mode(SCREEN_DIM)

pygame.display.set_caption('Frog Road!')

CLOCK = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
GREEN = (28, 128, 28)
YELLOW = (100, 85, 0)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (0, 0, 175)

frog = Frog()
bus = Bus(Bus.STARTING_POSITION, 'Left')
log = Log(Log.STARTING_POSITION, 'Right')

while True:
	CLOCK.tick(FPS)
	
	SCREEN.fill(BLACK)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:  # W
				# Add the correct frog movement function here
				frog.move_up()
			if event.key == pygame.K_a:  # A
				# Add the correct frog movement function here
				frog.move_left()
			if event.key == pygame.K_s:  # S
				# Add the correct frog movement function here
				frog.move_down()
			if event.key == pygame.K_d:  # D
				# Add the correct frog movement function here
				frog.move_right()
	
	bus.move()
	log.move()

	SCREEN.blit(frog.image, frog.rect)
	SCREEN.blit(bus.image, bus.rect)
	SCREEN.blit(log.image, log.rect)

	pygame.display.flip()

pygame.quit()

# Tuples example
'''
x, y = 3, 5
print(x)
print(y)
(a, b) = (4, 8)
print(a)
print(b)
'''
