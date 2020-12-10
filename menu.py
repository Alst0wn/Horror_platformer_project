import pygame.draw
import sys
from main import *

pygame.init()
font = pygame.font.Font(None, 60)
font1 = pygame.font.Font(None, 30)
FPS = 30
width = 800
length = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# creating display
screen = pygame.display.set_mode((width, length))
clock = pygame.time.Clock()
finished = False

def menu(screen):
    pygame.mixer.music.load('Jungle.mp3')
    pygame.mixer.music.play()
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
    tlevel_5 = font.render('Level 5', True, BLACK, WHITE)
    screen.blit(tlevel_5, (175, 450))
    tlevel_6 = font.render('Level 6', True, BLACK, WHITE)
    screen.blit(tlevel_6, (475, 50))
    tlevel_7 = font.render('Level 7', True, BLACK, WHITE)
    screen.blit(tlevel_7, (475, 150))
    tlevel_8 = font.render('Level 8', True, BLACK, WHITE)
    screen.blit(tlevel_8, (475, 250))
    tlevel_9 = font.render('Level 9', True, BLACK, WHITE)
    screen.blit(tlevel_9, (475, 350))
    tlevel_10 = font.render('Level 10', True, BLACK, WHITE)
    screen.blit(tlevel_10, (475, 450))
    tsettings = font.render('Settings', True, BLACK, WHITE)
    screen.blit(tsettings, (300, 525))


def quit_draw():
    tquit = font.render('Quit', True, WHITE, BLACK)
    screen.blit(tquit, (700, 0))


def quit_check(event, screen):
    x, y = event
    if x > 700 and x < 790 and y > 0 and y < 44:
        menu(screen)


def menu_choice(screen):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                x, y = i.pos
                if x > 175 and x < 320 and y > 50 and y < 94:
                    #pygame.mixer.music.pause()
                    pygame.display.update()
                    gameplay(screen, clock, 'level_1.txt')
                if x > 175 and x < 320 and y > 150 and y < 194:
                    #pygame.mixer.music.pause()
                    pygame.display.update()
                    gameplay(screen, clock, 'level_2.txt')
                if x > 175 and x < 320 and y > 250 and y < 294:
                    #pygame.mixer.music.pause()
                    pygame.display.update()
                    gameplay(screen, clock, 'level_3.txt')
                if x > 175 and x < 320 and y > 350 and y < 394:
                    #pygame.mixer.music.pause()
                    pygame.display.update()
                    gameplay(screen, clock, 'level_4.txt')
                if x > 175 and x < 320 and y > 450 and y < 494:
                    #pygame.mixer.music.pause()
                    pygame.display.update()
                    gameplay(screen, clock, 'level_5.txt')
                if x > 475 and x < 620 and y > 50 and y < 94:
                    #pygame.mixer.music.pause()
                    pygame.display.update()
                    gameplay(screen, clock, 'level_6.txt')
                if x > 475 and x < 620 and y > 150 and y < 194:
                    #pygame.mixer.music.pause()
                    pygame.display.update()
                    gameplay(screen, clock, 'level_7.txt')
                if x > 475 and x < 620 and y > 250 and y < 294:
                    #pygame.mixer.music.pause()
                    pygame.display.update()
                    gameplay(screen, clock, 'level_8.txt')
                if x > 475 and x < 620 and y > 350 and y < 394:
                    #pygame.mixer.music.pause()
                    pygame.display.update()
                    gameplay(screen, clock, 'level_9.txt')
                if x > 475 and x < 620 and y > 450 and y < 494:
                    #pygame.mixer.music.pause()
                    pygame.display.update()
                    gameplay(screen, clock, 'level_10.txt')
                if x > 300 and x < 475 and y > 525 and y < 569:
                    quit_draw()
                    #pygame.mixer.music.pause()
                    pygame.display.update()
                quit_check(i.pos, screen)
                pygame.display.update()
    pygame.display.update()


menu(screen)
while not finished:
    clock.tick(FPS)
    menu_choice(screen)
pygame.quit()
