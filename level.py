import pygame
from player_class import *
from visual_module import *


def gameplay(screen, clock, levelname):
    """function with the main game loop

    takes pygame screen and clock
    also the name of the level file"""
    image_list = []
    for i in range(-1, 3):
        for j in range(-4, 2):
            create_image(2400 * i, 1800 * j, image_list)

    FPS = 30
    finished = False
    player, level, notes = level_read(levelname)
    dpress, apress = False, False

    while not finished:  # gameplay
        clock.tick(FPS)
        for event in pygame.event.get():  # event processing
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

        player.groundcheck(level)  # move functions
        if dpress:
            player.speedup(+1)
            player.right = True
        if apress:
            player.speedup(-1)
            player.right = False
        player.move(image_list)
        for obj in level:  # collisions and interactions functions
            player.collision(obj, True)
        player.deathcheck()
        if player.dead:
            finished = True
        for note in notes:
            if player.collision(note, True) and not note.disabled:
                loop = False
                notedraw(screen, 800, 600, note)
                pygame.display.update()
                while not loop:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            loop = True
                    clock.tick(FPS)
                note.disabled = True
                dpress = pygame.key.get_pressed()[pygame.K_d]
                if not dpress:
                    apress = pygame.key.get_pressed()[pygame.K_a]
                else:
                    apress = 0

        pygame.display.update()  # frame drawing
        for im in image_list:
            screen.blit(im.forest_surf, im.forest_rect)
        frame_draw(level, player, notes, 600, 800, screen, 1600)
    return player.win
