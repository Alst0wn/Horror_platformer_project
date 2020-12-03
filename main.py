import pygame
from player_class import *
from visual_module import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
player, level = level_read('level_1.txt')
dpress, apress = False, False

while not finished:  # gameplay
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and not dpress:
                apress = True
            if event.key == pygame.K_d and not apress:
                dpress = True
            if event.key == pygame.K_w:
                player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                apress = False
            if event.key == pygame.K_d:
                dpress = False

    player.groundcheck(level)
    if dpress:
        player.speedup(+1)
    if apress:
        player.speedup(-1)
    player.move()
    for obj in level:
        player.collision(obj, True)
    player.deathcheck()
    if player.dead:
        finished = True
    pygame.display.update()
    frame_draw(level, player, 600, 800, screen, 1600)

pygame.quit()