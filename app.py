import os
import sys
import time
import pygame
import random
import globals
from resources import game
from resources.classes import enemy
from resources.classes import weapons
from resources.scripts import colors

# Commented code bellow detects screen resolutin
# on windows. Might be usful in near future
#import ctypes
#user32 = ctypes.windll.user32
#width & hight - user32.GetSystemMetrics(0) & user32.GetSystemMetrics(1)

# Init pygame
pygame.init()
pygame.font.init()

# Load fonts
font = pygame.font.Font(os.path.join(globals.data_dir, 'fonts/LeelawUI.ttf'), 16)
fontSmall = pygame.font.Font(os.path.join(globals.data_dir, 'fonts/LeelUIsl.ttf'), 14)

# Game window
globals.winWidth = 1366
globals.winHeight = 768
fullscreen = True
FPS = 60
winBackground = colors.black
win = game.window(globals.winWidth, globals.winHeight, pygame.FULLSCREEN, winBackground, "Silent City")

# Sprites
sprites = pygame.sprite.Group()
topSprites = pygame.sprite.Group()

# Crosshair & Guns
cursor = weapons.Crosshair()
topSprites.add(cursor)
gun = weapons.Gun()
topSprites.add(gun)
gunOffsetY = 0

# Enemy
foe = enemy.Enemy()
sprites.add(foe)

# Shooting
isShooting = False
shotOnce = False

# Reloading
isReloading = False

# Load sounds
sndDie = (
    game.loadSound('snd/ah.wav'), 
    game.loadSound('snd/ah2.wav'), 
    game.loadSound('snd/ah3.wav')
)
sndShot = game.loadSound('snd/shot.wav')
sndShot.set_volume(0.5)
sndEmpty = game.loadSound('snd/empty.wav')
sndShot.set_volume(0.5)
sndReload = game.loadSound('snd/reload.wav')
sndGameOver = game.loadSound('snd/game_over.wav')
sndRebirth = game.loadSound('snd/rebirth.wav')
sndRebirth.set_volume(0.6)

# Load spriotes background
bg = game.loadBackground()
statusBarImage = pygame.image.load(os.path.join(globals.data_dir, 'img/status_bar.png'))
imgOhSnap = pygame.image.load(os.path.join(globals.data_dir, 'img/oh_snap.png'))
imgReplay = pygame.image.load(os.path.join(globals.data_dir, 'img/replay.png'))

# Clock
clock = pygame.time.Clock()

# Hide cursor
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

# Starting room
room = 'main'

# Load and play music
musicMain = game.loadMusic('snd/music.mp3')
musicMain.play(-1)
pygame.mixer.music.set_volume(0.7)

# Sleep for a while so the first enemy 
# doesn't reach the end of the screen
time.sleep(1.5)

# App running
run = True

# Game loop
while run:

    # Handle events
    for event in pygame.event.get():

        # Quit game
        if event.type == pygame.QUIT: run = False

        # KEY EVENTS
        if event.type == pygame.KEYDOWN:

            # ESC
            if event.key == pygame.K_ESCAPE:
                run = False
                room = 'quit'

            # Full screen
            if event.key == pygame.K_F4:
                if not fullscreen:
                    pygame.display.set_mode((globals.winWidth, globals.winHeight), pygame.FULLSCREEN)
                    fullscreen = True
                else:
                    pygame.display.set_mode((globals.winWidth, globals.winHeight))
                    fullscreen = False

            # Replay game
            if room == 'game_over':
                if event.key == pygame.K_SPACE:
                    # Clear all score and stuff
                    game.clear()
                    # Play sound
                    sndRebirth.play()
                    # Restart bullets
                    gun.bulletsLeft = globals.gunMaxBullets
                    # Create an enemy
                    foe = enemy.Enemy()
                    sprites.add(foe)
                    # Switch rooms
                    room = 'main'

    # Mouse position and button clicking.
    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

    # Main Room
    if room == 'main':
        # Shooting
        if pressed1 and isShooting == False:
            if gun.bulletsLeft > 0:
                # Play shot sound
                sndShot.play()

                # Display gun shot
                gunShot = weapons.Gunshot()
                sprites.add(gunShot)

                # Increment shots
                globals.shots += 1
                gun.bulletsLeft -= 1
            else:
                sndEmpty.play()

        # Check if the rect collided with the mouse pos
        # and if the left mouse button was pressed.
        if pygame.sprite.collide_mask(foe, cursor) and pressed1 and gun.bulletsLeft > 0:
            if isShooting == False:
                # Remove enemy
                foe.kill()
                # Play die sound
                random.choice(sndDie).play()
                blood = enemy.Blood()
                sprites.add(blood)
                # Make a new one
                foe = enemy.Enemy()
                sprites.add(foe)
                # Add score & kills
                globals.kills += 1
                # Check if we should raise a level
                if globals.kills % globals.nextLevelKills == 0:
                    globals.level += 1
                game.incrementScore()

        # Check if player is shooting
        if pressed1:
            isShooting = True

            # Animate gun position
            if shotOnce == False:
                if gun.rect.y < globals.winHeight - 148:
                    gun.rect.y += 3
                    if gun.rect.y == globals.winHeight - 148:
                        shotOnce = True
            if shotOnce == True and gun.rect.y > globals.winHeight - 160:
                gun.rect.y -= 3
        else:
            isShooting = False

            # Restore original gun position
            if gun.rect.y > globals.winHeight - 160:
                gun.rect.y -= 3
            shotOnce = False

        if pressed3 and gun.bulletsLeft == 0 and isReloading == False:
            sndReload.play()
            gun.bulletsLeft = 10

        if pressed3:
            isReloading = True
        else:
            isReloading = False

        # Check if enemy is out of boundry (screen)
        if(foe.rect.x > globals.winWidth or foe.rect.y > globals.winHeight or foe.rect.x < 1-foe.spriteWidth or foe.rect.y < 1-foe.spriteWidth):
            # Remove enemy
            foe.kill()
            # Make a new one
            foe = enemy.Enemy()
            sprites.add(foe)
            # Increment missed
            globals.missed += 1
            # Game over if missed too much
            if globals.missed == globals.maxMissed:
                room = 'game_over'

        # Limit frame rate
        clock.tick(FPS)

        # Render screen
        win.blit(bg, (0, 0))
        sprites.update()
        sprites.draw(win)
        topSprites.update()
        game.drawBullets(win, gun.bulletsLeft)
        game.drawStatusbar(win, statusBarImage, font, fontSmall)
        topSprites.draw(win)
        pygame.display.update()

    # Game over screen
    if room == 'game_over':
        if globals.roomInit == False:
            # Play sound
            foe.kill()
            sndGameOver.play()
            globals.roomInit = True

        win.blit(bg, (0, 0))
        game.drawGameOver(win, imgOhSnap, imgReplay)
        pygame.display.update()

# Exiting game
quit()
