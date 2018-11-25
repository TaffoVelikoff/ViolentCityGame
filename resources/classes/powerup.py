import os
import pygame
import random
import globals
from os import listdir
from os.path import isfile, join

class BulletPlus(pygame.sprite.Sprite):

	appeared = 0

	# Constructor
	def __init__(self):

		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Image
		self.image = pygame.image.load(os.path.join(globals.data_dir, 'img/pwrp/pwr_bullets.png')).convert_alpha()
		self.rect = self.image.get_rect()

		# Create mask
		self.mask = pygame.mask.from_surface(self.image)

		# Place on screen
		self.rect.center = (random.randint(1, globals.winWidth - 140), random.randint(100, globals.winHeight - 140))

	def kill(self):
		self.rect.center = (-300, -300)

class BulletPlusGone(pygame.sprite.Sprite):
	frames = []

	# Constructor
	def __init__(self, x, y):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Get all frames
		path = "data/img/pwrp/pwr_bullets_kill/"
		frames = [f for f in listdir(path) if isfile(join(path, f))]

		# Put all frames in a list of Pygame images
		self.images = []
		for frame in frames:
			self.images.append(pygame.image.load(path + frame).convert_alpha())

		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()

		# Position
		self.rect.x = x
		self.rect.y = y

	def update(self):
		# ANIMATE AND KILL AFTER ANIMATION
		if self.index >= len(self.images):
			self.kill()
		else:
			self.image = self.images[self.index]

		self.index += 1

class Bomb(pygame.sprite.Sprite):

	appeared = 0

	# Constructor
	def __init__(self):

		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Image
		self.image = pygame.image.load(os.path.join(globals.data_dir, 'img/pwrp/pwr_bomb.png')).convert_alpha()
		self.rect = self.image.get_rect()

		# Create mask
		self.mask = pygame.mask.from_surface(self.image)

		# Place on screen
		self.rect.center = (random.randint(1, globals.winWidth - 140), random.randint(100, globals.winHeight - 140))

	def kill(self):
		self.rect.center = (-300, -300)
		
class BombGone(pygame.sprite.Sprite):
	frames = []

	# Constructor
	def __init__(self, x, y):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Get all frames
		path = "data/img/pwrp/pwr_bomb_kill/"
		frames = [f for f in listdir(path) if isfile(join(path, f))]

		# Put all frames in a list of Pygame images
		self.images = []
		for frame in frames:
			self.images.append(pygame.image.load(path + frame).convert_alpha())

		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()

		# Position
		self.rect.x = x
		self.rect.y = y

	def update(self):
		# ANIMATE AND KILL AFTER ANIMATION
		if self.index >= len(self.images):
			self.kill()
		else:
			self.image = self.images[self.index]

		self.index += 1