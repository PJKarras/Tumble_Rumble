import pygame
from Player import Player
import os, sys
import pygame
import numpy
from gameTools import perlin
from pygame.locals import *
from flatSlope import get_random_pix_map, get_slope_pix_map, collision_circle

'''
DISCLAIMER:
    main.py is a test file, used to test the Player class
    it is not intended to be used in the game, but only for testing purposes
    you have been warned!!!
'''

# initialize pygame
pygame.init()

# create the screen
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# make some colors
WHITE = (250, 250, 250)
GREEN = (0, 110, 0)
SKYBLUE = (100, 190, 255)

screen.fill(SKYBLUE)

numpyPixel, surf = get_random_pix_map(screen, DISPLAY_WIDTH, DISPLAY_HEIGHT, 400)
pygame.draw.circle(screen, WHITE, [80, 80], 80, 0)

# title and icon
pygame.display.set_caption("Tumble Rumble")
icon = pygame.image.load("assets/tanks/tank_red.png")
pygame.display.set_icon(icon)

# Player
playerRawImg = pygame.image.load("assets/tanks/tank_red.png")
newSize = (int(playerRawImg.get_width() * 0.25), int(playerRawImg.get_height() * 0.25))
playerImg = pygame.transform.scale(playerRawImg, newSize)

# Cannon
cannonRawImg = pygame.image.load("assets/cannons/cannon_red.png")
newSize = (int(cannonRawImg.get_width() * 0.25), int(cannonRawImg.get_height() * 0.25))
cannonImg = pygame.transform.scale(cannonRawImg, newSize)

xMax = DISPLAY_WIDTH
yMax = DISPLAY_HEIGHT
spawnPos = ((xMax * 0.6), (yMax * 0.7))

# initialize test player and helping attributes
player = Player(playerImg, cannonImg, 1, screen, numpyPixel)
player_dx = 0
event_key = None

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Exiting...")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                event_key = event.key
                player_dx = 0.24
        if event.type == pygame.KEYUP:
            event_key = None
            player_dx = 0
    # add player to screen
    player.Change_Pos(player_dx, event_key)
    # to update screen, use pygame.display.update()
    pygame.display.update()
    screen.fill(SKYBLUE)
    screen.blit(surf, (0, 0))

pygame.quit()
exit()
