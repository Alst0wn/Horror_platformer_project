import pygame


class Character:

    def __init__(self):
        self.name = 'Julia'
        """the name of the character"""
        self.x = 0
        """the x position of upper left corner of the character"""
        self.y = 0
        """the y position of upper left corner of the character"""
        self.prevx = 0
        """the previous x position of upper left corner of the 
            character """
        self.prevy = 0
        """the previous y position of upper left corner of the 
        character """
        self.vx = 0
        """the x component of the character's speed"""
        self.vy = 0
        """the y component of the character's speed"""
        self.xscale = 0.5
        """the x scale of the character in meters """
        self.yscale = 2
        """the y scale of the character in meters """
        self.texturename = 1
        """number of the current character texture"""
        self.doublejump = 1

    def move(self, g=5):
        """function moves the character in gravitational field g"""
        self.prevx = self.x
        self.prevy = self.y
        self.x += self.vx
        self.y += self.vy
        self.vy += g

    def collision(self, obj, change):
        """function checks for collision with the object obj - bull
            checks if you need to change the properties of
             a character """
        rectobj = pygame.Rect(obj.x, obj.y, obj.xscale, obj.yscale)
        if rectobj.colliderect(self.x, self.y, self.xscale,
                               self.yscale):
            if rectobj.colliderect(self.prevx, self.y, self.xscale,
                                   self.yscale) and change:
                if self.vy > 0:
                    self.vy = 0
                    self.y = obj.y - self.yscale
                    self.doublejump = 1
                else:
                    self.vy = -self.vy
                    self.y = obj.y + obj.yscale
            elif change:
                self.vx = -self.vx
            return True
        else:
            return False

    def jump(self, surfs):
        """function makes a character jump of the surfaces in surf"""
        k = 0
        checkself = self
        checkself.x -= 0.01
        for surf in surfs:
            k += int(checkself.collision(surf, False))
        if k > 0:
            self.vy -= 10
        elif self.doublejump == 1:
            self.vy -= 10
            self.doublejump = 0
