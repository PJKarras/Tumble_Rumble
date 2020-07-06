import pygame
from Player import Player

'''
DISCLAIMER:
    main.py is a test file, used to test the Player class
    it is not intended to be used in the game, but only for testing purposes
    you have been warned!!!
'''

# initialize pygame
pygame.init()

# create the screen
resolution = (800, 600)
screen = pygame.display.set_mode(resolution)

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

xMax = resolution[0]
yMax = resolution[1]
spawnPos = ((xMax * 0.6), (yMax * 0.7))

# initialize test player and helping attributes
player = Player(playerImg, cannonImg, spawnPos[0], spawnPos[1], screen)
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
                player_dx = 0.06
        if event.type == pygame.KEYUP:
            event_key = None
            player_dx = 0

    # RGB value fill
    screen.fill((26, 127, 200))

    # add player to screen
    player.Change_Pos(player_dx, event_key)

    # to update screen, use pygame.display.update()
    pygame.display.update()

pygame.quit()
exit()
