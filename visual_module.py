import pygame
import pygame.draw

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


def frame_draw(plat, char, hight, width, screen, scale):
    screen.fill(WHITE)
    for i in plat:
        pygame.draw.rect(screen, GREEN,
                         (int(hight / scale * (
                                     i.x - char.x) + width / 2),
                          int(hight / scale * (
                                      i.y - char.y) + 0.7 * hight),
                          int(hight / scale * i.xscale),
                          int(hight / scale * i.yscale)))
    pygame.draw.rect(screen, (255, 0, 0),
                     (int(width / 2), int(0.7 * hight),
                      int(hight / scale * char.xscale),
                      int(hight / scale * char.yscale)))