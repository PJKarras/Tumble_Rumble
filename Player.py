import pygame

class Player:

    def __init__(self, spr_player, spr_cannon, spawn_x, spawn_y, screen):
        self.spr_player_right = spr_player

        # need to flip player sprite to create left facing player sprite
        self.spr_player_left = pygame.transform.flip(spr_player, True, False)

        # set the spawn position
        self.xpos = spawn_x
        self.ypos = spawn_y

        self.spr_cannon_right = spr_cannon

        # need to flip cannon sprite to create left facing cannon sprite
        self.spr_cannon_left = pygame.transform.flip(spr_cannon, True, False)

        self.screen = screen

        # determine which way the tank is facing at time of spawn
        # we will also use this to determine spawn position of cannon
        if spawn_x <= int(screen.get_width() * 0.5):
            self.spr_player = self.spr_player_right
            self.spr_cannon = self.spr_cannon_right
            self.xpos_cannon = self.xpos + int(0.25 * self.spr_player_right.get_width())
            self.ypos_cannon = self.ypos
        else:
            self.spr_player = self.spr_player_left
            self.spr_cannon = self.spr_cannon_left
            self.xpos_cannon = self.xpos - int(0.25 * self.spr_player_left.get_width())
            self.ypos_cannon = self.ypos

    # end of constructor

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
                        self.xpos -= dx
                        self.xpos_cannon = self.xpos - int(0.25 * self.spr_player_left.get_width())
                        self._Update()
                elif event_key == pygame.K_d:
                    self.spr_player = self.spr_player_right
                    self.spr_cannon = self.spr_cannon_right

                    if (self.xpos + dx) > (self.screen.get_width() - self.spr_player.get_width()):
                        self._Update()
                    else:
                        self.xpos += dx
                        self.xpos_cannon = self.xpos + int(0.25 * self.spr_player_right.get_width())
                        self._Update()

    # end of Change_Pos


    # blit's the player object to screen, updating its position
    def _Update(self):
        self.screen.blit(self.spr_cannon, (self.xpos_cannon, self.ypos_cannon))
        self.screen.blit(self.spr_player, (self.xpos, self.ypos))

    # end of _Update


# end of Player class