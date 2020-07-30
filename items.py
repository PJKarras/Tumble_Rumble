import pygame

class item:
    def __init__(self, spr_item, xpos, screen, pixelMatrix):
        itemRawImg = pygame.image.load(spr_item)
        newSize = (int(itemRawImg.get_width() * 0.5), int(itemRawImg.get_height() * 0.5))
        self.spr = pygame.transform.scale(itemRawImg, newSize)
        self.screen = screen
        self.pixelMatrix = pixelMatrix
        self.true_xpos = xpos

        self.setSpawn()

    def setSpawn(self):
        ypos = 0
        num = 0
        while int(num) == 0:
            ypos += 1
            num = self.pixelMatrix[int(ypos), int(self.true_xpos)]
        self.true_ypos = ypos
        # need to adjust x and y positions to look in place on map
        self.xpos = self.true_xpos - (0.5 * self.spr.get_width())
        self.ypos = self.true_ypos - (0.5 * self.spr.get_height())


    def _Update(self):
        self.screen.blit(self.spr, (self.xpos, self.ypos))

    def getXPos(self):
        return self.true_xpos

    def getSprite(self):
        return self.spr

# end of item class

class shield(item):
    def __init__(self, xpos, screen, pixelMatrix):
        super(shield, self).__init__("assets/items/shield.png", xpos, screen, pixelMatrix)

    def update(self):
        super(shield, self)._Update()
        
    def itemName(self):
        return "shield"

# end of shield class

class bomb(item):
    def __init__(self, xpos, screen, pixelMatrix):
        super(bomb, self).__init__("assets/items/nuke.png", xpos, screen, pixelMatrix)

    def update(self):
        super(bomb, self)._Update()
        
    def itemName(self):
        return "bomb"

# end of bomb class

class wrench(item):
    def __init__(self, xpos, screen, pixelMatrix):
        super(wrench, self).__init__("assets/items/wrench.png", xpos, screen, pixelMatrix)

    def update(self):
        super(wrench, self)._Update()
        
    def itemName(self):
        return "wrench"

class jetPack(item):
    def __init__(self, xpos, screen, pixelMatrix):
        super(jetPack, self).__init__("assets/items/jetPack.png", xpos, screen, pixelMatrix)

    def update(self):
        super(jetPack, self)._Update()
        
    def itemName(self):
        return "jetPack"

# end of jetPack class
