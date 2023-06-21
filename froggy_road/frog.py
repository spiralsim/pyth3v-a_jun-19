import pygame

class Frog(pygame.sprite.Sprite):
	STARTING_POSITION = (300, 490)
	SIZE = (20, 10)

	IMAGE = pygame.image.load('resources/frog.png')

	def __init__(self):
		super().__init__()
		self.image = Frog.IMAGE

		self.rect = pygame.Rect((0, 0), Frog.SIZE)
		self.rect.center = Frog.STARTING_POSITION