import pygame
import pygame.draw

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


def frame_draw(plat, char, notes, hight, width, screen, scale):
    for i in plat:
        i.image = pygame.transform.scale(i.image,
                                         (int(
                                             hight / scale * i.xscale),
                                          int(
                                              hight / scale * i.yscale)))
        i.rect = (int(hight / scale * (i.x - char.x) + width / 2),
                  int(hight / scale * (i.y - char.y) + 0.7 * hight))
        screen.blit(i.image, i.rect)
    for i in notes:
        if not i.disabled:
            i.image = pygame.transform.scale(i.image,
                                             (int(
                                                 hight / scale * i.xscale),
                                              int(
                                                  hight / scale * i.yscale)))
            i.rect = (int(hight / scale * (i.x - char.x) + width / 2),
                      int(hight / scale * (
                                  i.y - char.y) + 0.7 * hight))
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
                                        (int(
                                            hight / scale * char.xscale),
                                         int(
                                             hight / scale * char.yscale)))
    char.rect = (int(width / 2), int(0.7 * hight))
    screen.blit(char.image, char.rect)


def notedraw(screen, width, height, note):
    note1=note
    note1.image = pygame.image.load(
        'notebackground'+note1.picture+'.png')
    note1.image = pygame.transform.scale(note1.image,
                                         (width // 2, height // 2))
    note1.rect = (width // 4, height // 4)
    screen.blit(note1.image, note1.rect)
