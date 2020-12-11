import pygame
from player_class import *
from visual_module import *


def check_display(list_obj, char):
    o_high = list_obj[2]
    o_low = list_obj[1]
    o_left = list_obj[4]
    o_right = list_obj[3]
    if char.y - 600 > o_high.y:
        for i in list_obj:
            i.y += 600
    if char.y + 1200 < o_low.y:
        for i in list_obj:
            i.y -= 600
    if char.x - 800 > o_left.x:
        for i in list_obj:
            i.x += 800
    if char.x + 1600 < o_right.x:
        for i in list_obj:
            i.x -= 800

class Image():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.forest_surf = pygame.image.load('forest.jpg')
        self.forest_rect = self.forest_surf.get_rect(
            bottomright=(self.x, self.y))


def gameplay(screen, clock, levelname):
    image = Image(800, 600)
    image_low = Image(800, 1200)
    image_high = Image(800, 0)
    image_right = Image(1600, 600)
    image_left = Image(0, 600)
    image_righth = Image(1600, 0)
    image_lefth = Image(0, 0)
    image_rightl = Image(1600, 1200)
    image_leftl = Image(0, 1200)
    image_list = [image, image_low, image_high,
                  image_right, image_left, image_righth,
                  image_lefth, image_rightl, image_leftl]
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
        player.move(image_list)
        #check_display(image_list, player) I don't know where it has to be
        for obj in level:
            player.collision(obj, True)
        player.deathcheck()
        if player.dead:
            finished = True
        if player.note==1:
            loop = False
            note(screen, 800, 600)
            pygame.display.update()
            while not loop:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        loop = True
                clock.tick(FPS)
            player.note = -1
        pygame.display.update()
        for im in image_list:
            screen.blit(im.forest_surf, im.forest_rect)
        frame_draw(level, player, 600, 800, screen, 1600)
    return player.win