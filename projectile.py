import game_ui
import math
import pygame
import time

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

class Projectile(object):
    # X_ret,y_ret: coords of reticle
    # radius: size of bullet (keep fixed at something small for now)
    # player: player object that is firing the projectile
    def __init__(self,x_ret,y_ret,xpos_cannon,ypos_cannon,screen):
        self.x_ret = x_ret
        self.y_ret = y_ret
        self.x = xpos_cannon
        self.y = ypos_cannon
        self.screen = screen
        self.y_change = float(abs(self.x_ret-ypos_cannon))
        self.x_change = float(abs(self.y_ret-xpos_cannon))
        self.angle = math.atan(self.y_change/self.x_change)
        self.gravity = 9.80
        self.color = (105, 105, 105) # Grey bullet
        self.per_pix_speed = 10  # Pixels per second 
        self.to_ret_sec = 3.0 # Seconds to reach reticle (help in velocity calc)
        self.initial_v = self.get_initial_velocity()
        self.round_img = pygame.image.load('assets/tank_round.png')

    # Returns true and the coordinates as a tuple if there is a collision
    # Returns false and the coordinates (0,0) if there is no collision
    def animate_proj(self,x_ret,y_ret,xpos_cannon,ypos_cannon,numpy_pixel):
        print("Before update: (", x_ret, y_ret,") (",xpos_cannon,ypos_cannon,")")
        print("~~~INIT V:", self.initial_v)
        print("Changes:", self.x_change,self.y_change)
        self.update_values(x_ret,y_ret,xpos_cannon,ypos_cannon)
        print("After update: (", x_ret, y_ret,") (",xpos_cannon,ypos_cannon,")")
        print("~~~INIT V:", self.initial_v)
        print("Changes:", self.x_change,self.y_change)
        print("##ANGLEEEEEE:", self.angle)
        print("sinnnLEEEEEE:", math.sin(self.angle))
        init_x = self.x
        init_y = DISPLAY_HEIGHT-self.y
        flip_shot = 1
        if(self.x_change<0):
            flip_shot = -1
        blit_counter = 0
        for sec in [x * 0.001 for x in range(0, 10000)]:
            print("Blit: ",sec, "has: (",self.x,self.y,")")
            # if doesnt go out of bounds
            if not (self.x > DISPLAY_WIDTH or self.y > DISPLAY_HEIGHT or 
                self.x < 0 or self.y < 0):
                if numpy_pixel[int(self.y),int(self.x)] == 1:
                    return True, (int(self.x),int(self.y))
                    print("COLLSION-----------------COLLSION-----------------")
            else:
                break
            blit_counter += 1
            if blit_counter % 600 == 0:
                self.screen.blit(self.round_img, (self.x,self.y))

            self.x = (init_x + (flip_shot*(self.initial_v*sec*math.cos(self.angle))))
            self.y = DISPLAY_HEIGHT-( init_y + (self.initial_v*sec*flip_shot*math.sin(self.angle)-((0.5*self.gravity*pow(sec,2)))))
            pygame.display.update()
        return False, (0,0)

    def get_initial_velocity(self):
        dist_to_ret = math.sqrt(pow(self.x_change,2)+pow(self.y_change,2))
        top = self.y_change - (0.5 * self.gravity * pow(self.to_ret_sec,2))
        bot = self.to_ret_sec*math.sin(self.angle)
        y_init_vel = top/bot
        x_init_vel = self.x_change/self.to_ret_sec
        return math.sqrt(pow(y_init_vel,2)+pow(x_init_vel,2))

    def update_values(self,x_ret,y_ret,xpos_cannon,ypos_cannon):
        self.x_ret = x_ret
        self.y_ret = y_ret
        self.x = xpos_cannon
        self.y = ypos_cannon
        self.y_change = float(abs(self.y_ret-ypos_cannon))
        self.x_change = float((self.x_ret-xpos_cannon))
        self.angle = math.atan(self.y_change/self.x_change)
        self.initial_v = self.get_initial_velocity()


# NEED TO TWEAK VELOCITIES AND SUCH