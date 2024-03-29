import os, sys
import pygame
import numpy
import math
from gameTools import perlin
from pygame.locals import *

# Color constants
WHITE = (250, 250, 250)
GREEN = (0, 110, 0)
SKYBLUE = (100, 190, 255)

# create the screen
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

def get_random_pix_map(DISPLAYSURF, displayW, displayH, maxHillHeight, freqOfHills=2):
    # Creation of 2d pixel matrix, will store 1's for ground, 0 for sky
    collisionNumpyArray = numpy.zeros((displayH, displayW))

    # Declare surface for terrain (used to draw terrain on window)
    surf = pygame.Surface((displayW, displayH))
    surf = surf.convert_alpha()
    transperantFill = (100, 190, 255, 0)
    surf.fill(transperantFill)

    # Declare pixel array, to be used to tell pygame where to fill with color
    par = pygame.PixelArray(surf)

    # Pixel  representation of the bottom of window (addresses start at 0)
    bottomOfWindow = displayH

    # Randomly generate heights
    # ratio of points (hills) to pixels
    ratio_hills_pixels = 3.0 / 200.0
    # frequency represents frequency of hills
    frequency = 3

    # Get perlin randomly generated values
    noise = perlin.Perlin(frequency)
    x_vals = [x for x in range(displayW)]
    y_vals = [noise.valueAt(x) for x in x_vals]

    # Normalization of random perlin values to 0-1 so we may then
    # multiply these normalized values by our max hill height to achieve smooth
    # random hills
    old_max_y = max(y_vals)
    old_min_y = min(y_vals)
    old_range = old_max_y - old_min_y
    new_max_y = 1.0
    new_min_y = 0
    new_range = new_max_y - new_min_y
    norm = lambda oldVal: (((oldVal - old_min_y) * new_range) / old_range) + new_min_y
    y_vals_norm = [norm(i) for i in y_vals]

    GREEN = (0, 110, 0)

    for x in range(displayW):
        currentHeight = int(y_vals_norm[x] * maxHillHeight)
        # with open("MyFile.txt","a") as file1:
        #     print(f"Row {x} has a height of {currentHeight}", file=file1)
        par[x, bottomOfWindow - currentHeight:bottomOfWindow] = GREEN
        # Set 1 values for pixel matrix
        for index in range(displayH - 1, displayH - 1 - currentHeight, -1):
            collisionNumpyArray[index][x] = 1
    collisionNumpyArray[719,0:]=1
    par.close()
    #DISPLAYSURF.blit(surf, (0, 0))
    colorNumpyArray = pygame.surfarray.array3d(surf)
    return collisionNumpyArray, colorNumpyArray


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
    surf = pygame.Surface((displayW, displayH))
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
        # print("my currentHeight: ", currentHeight)
        # print("my stepSize: ", stepSize)
        # print("my maxH: ", maxH)
        for x in range(displayW):
            # Set Color of PixelArray
            par[x, currentHeight:bottomOfWindow] = color
            # Set 1 values for pixel matrix
            for index in range(displayH - 1, currentHeight, -1):
                pixelMatrix[index][x] = 1
            if displayH - (currentHeight + stepSize) <= maxH:
                currentHeight -= stepSize
    elif direction == "\\" or direction == "down" or direction == "l":
        # Declare variables to be used within loop
        currentHeight = displayH - maxH
        # Run loop to fill pixel array
        for x in range(displayW):
            # Set Color of PixelArray
            par[x, currentHeight:bottomOfWindow] = color
            # Set 1 values for pixel matrix
            for index in range(displayH - 1, currentHeight, -1):
                pixelMatrix[index][x] = 1
            if displayH - (currentHeight - stepSize) > minH:
                currentHeight += stepSize
    # Close and locks PixelArray and then draws it to screen
    par.close()
    DISPLAYSURF.blit(surf, (0, 0))
    return pixelMatrix


def collision_circle(x_cord, y_cord, radius):
    # Need to calculate pixel values of circle, possibly with trig?
    top = rectangle.top
    right = rectangle.right
    bottom = rectangle.bottom
    left = rectangle.left
    # Code here to check pixel matrix with above values for a collison

# Takes in location and size of impact, and modifies pasted in arrays for the 
# terrain color and collision to display the affects of that round/projectile.
#   RETURNS: terrain_array, collision_array back in updated form 
#   Center_impact: the coordinate of the collision, tuple of format (x,y)
#   Round_size: the area of explosion area in pixels
#   Terrain_array: the color numpy array for the terrain (as gotten with
#   pygame.surfarray.array3d)
#   Collision_array: numpy array that represents 1s and 0s for collision
def destroy_terrain_circle(center_impact, round_size, collision_array, terrain_array):
    x_rem = center_impact[0]
    y_rem = center_impact[1]
    r = math.ceil( (float(round_size)/math.pi) ** 0.5)
    diameter = r*2
    for row in range(0, diameter+1):
        for col in range(0, diameter+1):
            circle_func_res = (col-r)**2 + (row-r)**2
            if circle_func_res <= r**2:
                if(x_rem+row >= DISPLAY_WIDTH or y_rem+col >= DISPLAY_HEIGHT):
                    continue
                terrain_array[x_rem+row, y_rem+col] = SKYBLUE
                collision_array[y_rem+col, x_rem+row] = 0
    return collision_array, terrain_array

if __name__ == "__main__":

    pygame.init()

    # Set up display window
    DISPLAY_WIDTH = 500
    DISPLAY_HEIGHT = 400
    DISPLAYSURF = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    DISPLAYSURF.fill(SKYBLUE)

    # First, get random pixel map
    collisionNumpyArray, colorNumpyArray = get_random_pix_map(DISPLAYSURF,DISPLAY_WIDTH, DISPLAY_HEIGHT, 300)
    
    # Secondly, simulate an impact from a tank round (due to random generation of
    # terrain and nature of this hard code the impact might not be apparent)
    collisionNumpyArray, colorNumpyArray = destroy_terrain_circle((10,300), 200, collisionNumpyArray, colorNumpyArray)

    # Main game loop.
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #DISPLAYSURF.blit(surf, (0,0))
            # NEW BLIT METHOD
            pygame.surfarray.blit_array(DISPLAYSURF, colorNumpyArray)
            pygame.display.update()


    # print(screenPixelArray[599,20])
    # if screenPixelArray[10,10][1] == SKYBLUE[1]:
    #     screenPixelArray[10:20,10:20] = GREEN
    # print(numpyPixel[20,599])
    #numpy.set_printoptions(threshold=sys.maxsize)
    #numpy.set_printoptions(linewidth=200)
    #print(numpyPixel)
    # Makes it so full numpy array is displayed in terminal
    # Be careful when using large resolutions
    # numpy.set_printoptions(threshold=sys.maxsize)
    # # Set linewidth to the size of a single line of numpy array (when printed)
    # numpy.set_printoptions(linewidth=140)
    # file1 = open("MyFile.txt","a")
    # print()
    # print(numpyPixel)
    # file1.write(str(numpyPixel))
    # file1.close()