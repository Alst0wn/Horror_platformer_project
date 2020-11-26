import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
player, level = levelread('testlevel')
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
            if event.key == pygame.K_space:
                player.jump(level)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                apress = False
            if event.key == pygame.K_d:
                dpress = False

    if dpress:
        player.speedup(level, +1)
    if apress:
        player.speedup(level, -1)
    player.move()
    for obj in level:
        collision(obj, True)
    pygame.display.update()
    framedraw(player, level)
