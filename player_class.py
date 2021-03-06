import pygame


class Character:

    def __init__(self):
        self.name = 'Julia'
        # the name of the character
        self.x = 0
        # the x position of upper left corner of the character
        self.y = 0
        # the y position of upper left corner of the character
        self.y0 = 0
        # the initial y position of upper left corner of the
        # character
        self.prevx = 0
        # the previous x position of upper left corner of the
        # character
        self.prevy = 0
        # the previous y position of upper left corner of the
        # character
        self.vx = 0
        # the x component of the character's speed
        self.vy = 0
        # the y component of the character's speed
        self.xscale = 200
        # the x scale of the character in centimeters
        self.yscale = 400
        # the y scale of the character in centimeters
        self.texturename = 1
        # number of the current character texture
        self.image = pygame.image.load('groundright.png')  # creates
        # a texture
        self.image = pygame.transform.scale(self.image, (
            self.xscale, self.yscale))
        self.rect = self.image.get_rect()
        self.doublejump = 1
        # how many doublejuns does character have left
        self.grounded = False
        # boolean if character is standing on the ground
        self.dead = False
        # boolean if character is dead
        self.win = False
        # boolean if the exit is hit
        self.right = True
        # boolean if the character is facing right

    def move(self, list_obj, g=1):
        """function moves the character in gravitational field g"""
        self.prevx = self.x
        self.prevy = self.y
        for obj in list_obj:
            obj.x -= self.vx / 2
            obj.y -= self.vy / 2
            obj.forest_rect = obj.forest_surf.get_rect(
                bottomright=(obj.x, obj.y))
        self.x += self.vx
        self.y += self.vy
        if self.grounded:
            self.vx = 0
        else:
            self.vy += g

    def groundcheck(self, surfs):
        """function checks if the character is standing on the
        ground"""
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
        if obj.type == 0 or obj.type == 1 or obj.type == \
                5:  # collisions with platforms
            if rectobj.colliderect((self.x, self.y, self.xscale,
                                    self.yscale)):
                if rectobj.colliderect(
                        (self.prevx, self.y, self.xscale,
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
        else:
            if change:
                if rectobj.colliderect((self.x, self.y,
                                        self.xscale,
                                        self.yscale)) and obj.type \
                        == 2:  # collision with exit
                    self.win = True
                    self.dead = True
            if rectobj.colliderect((self.x, self.y,
                                    self.xscale,
                                    self.yscale)) and obj.type \
                    == 4 and change:  # collisions with notes
                return True
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
        """function checks if the character is out of bounds"""
        if abs(self.x) > 10000 or self.y - self.y0 > 4000:
            self.dead = True


class Platform:
    """class for interactable nonmovable oblects """

    def __init__(self, x, y, pl_width, pl_length, pl_type):
        self.x = float(x)
        # the x position of upper left corner of the object
        self.y = float(y)
        # the y position of upper left corner of the object
        self.xscale = float(pl_width)
        # the x scale of the object in centimeters
        self.yscale = float(pl_length)
        # the y scale of the object in centimeters
        self.type = int(pl_type)
        # the number of type of the object
        if int(pl_type) == 0:
            self.image = pygame.image.load('platformtexture.jpg')
        if int(pl_type) == 1:
            self.image = pygame.image.load('platformtexture.jpg')
        if int(pl_type) == 2:
            self.image = pygame.image.load('exit.png')
        if int(pl_type) == 3:
            self.image = pygame.image.load('platformtexture.jpg')
        if int(pl_type) == 4:
            self.image = pygame.image.load('platformtexture.jpg')
        if int(pl_type) == 5:
            self.image = pygame.image.load('platformtexture.jpg')
        self.image = pygame.transform.scale(self.image, (
            int(self.xscale), int(self.yscale)))
        self.rect = self.image.get_rect()
        # attributes for drawing


class Note:
    """class for notes"""

    def __init__(self, x, y, width, picture, type):
        self.x = float(x)
        self.y = float(y)
        self.xscale = float(width)
        self.yscale = self.xscale
        self.type = int(type)
        self.xscaleshow = 100
        self.yscaleshow = 200
        self.disabled = False
        self.picture = picture
        self.image = pygame.image.load(
            'note.png')
        self.image = pygame.transform.scale(self.image,
                                            (self.xscaleshow,
                                             self.yscaleshow))
        self.rect = self.image.get_rect()


def level_read(levelname):
    """function reads level data from file"""
    file = open(levelname, 'r')
    plat = []
    notes = []
    lines = file.readlines()
    player = Character()
    player.x = int(lines[0].split()[0])
    player.y = int(lines[0].split()[1])
    player.y0 = player.y
    lines.pop(0)
    for line in lines:
        a = line.split()
        x_cord, y_cord, p_width, parameter, p_type = a
        if not int(p_type) == 4:
            plat.append(
                Platform(x_cord, y_cord, p_width, parameter, p_type))
        else:
            notes.append(
                Note(x_cord, y_cord, p_width, parameter, p_type))
    file.close()
    return player, plat, notes


if __name__ == "__main__":
    print("This module is not for direct call!")
