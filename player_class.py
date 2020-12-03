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
        self.xscale = 50
        """the x scale of the character in centimeters """
        self.yscale = 200
        """the y scale of the character in centimeters """
        self.texturename = 1
        """number of the current character texture"""
        self.doublejump = 1
        self.grounded = False
        self.dead = False

    def move(self, g=1):
        """function moves the character in gravitational field g"""
        self.prevx = self.x
        self.prevy = self.y
        self.x += self.vx
        self.y += self.vy
        if self.grounded:
            self.vx = 0
        else:
            self.vy += g


    def groundcheck (self, surfs):
        k = 0
        checkself = self
        checkself.y += 1
        for surf in surfs:
            k += int(checkself.collision(surf, False))
        if k > 0:
            self.grounded = True
            self.vx = 0
        else:
            self.grounded = False

    def collision(self, obj, change):
        """function checks for collision with the object obj - bull
            checks if you need to change the properties of
             a character """
        rectobj = pygame.Rect(obj.x, obj.y, obj.xscale, obj.yscale)
        if rectobj.colliderect((self.x, self.y, self.xscale,
                               self.yscale)):
            if rectobj.colliderect((self.prevx, self.y, self.xscale,
                                   self.yscale)) and change:
                if self.vy >= 0:
                    self.vy = 0
                    self.vx = 0
                    self.y = obj.y - self.yscale
                    self.doublejump = 1
                else:
                    self.vy = -self.vy
                    self.y = obj.y + obj.yscale
            elif change:
                self.vx = -self.vx
                self.x = self.prevx
            return True
        else:
            return False

    def jump(self):
        """function makes a character jump of the surfaces in surf"""
        if self.grounded:
            self.vy -= 30
        elif self.doublejump == 1:
            self.vy -= 30
            self.doublejump = 0

    def speedup(self, coef):
        """function makes a character speed up on the surfaces in
        surf or in the air - coef defines the direction"""
        if self.grounded:
            self.vx = coef * 20
        else:
            self.vx += coef * 0.4

    def deathcheck(self):
        self.dead = (abs(self.x) > 100000 or abs(self.y) > 100000)


class Platform:
    def __init__(self, x, y, pl_width, pl_length):
        self.x = float(x)
        self.y = float(y)
        self.xscale = float(pl_width)
        self.yscale = float(pl_length)
        self.color = (0, 255, 0)


def level_read(levelname):
    file = open(levelname, 'r')
    plat = []
    lines = file.readlines()
    player = Character()
    player.x = int(lines[0].split()[0])
    player.y = int(lines[0].split()[1])
    lines.pop(0)
    for line in lines:
        a = line.split()
        x_cord, y_cord, p_width, p_length = a
        plat.append(Platform(x_cord, y_cord, p_width, p_length))
    file.close()
    return player, plat
