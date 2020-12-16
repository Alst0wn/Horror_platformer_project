import pygame.draw
import sys
from level import *

pygame.init()
font = pygame.font.Font(None, 60)
font1 = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 180)
FPS = 30
width = 800
length = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREY = (100, 100, 100)
SLIGHT_GREY = (200, 200, 200)

# creating display
screen = pygame.display.set_mode((width, length))
clock = pygame.time.Clock()
finished = False


def initial_display_draw(screen):
    """function draws initial menu on screen"""
    forest_surf = pygame.image.load('forest.jpg')
    forest_rect = forest_surf.get_rect(
        bottomright=(width, length))
    screen.blit(forest_surf, forest_rect)
    dark_forest = pygame.image.load('name.png')
    pygame.transform.scale(dark_forest, (400, 150))
    dark_rect = (200, 70)
    screen.blit(dark_forest, dark_rect)
    tlevel_1 = font2.render('PLAY', True, BLACK, WHITE)
    screen.blit(tlevel_1, (245, 300))
    tlevel_2 = font.render('QUIT', True, BLACK, WHITE)
    screen.blit(tlevel_2, (345, 545))
    tsettings = font.render('Settings', True, BLACK, WHITE)
    screen.blit(tsettings, (310, 465))


def in_scr_choice(screen):
    """function provides opportunity to select what to do"""
    initial_display_draw(screen)
    for ins in pygame.event.get():
        if ins.type == pygame.QUIT:
            sys.exit()
        if ins.type == pygame.MOUSEBUTTONDOWN:
            if ins.button == 1:
                x_in, y_in = ins.pos
                if x_in > 245 and x_in < 570 and y_in > 300 and y_in < 425:
                    pygame.display.update()
                    menu_choice(screen)
                if x_in > 345 and x_in < 445 and y_in > 545 and y_in < 590:
                    pygame.display.update()
                    sys.exit()
                if x_in > 310 and x_in < 485 and y_in > 465 and y_in < 509:
                    pygame.display.update()
                    music_choice(screen)
                pygame.display.update()
    pygame.display.update()


def menu(screen):
    """function draws menu, where we can choose levels"""
    forest_surf = pygame.image.load('forest.jpg')
    forest_rect = forest_surf.get_rect(
        bottomright=(width, length))
    screen.blit(forest_surf, forest_rect)
    tlevel_1 = font.render('Level 1', True, BLACK, WHITE)
    screen.blit(tlevel_1, (175, 50))
    tlevel_2 = font.render('Level 2', True, BLACK, WHITE)
    screen.blit(tlevel_2, (175, 150))
    tlevel_3 = font.render('Level 3', True, BLACK, WHITE)
    screen.blit(tlevel_3, (175, 250))
    tlevel_4 = font.render('Level 4', True, BLACK, WHITE)
    screen.blit(tlevel_4, (175, 350))
    tlevel_6 = font.render('Level 5', True, BLACK, WHITE)
    screen.blit(tlevel_6, (475, 50))
    tlevel_7 = font.render('Level 6', True, BLACK, WHITE)
    screen.blit(tlevel_7, (475, 150))
    tlevel_8 = font.render('Level 7', True, BLACK, WHITE)
    screen.blit(tlevel_8, (475, 250))
    tlevel_9 = font.render('Level 8', True, BLACK, WHITE)
    screen.blit(tlevel_9, (475, 350))
    tlevel_2 = font.render('BACK', True, BLACK, WHITE)
    screen.blit(tlevel_2, (345, 545))


def menu_choice(screen):
    """function provides opportunity to select level"""
    fin = False
    while not fin:
        menu(screen)
        file_key = open('level_key.txt', 'r')
        level_key = int(file_key.read())
        file_key.close()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    x, y = i.pos
                    if x > 345 and x < 445 and y > 545 and y < 590:
                        pygame.display.update()
                        fin = True
                    if x > 175 and x < 320 and y > 50 and y < 94:
                        pygame.display.update()
                        if level_key >= 1:
                            if gameplay(screen, clock, 'level_1.txt') \
                                    and level_key == 1:
                                level_key = 2
                        else:
                            locked(screen)
                            clock.tick(FPS)
                    if x > 175 and x < 320 and y > 150 and y < 194:
                        pygame.display.update()
                        if level_key >= 2:
                            if gameplay(screen, clock, 'level_2.txt') \
                                    and level_key == 2:
                                level_key = 3
                        else:
                            locked(screen)
                            clock.tick(FPS)
                    if x > 175 and x < 320 and y > 250 and y < 294:
                        pygame.display.update()
                        if level_key >= 3:
                            if gameplay(screen, clock, 'level_3.txt') \
                                    and level_key == 3:
                                level_key = 4
                        else:
                            locked(screen)
                            clock.tick(FPS)
                    if x > 175 and x < 320 and y > 350 and y < 394:
                        pygame.display.update()
                        if level_key >= 4:
                            if gameplay(screen, clock, 'level_4.txt') \
                                    and level_key == 4:
                                level_key = 5
                        else:
                            locked(screen)
                            clock.tick(FPS)
                    if x > 475 and x < 620 and y > 50 and y < 94:
                        pygame.display.update()
                        if level_key >= 5:
                            if gameplay(screen, clock, 'level_5.txt') \
                                    and level_key == 5:
                                level_key = 6
                        else:
                            locked(screen)
                            clock.tick(FPS)
                    if x > 475 and x < 620 and y > 150 and y < 194:
                        pygame.display.update()
                        if level_key >= 6:
                            if gameplay(screen, clock, 'level_6.txt') \
                                    and level_key == 6:
                                level_key = 7
                        else:
                            locked(screen)
                            clock.tick(FPS)
                    if x > 475 and x < 620 and y > 250 and y < 294:
                        pygame.display.update()
                        if level_key >= 7:
                            if gameplay(screen, clock, 'level_7.txt') \
                                    and level_key == 7:
                                level_key = 8
                        else:
                            locked(screen)
                            clock.tick(FPS)
                    if x > 475 and x < 620 and y > 350 and y < 394:
                        pygame.display.update()
                        if level_key >= 8:
                            if gameplay(screen, clock, 'level_8.txt') \
                                    and level_key == 8:
                                level_key = 9
                        else:
                            locked(screen)
                            clock.tick(FPS)
            pygame.display.update()
            file_key = open('level_key.txt', 'w')
            file_key.write(str(level_key))
            file_key.close()


def music_draw(screen):
    """function draws settings of the game, where we can turn on/off
    the music"""
    forest_surf = pygame.image.load('forest.jpg')
    forest_rect = forest_surf.get_rect(
        bottomright=(width, length))
    screen.blit(forest_surf, forest_rect)
    file = open('button_color.txt', 'r')
    button_0 = file.read()
    color_off, color_on = button_0.split()
    if int(color_on) == 1:
        color_on = WHITE
    else:
        color_on = GREY
    if int(color_off) == 1:
        color_off = WHITE
    else:
        color_off = GREY
    file.close()
    md_1 = font.render('OFF', True, BLACK, color_off)
    screen.blit(md_1, (270, 50))
    md_2 = font.render('ON', True, BLACK, color_on)
    screen.blit(md_2, (360, 50))
    md_3 = font.render('Music', True, BLACK, WHITE)
    screen.blit(md_3, (140, 50))
    tlevel_2 = font.render('BACK', True, BLACK, WHITE)
    screen.blit(tlevel_2, (345, 545))
    t_1 = font.render('Developers:', True, BLACK, WHITE)
    screen.blit(t_1, (140, 375))
    t_2 = font.render('Bugrova Alice', True, BLACK, SLIGHT_GREY)
    screen.blit(t_2, (140, 430))
    t_3 = font.render('Nurysheva Alina', True, BLACK, SLIGHT_GREY)
    screen.blit(t_3, (140, 485))


def music_choice(screen):
    """function creates new setting display, where we can select
    music parameter"""
    finishedm = False
    while not finishedm:
        music_draw(screen)
        for m in pygame.event.get():
            if m.type == pygame.QUIT:
                sys.exit()
            if m.type == pygame.MOUSEBUTTONDOWN:
                if m.button == 1:
                    x_m, y_m = m.pos
                    if x_m > 345 and x_m < 445 and y_m > 545 and y_m < 590:
                        pygame.display.update()
                        finishedm = True
                    if x_m > 270 and x_m < 353 and y_m > 50 and y_m < 94:
                        file = open('button_color.txt', 'w')
                        file.write('1 0')
                        file.close()
                        pygame.mixer.music.pause()
                    if x_m > 360 and x_m < 424 and y_m > 50 and y_m < 94:
                        file = open('button_color.txt', 'w')
                        file.write('0 1')
                        file.close()
                        pygame.mixer.music.play()
                    pygame.display.update()
        pygame.display.update()


def locked(screen):
    """function displays if we don't have an access to a level"""
    tlocked = font.render('Locked!', True, WHITE, BLACK)
    a = 1000
    while a > 0:
        screen.blit(tlocked, (330, 300))
        a -= 1
        pygame.display.update()


# started a game menu
file = open('button_color.txt', 'r')
button = file.read()
off, on = button.split()
pygame.mixer.music.load('Jungle.mp3')
if int(on):
    pygame.mixer.music.play()
else:
    pygame.mixer.music.pause()
initial_display_draw(screen)
while not finished:
    clock.tick(FPS)
    in_scr_choice(screen)
pygame.quit()
