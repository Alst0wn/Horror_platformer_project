import pygame
import pygame.draw

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


def frame_draw(plat, char, hight, width, screen, scale):
    for i in plat:
        i.image = pygame.transform.scale(i.image,
                                         (int(hight / scale * i.xscale), int(hight / scale * i.yscale)))
        i.rect = (int(hight / scale * (i.x - char.x) + width / 2),
                                          int(hight / scale * (i.y - char.y) + 0.7 * hight))
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
                                        (int(hight / scale * char.xscale), int(hight / scale * char.yscale)))
    char.rect = (int(width / 2), int(0.7 * hight))
    screen.blit(char.image, char.rect)


def note(screen, width, height):
    pygame.draw.rect(screen, (200,200,200), (width//4, height//4,width//2, \
                        height//2))