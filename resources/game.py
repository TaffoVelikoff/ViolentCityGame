import os
import time
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

# Draw remaining bullets (ammo)
def drawBullets(screen, bulletsLeft):
    for bullet in range(0, bulletsLeft):
       screen.blit(pygame.image.load(os.path.join(globals.data_dir, 'img/bullet.png')).convert_alpha(), (globals.winWidth - 32 - (bullet * 16), 16))

    if bulletsLeft == 0:
        screen.blit(pygame.image.load(os.path.join(globals.data_dir, 'img/info/reload.png')).convert_alpha(), (globals.winWidth - 240, 16))

# Draw the status bar
def drawStatusbar(screen, statusBarImage, font, fontSmall):
    # Draw status bar image
    screen.blit(statusBarImage, (12, 12))

    # Draw speed (level)
    level = str(globals.level)
    if globals.level < 10:
        level = '0' + level
    fontlevel = font.render(str(level), True, colors.white)
    screen.blit(fontlevel, (194, 29))

    # Draw kills
    fontKills = font.render(str(globals.kills), True, colors.white)
    screen.blit(fontKills, (78, 26))

    # Draw missed
    fontMissed = font.render(str(globals.missed), True, colors.white)
    screen.blit(fontMissed, (78, 63))

    # Draw score
    fontScore = fontSmall.render(str(globals.score), True, colors.white)
    screen.blit(fontScore, (74, 100))

# increment score based on level & Kills
def incrementScore():
    globals.score += globals.scorePerKill * globals.level

# Draw images for game over screen
def drawGameOver(screen, imgOhSnap, imgReplay):
    screen.blit(imgOhSnap, (12, 12))
    screen.blit(imgReplay, (globals.winWidth/2 - 190, globals.winHeight/2 - 30))

# Generate random stars
def generateStars():
    globals.stars = [
      [random.randint(0, globals.winWidth),random.randint(0, globals.winHeight)]
      for x in range(globals.maxStars)
    ]
    globals.starsLayer2 = [
      [random.randint(0, globals.winWidth),random.randint(0, globals.winHeight)]
      for x in range(globals.maxStars)
    ]

# Draw the stars
def drawStars(win, layer2 = False):
    for star in globals.stars:
        pygame.draw.line(win, colors.white, (star[0], star[1]), (star[0], star[1]))
        star[0] = star[0] - 1
        if star[0] < 0:
            star[0] = globals.winWidth
            star[1] = random.randint(0, globals.winHeight)
    if layer2 == True:
        for star in globals.starsLayer2:
            pygame.draw.line(win, colors.white, (star[0], star[1]), (star[0], star[1]))
            star[0] = star[0] - 2
            if star[0] < 0:
                star[0] = globals.winWidth
                star[1] = random.randint(0, globals.winHeight)

# Draw the status bar
def drawMainMenu(screen, font):
    fontKills = font.render('PRESS SPACE TO START', True, colors.white)
    textRect = fontKills.get_rect(center=(globals.winWidth/2, globals.winHeight/2 - 60))
    screen.blit(fontKills, textRect)

# Show score for current kileld enemy
def drawEnemyScore(screen, font, score, x, y, creationTime):
    font = font.render('+' + str(score) + ' pts.', True, colors.white)
    textRect = font.get_rect(center=(x + 100, y + 100 - globals.enemyScorePos))
    screen.blit(font, textRect)

# Clear scores and stuff
def clear():
    globals.kills = 0
    globals.score = 0
    globals.shots = 0
    globals.missed = 0 
    globals.level = 1
    globals.roomInit = False