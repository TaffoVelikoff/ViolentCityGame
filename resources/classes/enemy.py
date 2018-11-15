import os
import pygame
import random
import globals
from os import listdir
from resources import game
from os.path import isfile, join
from resources.scripts import colors

class Enemy(pygame.sprite.Sprite):
	selectedPos = 'left'
	speed = 0
	spriteWidth = 200

	# Constructor
	def __init__(self):

		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Enemy image
		self.image = pygame.image.load(os.path.join(globals.data_dir, 'img/enemy/01.png')).convert_alpha()
		self.rect = self.image.get_rect()

		# Speed
		if globals.debug == False:
			self.speed = 5 + globals.level
		else:
			globals.speed = 0

		# Create mask
		self.mask = pygame.mask.from_surface(self.image)

		'''
			The enemy can appear at 4 different places on the screen
			and start moving in 4 different possitions
		'''

		# Position to place
		positions = ('left', 'right', 'up', 'down')
		self.selectedPos = random.choice(positions)

		# Place sprite on screen (based on the randomly selected position)
		if self.selectedPos == 'left':
			self.rect.center = (self.spriteWidth/2, random.randint(self.spriteWidth/2, globals.winHeight - self.spriteWidth/2))
		elif self.selectedPos == 'right':
			self.rect.center = (globals.winWidth - self.spriteWidth/2, random.randint(self.spriteWidth/2, globals.winHeight - self.spriteWidth))
		elif self.selectedPos == 'up':
			self.rect.center = (random.randint(self.spriteWidth/2, globals.winWidth - self.spriteWidth/2), self.spriteWidth/2)
		else:
			self.rect.center = (random.randint(self.spriteWidth/2, globals.winWidth - self.spriteWidth/2), globals.winHeight - self.spriteWidth/2)

	def update(self):
		self.image.set_colorkey((0, 0, 0))
		if self.selectedPos == 'left':
			self.rect.x += self.speed
		elif self.selectedPos == 'right':
			self.rect.x -= self.speed
		elif self.selectedPos == 'up':
			self.rect.y += self.speed
		else:
			self.rect.y -= self.speed

class Blood(pygame.sprite.Sprite):
	frames = []

	# Constructor
	def __init__(self, x = None, y = None):
		# Counter
		self.steps = 0

		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Get all frames
		path = "data/img/enemy/explode/"
		frames = [f for f in listdir(path) if isfile(join(path, f))]

		# Put all frames in a list of Pygame images
		self.images = []
		for frame in frames:
			self.images.append(pygame.image.load(path + frame).convert_alpha())

		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()

		# Position
		mousePos = pygame.mouse.get_pos()
		self.rect.x = mousePos[0] - 79
		self.rect.y = mousePos[1] - 115

	def update(self):
		# ANIMATE AND KILL AFTER ANIMATION
		if self.index >= len(self.images):
			self.kill()
		else:
			self.image = self.images[self.index]

		# This will slow down animation
		if self.steps % 2 == 0:
			self.index += 1

		self.steps += 1