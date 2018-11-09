import os
import pygame
import random
import globals
from os import listdir
from os.path import isfile, join
from resources.scripts import colors

# Game window
def window(winWidth, winHeight, fullscreen, backgroundColor, caption):
    win = pygame.display.set_mode((winWidth, winHeight), fullscreen)
    win.fill(backgroundColor) # Background color

    # Window caption
    pygame.display.set_caption(caption)

    return win

# Load sound
def loadSound(fileName):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(globals.data_dir, fileName)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print ('Cannot load sound: %s' % fullname)
        raise SystemExit(str(geterror()))
    return sound

# Load music
def loadMusic(fileName):
    fullname = os.path.join(globals.data_dir, fileName)
    try:
        pygame.mixer.music.load(fullname)
    except pygame.error:
        print ('Cannot load music file: %s' % fullname)
    return pygame.mixer.music

# Load background
def loadBackground():
    # List all backgrounds
    path = "data/img/backs/"
    bgs = [f for f in listdir(path) if isfile(join(path, f))]

    # Choose a random one
    img = random.choice(bgs)

    # Load the selected and scale for resolution
    return pygame.transform.scale(pygame.image.load(path + img).convert(), (globals.winWidth, globals.winHeight))