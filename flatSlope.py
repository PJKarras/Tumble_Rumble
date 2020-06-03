import os, sys
import pygame
import numpy
from pygame.locals import *

def get_slope_pix_map(displayW, displayH, stepSize, minH, maxH, color, direction):
    """ Draws a sloped map to pygame screen and returns a numpy 2Darray that acts
    as a pixel map for collision detection where 0's represent air, and 1's 
    represent ground. This matrix directly corresponds to the drawn terrain on 
    screen.
    displayW: The variable representing display width i.e. 1920 in 1920x1080
    displayH: The variable representing display height i.e. 1080 in 1920x1080
    stepSize: How many pixels each column of terrain changes by 
    minH: The minimum height of terrain (little buggy)
    maxH: The max height of terrain
    color: The color of drawn terrain
    direction: "/", "up", or "r" for upwards slope, "\\", "down", or "l" for down  
    """

    # Creation of 2d pixel matrix, will store 1's for ground, 0 for sky
    pixelMatrix = numpy.zeros((displayH, displayW))

    # Declare surface for terrain (used to draw terrain on window)
    surf = pygame.Surface((displayW,displayH))
    surf = surf.convert_alpha()
    transperantFill = (0, 0, 255, 0)
    surf.fill(transperantFill)

    # Declare pixel array, to be used to tell pygame where to fill with color
    par = pygame.PixelArray(surf)

    # Pixel  representation of the bottom of window (addresses start at 0)
    bottomOfWindow = displayH

    # currentHeight here actually represents the raw y coordinate of the height,
    # so while currentHeight might be equal to 490, it acutally represents a 
    # height of 10, will fix in future, this is also the reason beside the 
    # seemingly weird step behavior
    if direction == "/" or direction == "up" or direction == "r":
        # Declare variables to be used within loop
        currentHeight = displayH - minH
        # Run loop to fill pixel array
        print("my currentHeight: ", currentHeight)
        print("my stepSize: ", stepSize)
        print("my maxH: ", maxH)
        for x in range(displayW):
            # Set Color of PixelArray
            par[x,currentHeight:bottomOfWindow] = color
            # Set 1 values for pixel matrix
            for index in range(displayH-1, currentHeight, -1):
                 pixelMatrix[index][x] = 1
            if displayH - (currentHeight + stepSize) <= maxH:
                currentHeight -= stepSize
    elif direction == "\\" or direction == "down" or direction == "l":
        # Declare variables to be used within loop
        currentHeight = displayH - maxH
        # Run loop to fill pixel array
        for x in range(displayW):
            # Set Color of PixelArray
            par[x,currentHeight:bottomOfWindow] = color
            # Set 1 values for pixel matrix
            for index in range(displayH-1, currentHeight, -1):
                 pixelMatrix[index][x] = 1
            if displayH - (currentHeight - stepSize) > minH:
                currentHeight += stepSize
    # Close and locks PixelArray and then draws it to screen
    par.close()
    DISPLAYSURF.blit(surf, (0,0))
    return pixelMatrix

def collide_terrain(rectangle, pixelMatrix):
    top = rectangle.top
    right = rectangle.right
    bottom = rectangle.bottom
    left = rectangle.left
    # Code here to check pixel matrix with above values for a collison

if __name__ == "__main__":

    pygame.init()

    # Set up display window
    DISPLAY_WIDTH =  20
    DISPLAY_HEIGHT = 15
    DISPLAYSURF = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    # Color constants
    WHITE = (250, 250, 250)
    GREEN = (0, 110, 0)
    SKYBLUE = (100, 190, 255)

    DISPLAYSURF.fill(SKYBLUE)

    numpyPixel = get_slope_pix_map(DISPLAY_WIDTH, DISPLAY_HEIGHT, 1, 3, 10, GREEN, "\\")

    print(numpyPixel)

    # Main game loop.
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()


