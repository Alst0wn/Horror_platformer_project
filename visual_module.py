import pygame
import pygame.draw

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


class Image:
    """class of images that make up the background"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.forest_surf = pygame.image.load('ok.jpg')
        self.forest_surf = pygame.transform.scale(self.forest_surf,
                                                  (2400, 1800))
        self.forest_rect = self.forest_surf.get_rect(
            bottomright=(self.x, self.y))


def create_image(x, y, im_list):
    """function creates a new background image"""
    image = Image(x + 800, y + 600)
    im_list += [image]


def frame_draw(plat, char, notes, h, width, screen, sc):
    """functions draws a frame of the game with platforms in plat,
    character char, notes in notes with frame height h and
    width width on screen screen scaled with sc"""
    for i in plat:
        i.image = pygame.transform.scale(i.image,
                                         (int(h / sc * i.xscale),
                                          int(h / sc * i.yscale)))
        i.rect = (int(h / sc * (i.x - char.x) + width / 2),
                  int(h / sc * (i.y - char.y) + 0.7 * h))
        screen.blit(i.image, i.rect)
    for i in notes:
        if not i.disabled:
            i.image = pygame.transform.scale(i.image,
                                             (int(h / sc * i.xscale),
                                              int(h / sc * i.yscale)))
            i.rect = (int(h / sc * (i.x - char.x) + width / 2),
                      int(h / sc * (
                              i.y - char.y) + 0.7 * h))
            screen.blit(i.image, i.rect)
    if char.grounded and char.right:
        char.image = pygame.image.load('groundright.png')
    elif char.grounded and not char.right:
        char.image = pygame.image.load('groundleft.png')
    elif not char.grounded and char.vx > 0:
        char.image = pygame.image.load('airright.png')
    elif not char.grounded and char.vx <= 0:
        char.image = pygame.image.load('airleft.png')
    char.image = pygame.transform.scale(char.image,
                                        (int(h / sc * char.xscale),
                                         int(h / sc * char.yscale)))
    char.rect = (int(width / 2), int(0.7 * h))
    screen.blit(char.image, char.rect)


def notedraw(screen, width, height, note):
    """function draws a note on top of the frame"""
    note1 = note
    note1.image = pygame.image.load(
        'notebackground' + note1.picture + '.png')
    note1.image = pygame.transform.scale(note1.image,
                                         (width // 2, height // 2))
    note1.rect = (width // 4, height // 4)
    screen.blit(note1.image, note1.rect)


if __name__ == "__main__":
    print("This module is not for direct call!")
