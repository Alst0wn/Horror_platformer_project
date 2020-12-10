import pygame
from player_class import *
from visual_module import *

class Image():
    def __init__(self):
        self.x = 800
        self.y = 600
        self.forest_surf = pygame.image.load('forest.jpg')
        self.forest_rect = self.forest_surf.get_rect(
            bottomright=(self.x, self.y))



def gameplay(screen, clock, levelname):
    image = Image()
    FPS = 30
    finished = False
    player, level = level_read(levelname)
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
        player.move(image)
        for obj in level:
            player.collision(obj, True)
        player.deathcheck()
        if player.dead:
            finished = True
        pygame.display.update()
        screen.blit(image.forest_surf, image.forest_rect)
        frame_draw(level, player, 600, 800, screen, 1600)
