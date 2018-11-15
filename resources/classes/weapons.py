import os
import pygame
import globals
from os import listdir
from os.path import isfile, join

class Crosshair(pygame.sprite.Sprite):

	# Constructor
	def __init__(self, xOffset = 16, yOffset = 16):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(globals.data_dir, 'img/crosshair.png'))
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.center = (16, 16)
		self.xOffset = xOffset
		self.yOffset = yOffset

	def update(self):
		mousePos = pygame.mouse.get_pos()
		self.rect.x = mousePos[0] - self.xOffset
		self.rect.y = mousePos[1] - self.yOffset
    		
class Gun(pygame.sprite.Sprite):
	bulletsLeft = 0

	# Constructor
	def __init__(self):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)
		self.bulletsLeft = globals.gunMaxBullets
		self.image = pygame.image.load(os.path.join(globals.data_dir, 'img/gun.png'))
		self.rect = self.image.get_rect()
		self.rect.center = (229, 181)
		self.rect.y = globals.winHeight-160

	def update(self):
		mousePos = pygame.mouse.get_pos()
		self.rect.x = mousePos[0]+64
    		
class Gunshot(pygame.sprite.Sprite):
	frames = []
	frameRepeat = 3
	steps = 0

	# Constructor
	def __init__(self):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Get all frames
		path = "data/img/gunshot/"
		frames = [f for f in listdir(path) if isfile(join(path, f))]

		# Put all frames in a list of Pygame images
		self.images = []
		for frame in frames:
			self.images.append(pygame.image.load(path + frame))

		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()

		# Position
		mousePos = pygame.mouse.get_pos()
		self.rect.x = mousePos[0]+20
		self.rect.y = globals.winHeight-212

	def update(self):
		if self.index >= len(self.images):
			self.kill()
		else:
			self.image = self.images[self.index]
			self.image.set_colorkey((0, 0, 0))
			mousePos = pygame.mouse.get_pos()
			self.rect.x = mousePos[0]+20

			# This will make sure that we repeat frames
			# so animation looks a bit slower
			if self.steps % self.frameRepeat == 0:
				self.index += 1
			self.steps += 1