from Player import Player
from flatSlope import destroy_terrain_circle
from projectile import Projectile
import os, sys
import pygame
import numpy
from items import shield, bomb, wrench, jetPack
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
import menu_gui
from menu_gui import UIElement, right_arrow, left_arrow, right_arrowX, right_arrowY, left_arrowX

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
BLUE = (106, 150, 181)

#screen.fill(SKYBLUE)


# title and icon
pygame.display.set_caption("Tumble Rumble")
icon = pygame.image.load("assets/tanks/tank_red.png")
pygame.display.set_icon(icon)

# Player
playerRawImg = pygame.image.load("assets/tanks/tank_red.png")
newSize = (int(playerRawImg.get_width() * 0.25), int(playerRawImg.get_height() * 0.25))
playerImg = pygame.transform.scale(playerRawImg, newSize)
player2Img = pygame.transform.scale(pygame.image.load("assets/tanks/tank_blue.png"), newSize)
player3Img = pygame.transform.scale(pygame.image.load("assets/tanks/tank_green.png"), newSize)
player4Img = pygame.transform.scale(pygame.image.load("assets/tanks/tank_black.png"), newSize)
player5Img = pygame.transform.scale(pygame.image.load("assets/tanks/tank_pink.png"), newSize)

# Cannon
cannonRawImg = pygame.image.load("assets/cannons/cannon_red.png")
newSize = (int(cannonRawImg.get_width() * 0.25), int(cannonRawImg.get_height() * 0.25))
cannonImg = pygame.transform.scale(cannonRawImg, newSize)
cannon2Img = pygame.transform.scale(pygame.image.load("assets/cannons/cannon_blue.png"), newSize)
cannon3Img = pygame.transform.scale(pygame.image.load("assets/cannons/cannon_green.png"), newSize)
cannon4Img = pygame.transform.scale(pygame.image.load("assets/cannons/cannon_black.png"), newSize)
cannon5Img = pygame.transform.scale(pygame.image.load("assets/cannons/cannon_pink.png"), newSize)

xMax = DISPLAY_WIDTH
yMax = DISPLAY_HEIGHT
spawnPos = ((xMax * 0.6), (yMax * 0.7))


def optionsMenu(screen):

    optionTitle = UIElement(
        center_position=(DISPLAY_WIDTH/2, DISPLAY_HEIGHT*.125),
        font_size=60,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Options'
    )

    returnButton = UIElement(
        center_position=(DISPLAY_WIDTH*.25, DISPLAY_HEIGHT*.92),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Return to Main Menu'
    )
    done = False
    while not done:
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if returnButton.rect.collidepoint(pos):
                    done = True

        optionTitle.draw(screen)
        returnButton.update(pygame.mouse.get_pos())
        returnButton.draw(screen)
        pygame.display.flip()


def startMenu(screen):
    # player count
    playerCount = 1

    how_many_title = UIElement(
        center_position=(DISPLAY_WIDTH/2, DISPLAY_HEIGHT*.125),
        font_size=55,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='How many players?'
    )

    startButton = UIElement(
        center_position=(DISPLAY_WIDTH/2, DISPLAY_HEIGHT*.75),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Start'
    )

    returnButton = UIElement(
        center_position=(DISPLAY_WIDTH*.25, DISPLAY_HEIGHT*.92),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Return to Main Menu'
    )

    done = False
    while not done:
        playerCount_icon = UIElement(
            center_position=(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .33),
            font_size=50,
            bg_rgb=BLUE,
            text_rgb=WHITE,
            text=str(playerCount)
        )

        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if startButton.rect.collidepoint(pos):
                    startGame(screen, playerCount)
                    return
                if game_ui.left_arrow_button.rect.collidepoint(pos):
                    if playerCount == 1:
                        pass
                    else:
                        playerCount -= 1
                if game_ui.right_arrow_button.rect.collidepoint(pos):
                    if playerCount == 4:
                        pass
                    else:
                        playerCount += 1
                if returnButton.rect.collidepoint(pos):
                    done = True

        how_many_title.draw(screen)
        game_ui.right_arrow_button.draw(screen)
        game_ui.left_arrow_button.draw(screen)
        playerCount_icon.draw(screen)
        startButton.update(pygame.mouse.get_pos())
        startButton.draw(screen)
        returnButton.update(pygame.mouse.get_pos())
        returnButton.draw(screen)
        pygame.display.flip()


def startGame(screen, how_many_players):
    start(screen, how_many_players)


def main():
    pygame.init()

    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    gameTitle = UIElement(
        center_position=(DISPLAY_WIDTH/2, DISPLAY_HEIGHT*.125),
        font_size=60,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Tumble Rumble'
    )

    startGame = UIElement(
        center_position=(DISPLAY_WIDTH/2, DISPLAY_HEIGHT*.292),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Start Game'
    )

    optionButton = UIElement(
        center_position=(DISPLAY_WIDTH/2, DISPLAY_HEIGHT*.375),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Options'
    )

    exitGame = UIElement(
        center_position=(DISPLAY_WIDTH/2, DISPLAY_HEIGHT*.458),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Exit Game'
    )
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if exitGame.rect.collidepoint(pos):
                    done = True
                if startGame.rect.collidepoint(pos):
                    startMenu(screen)
                if optionButton.rect.collidepoint(pos):
                    optionsMenu(screen)
        screen.fill(BLUE)

        gameTitle.draw(screen)
        startGame.update(pygame.mouse.get_pos())
        startGame.draw(screen)
        optionButton.update(pygame.mouse.get_pos())
        optionButton.draw(screen)
        exitGame.update(pygame.mouse.get_pos())
        exitGame.draw(screen)
        pygame.display.flip()


# start game
def start(screen, how_many_players):

    fuel_text = UIElement(
        center_position=(DISPLAY_WIDTH * .265, DISPLAY_WIDTH * .01),
        font_size=20,
        bg_rgb=SKYBLUE,
        text_rgb=WHITE,
        text="Fuel"
    )

    numpyPixel, colorNumpyArray = get_random_pix_map(screen, DISPLAY_WIDTH, DISPLAY_HEIGHT, 400)
    pygame.draw.circle(screen, WHITE, [80, 80], 80, 0)

    # initialize test player and helping attributes
    playerList = []
    for i in range(how_many_players):
        if i == 0:
            playerList.append(Player(playerImg, cannonImg, i+1, screen, numpyPixel))
        elif i == 1:
            playerList.append(Player(player2Img, cannon2Img, i+1, screen, numpyPixel))
        elif i == 2:
            playerList.append(Player(player3Img, cannon3Img, i+1, screen, numpyPixel))
        elif i == 3:
            playerList.append(Player(player4Img, cannon4Img, i+1, screen, numpyPixel))
        elif i == 4:
            playerList.append(Player(player5Img, cannon5Img, i+1, screen, numpyPixel))
        else:
            playerList.append(Player(playerImg, cannonImg, i+1, screen, numpyPixel))
    player_dx = 0
    event_key = None

    # test list of items
    newWrench = wrench(int(0.25 * screen.get_width()), screen, numpyPixel)
    newShield = shield(int(0.3 * screen.get_width()), screen, numpyPixel)

    itemsRendered = []
    itemsRendered.append(newShield)
    itemsRendered.append(newWrench)

    # game loop
    weapon_menu_open = False
    item_menu_open = False
    movement_on = False
    running = True
    currentPlayer = 0
    playerName = "Player " + str(currentPlayer+1)
    aim_selected = True
    weapon_selection = None
    while running:

        player_turn = UIElement(
            center_position=(DISPLAY_WIDTH * .70, DISPLAY_WIDTH * .015),
            font_size=20,
            bg_rgb=SKYBLUE,
            text_rgb=WHITE,
            text="Turn: " + playerName
        )

        for i in range(0, len(playerList)):
            if playerList[i].getHealth() <= 0:
                playerList[i].pop()

        if weapon_menu_open:
            game_ui.weapons_holder.draw(screen)
            for i in game_ui.weapons_list:
                i.update(pygame.mouse.get_pos())
                i.draw(screen)
        if item_menu_open:
            game_ui.items_holder.draw(screen)
            for i in playerList[currentPlayer].getItems():
                #i.update(pygame.mouse.get_pos())
                #i.draw(screen)
                if i.itemName() == "wrench":
                    game_ui.item_list[0].update(pygame.mouse.get_pos())
                    game_ui.item_list[0].draw(screen)
                if i.itemName() == "shield":
                    game_ui.item_list[1].update(pygame.mouse.get_pos())
                    game_ui.item_list[1].draw(screen)
                if i.itemName() == "jetPack":
                    game_ui.item_list[2].update(pygame.mouse.get_pos())
                    game_ui.item_list[2].draw(screen)
        if movement_on:
            game_ui.move_on_button.draw(screen)
        else:
            game_ui.move_off_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if movement_on:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_h:
                        event_key = event.key
                        player_dx = 0.24
                        stopMovement = playerList[currentPlayer].isFuelEmpty()
                        if stopMovement:
                            player_dx = 0
                        playerList[currentPlayer].Change_Pos(True, player_dx, event_key)
                elif event.type == pygame.KEYUP:
                    event_key = None
                    player_dx = 0
                    playerList[currentPlayer].Change_Pos(True, player_dx, event_key)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.set_visible(True)
                    pos = pygame.mouse.get_pos()
                    if game_ui.leave_button.rect.collidepoint(pos):
                        return
                    if game_ui.move_off_button.rect.collidepoint(pos) or game_ui.move_on_button.rect.collidepoint(pos):
                        movement_on = False
                    if aim_selected:
                        if game_ui.aim_button.rect.collidepoint(pos):
                            pygame.mouse.set_visible(False)
                            aim_selected = False
                    else:
                        if game_ui.fire_button.rect.collidepoint(pos):
                            aim_selected = True
                            playerList[currentPlayer].fuelAmount = 5
                            if currentPlayer == how_many_players - 1:
                                currentPlayer = 0
                            else:
                                currentPlayer += 1
                            playerName = "Player " + str(currentPlayer + 1)
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.set_visible(True)
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
                    if game_ui.weapons_holder.rect.collidepoint(pos):
                        for weapon in game_ui.weapons_list:
                            if weapon.rect.collidepoint(pos):
                                weapon_selection = weapon
                    if aim_selected:
                        if game_ui.aim_button.rect.collidepoint(pos):
                            pygame.mouse.set_visible(False)
                            aim_selected = False
                    else:
                        if game_ui.fire_button.rect.collidepoint(pos):
                            aim_selected = True
                            coll_flag, coord_coll = playerList[currentPlayer].projectile.animate_proj(
                                last_pos[0], last_pos[1],
                                playerList[currentPlayer].xpos_cannon, 
                                playerList[currentPlayer].ypos_cannon,
                                numpyPixel)
                            # If there was a collision, destroy terrain and damage tank
                            if coll_flag:
                                numpyPixel, colorNumpyArray = destroy_terrain_circle(coord_coll,1000,numpyPixel, colorNumpyArray)
                                pygame.display.update()
                                for player in playerList:
                                    if(abs(player.true_xpos-coord_coll[0]) < 25 and
                                        abs(player.true_ypos-coord_coll[1]) < 25):
                                        # hit player
                                        print("HIT PLAYER")
                                        if player.shieldEquipped():
                                            player.removeShield()
                                        else:
                                            player.hit()

                            playerList[currentPlayer].fuelAmount = 5
                            if currentPlayer == how_many_players-1:
                                currentPlayer = 0
                            else:
                                currentPlayer += 1
                            playerName = "Player " + str(currentPlayer + 1)
        if item_menu_open:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if game_ui.item_list[0].rect.collidepoint(pos):
                    playerList[currentPlayer].repair()
                    for i in range(0, len(playerList[currentPlayer].getItems())):
                        if playerList[currentPlayer].getItems()[i].itemName() == "wrench":
                            playerList[currentPlayer].removeItem(i)
                if game_ui.item_list[1].rect.collidepoint(pos):
                    playerList[currentPlayer].addShield()
                    for i in range(0, len(playerList[currentPlayer].getItems())):
                        if playerList[currentPlayer].getItems()[i].itemName() == "shield":
                            playerList[currentPlayer].removeItem(i)

        # add players to screen
        for player in playerList:
            if player == playerList[currentPlayer]:
                stopMovement = playerList[currentPlayer].isFuelEmpty()
                if stopMovement:
                    player_dx = 0
                player.Change_Pos(True, player_dx, event_key)
            else:
                player.Change_Pos(False, 0, event_key)

        # add items to screen
        for i in range(0, len(itemsRendered)):
            itemsRendered[i].update()
            if abs(itemsRendered[i].getXPos() - playerList[currentPlayer].getXPos()) < 25:
                if len(playerList[currentPlayer].getItems()) < 4:
                    playerList[currentPlayer].addItem(itemsRendered.pop(i))

        # to update screen, use pygame.display.update()
        for i in game_ui.button_list:
            i.update(pygame.mouse.get_pos())
            i.draw(screen)
        if aim_selected:
            game_ui.aim_button.update(pygame.mouse.get_pos())
            game_ui.aim_button.draw(screen)
        else:
            game_ui.fire_button.update(pygame.mouse.get_pos())
            game_ui.fire_button.draw(screen)
            isVisible = pygame.mouse.get_visible()
            if not isVisible:
                screen.blit(game_ui.reticle, (pygame.mouse.get_pos()))
                last_pos = pygame.mouse.get_pos()
            screen.blit(game_ui.reticle, last_pos)
        fuel_text.draw(screen)
        player_turn.draw(screen)
        pygame.display.update()
        terrainSurface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.surfarray.blit_array(terrainSurface, colorNumpyArray)


main()
