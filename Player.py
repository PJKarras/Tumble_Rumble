import pygame

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

class Player:

    def __init__(self, spr_player, spr_cannon, playerNum, screen, pixelMatrix):
        self.spr_player_right = spr_player

        # need to flip player sprite to create left facing player sprite
        self.spr_player_left = pygame.transform.flip(spr_player, True, False)

        self.screen = screen
        self.pixelMatrix = pixelMatrix

        # set the spawn position
        self.playerNum = playerNum
        self.setSpawn()

        self.spr_cannon_right = spr_cannon

        # need to flip cannon sprite to create left facing cannon sprite
        self.spr_cannon_left = pygame.transform.flip(spr_cannon, True, False)

        # determine which way the tank is facing at time of spawn
        # we will also use this to determine spawn position of cannon
        # this also normalizes the sprite position
        if self.xpos <= int(screen.get_width() * 0.5):
            self.spr_player = self.spr_player_right
            self.spr_cannon = self.spr_cannon_right
            self.xpos = self.xpos - (0.5 * self.spr_player.get_width())
            self.ypos = self.ypos - (0.75 * self.spr_player.get_height())
            self.xpos_cannon = self.xpos + int(0.25 * self.spr_player_right.get_width())
            self.ypos_cannon = self.ypos
        else:
            self.spr_player = self.spr_player_left
            self.spr_cannon = self.spr_cannon_left
            self.xpos_cannon = self.xpos - int(0.25 * self.spr_player_left.get_width())
            self.ypos_cannon = self.ypos

        # create hit-box
        self.hitbox = (self.xpos + 1, self.ypos + 1, self.spr_player.get_width(), self.spr_player.get_height()+20)

        # create health bar
        self.health = 13
        self.visible = True

        # create fuel bar
        self.fuelAmount = 7.2
        self.canMove = True

        # normalize the spawn

    # end of constructor
    def setSpawn(self):
        self.xpos = (self.playerNum * 0.20) * self.screen.get_width()
        ypos = 0
        num = 0
        while int(num) == 0:
            ypos += 1
            num = self.pixelMatrix[int(ypos), int(self.xpos)]
        self.ypos = ypos
        # these tell us the true coordinate position, or rather, the exact center of the sprite
        self.true_xpos = self.xpos
        self.true_ypos = self.ypos


    # changes the position of the player; dx = "change in x position"
    def Change_Pos(self, dx = None, event_key = None):
        if dx == None:
            self._Update()
        else:
            if dx == 0:
                self._Update()
            else:
                if event_key == pygame.K_a:
                    self.spr_player = self.spr_player_left
                    self.spr_cannon = self.spr_cannon_left

                    if (self.xpos - dx) < 0:
                        self._Update()
                    else:
                        # obtain xpos
                        self.decreaseFuel(dx)
                        self.xpos -= dx
                        self.true_xpos -= dx
                        self.xpos_cannon = self.xpos - int(0.25 * self.spr_player_left.get_width())
                        # obtain ypos
                        self.find_ypos()
                        self.ypos_cannon = self.ypos
                        # update the screen
                        self._Update()
                elif event_key == pygame.K_d:
                    self.spr_player = self.spr_player_right
                    self.spr_cannon = self.spr_cannon_right

                    if (self.xpos + dx) > (self.screen.get_width() - self.spr_player.get_width()):
                        self._Update()
                    else:
                        # obtain xpos
                        self.decreaseFuel(dx)
                        self.xpos += dx
                        self.true_xpos += dx
                        self.xpos_cannon = self.xpos + int(0.25 * self.spr_player_right.get_width())
                        # obtain ypos
                        self.find_ypos()
                        self.ypos_cannon = self.ypos
                        # update the screen
                        self._Update()
                elif event_key == pygame.K_h:
                    #print("Hit")
                    self.hit()
                    self._Update()


    # end of Change_Pos

    #

    def find_ypos(self):
        check_ahead = self.pixelMatrix[int(self.true_ypos), int(self.true_xpos)]
        if int(check_ahead) == 0:
            while int(check_ahead) == 0:
                self.ypos += 1
                self.true_ypos += 1
                if (self.true_ypos > self.screen.get_height() - 1):
                    break
                check_ahead = self.pixelMatrix[int(self.true_ypos), int(self.true_xpos)]
            self.ypos -= 1
            self.true_ypos -= 1
        elif int(check_ahead) == 1:
            while int(check_ahead) == 1:
                self.ypos -= 1
                self.true_ypos -= 1
                if(self.true_ypos > self.screen.get_height() - 1):
                    break
                check_ahead = self.pixelMatrix[int(self.true_ypos), int(self.true_xpos)]
            self.ypos += 1
            self.true_ypos += 1

    # if player is hit, call this function
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


    # decreases fuel
    def decreaseFuel(self, dx):
        if self.fuelAmount > 0:
            self.fuelAmount -= dx
        else:
            self.canMove = False

    # if fuel is empty, returns true
    def isFuelEmpty(self):
        if self.fuelAmount <= 0:
            return True
        else:
            return False

    # blit's the player object to screen, updating its position
    def _Update(self):
        self.screen.blit(self.spr_cannon, (self.xpos_cannon, self.ypos_cannon))
        self.screen.blit(self.spr_player, (self.xpos, self.ypos))
        self.hitbox = (self.xpos, self.ypos + 20, self.spr_player.get_width(), self.spr_player.get_height()-20)

        # for testing hitbox
        # draws hitbox around player
        pygame.draw.rect(self.screen, (255,0,0), self.hitbox, 2)

        # draws health bar over player
        pygame.draw.rect(self.screen, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 65, 10))
        pygame.draw.rect(self.screen, (102,255,102), (self.hitbox[0], self.hitbox[1] - 20, 65 - (5 * (13 - self.health)), 10))

        # draws fuel bar
        pygame.draw.rect(self.screen, (255, 0, 0), ((DISPLAY_WIDTH * .24, DISPLAY_WIDTH * .02), (65, 10)))
        pygame.draw.rect(self.screen, (102, 255, 102),((DISPLAY_WIDTH * .24, DISPLAY_WIDTH * .02), (65 - (9.027 * (7.2 - self.fuelAmount)), 10)))

    # end of _Update


# end of Player class
