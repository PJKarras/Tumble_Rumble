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
    test.py is a test file, used to test the Player class
    it is not intended to be used in the game, but only for testing purposes
    you have been warned!!!
'''
import game_ui

# initialize pygame
#pygame.init()

# create the screen
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
#screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# make some colors
WHITE = (250, 250, 250)
GREEN = (0, 110, 0)
SKYBLUE = (100, 190, 255)

#screen.fill(SKYBLUE)


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


# start game
def start(screen):
    # Old terrain init
    #numpyPixel, surf = get_random_pix_map(screen, DISPLAY_WIDTH, DISPLAY_HEIGHT, 400)
    numpyPixel, colorNumpyArray = get_random_pix_map(screen, DISPLAY_WIDTH, DISPLAY_HEIGHT, 400)
    pygame.draw.circle(screen, WHITE, [80, 80], 80, 0)

    # initialize test player and helping attributes
    player = Player(playerImg, cannonImg, 1, screen, numpyPixel)
    player_dx = 0
    event_key = None

    # game loop
    weapon_menu_open = False
    item_menu_open = False
    movement_on = False
    running = True
    while running:
        if weapon_menu_open:
            game_ui.weapons_holder.draw(screen)
        if item_menu_open:
            game_ui.items_holder.draw(screen)
        if movement_on:
            game_ui.move_on_button.draw(screen)
        else:
            game_ui.move_off_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if movement_on:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        event_key = event.key
                        player_dx = 0.24
                if event.type == pygame.KEYUP:
                    event_key = None
                    player_dx = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if game_ui.leave_button.rect.collidepoint(pos):
                        return
                    if game_ui.move_off_button.rect.collidepoint(pos) or game_ui.move_on_button.rect.collidepoint(pos):
                        movement_on = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if game_ui.leave_button.rect.collidepoint(pos):
                        return
                    if game_ui.weapon_button.rect.collidepoint(pos):
                        if weapon_menu_open:
                            weapon_menu_open = False
                        else:
                            weapon_menu_open = True
                    if game_ui.items_button.rect.collidepoint(pos):
                        if item_menu_open:
                            item_menu_open = False
                        else:
                            item_menu_open = True
                    if game_ui.move_off_button.rect.collidepoint(pos) or game_ui.move_on_button.rect.collidepoint(pos):
                        movement_on = True

        # add player to screen
        player.Change_Pos(player_dx, event_key)
        # to update screen, use pygame.display.update()
        for i in game_ui.button_list:
            i.update(pygame.mouse.get_pos())
            i.draw(screen)
        pygame.display.update()

        # Old blit
        #screen.fill(SKYBLUE)
        #screen.blit(surf, (0, 0))
        terrainSurface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.surfarray.blit_array(terrainSurface, colorNumpyArray)
