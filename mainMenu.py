from Game import Game

import pygame, sys
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Menu')
screen = pygame.display.set_mode((1024, 768), 0, 32)

font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
def draw_button(text, font, color, surface, x, y):
    butobj = font.render(text, 1, color)
    butrect = butobj.get_rect()
    butrect.center = (x, y)
    surface.blit(butobj, butrect)

click = False

def main_menu():
    while True:

        screen.fill((128, 128, 128))
        draw_text('Menu Principal', font, (255, 255, 255), screen, 20, 20)
        
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)
        button_4 = pygame.Rect(50, 400, 200, 50)
        button_5 = pygame.Rect(50, 500, 200, 50)
    
        if button_1.collidepoint((mx, my)):
            if click:
                fase1()
        if button_2.collidepoint((mx, my)):
            if click:
                fase2()
        if button_3.collidepoint((mx, my)):
            if click:
                fase3()
        if button_4.collidepoint((mx, my)):
            if click:
                fase4()
        if button_5.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 128, 34), button_1)
        pygame.draw.rect(screen, (255, 128, 34), button_2)
        pygame.draw.rect(screen, (255, 128, 34), button_3)
        pygame.draw.rect(screen, (255, 128, 34), button_4)
        pygame.draw.rect(screen, (255, 128, 34), button_5)
        draw_text('Fase 1: Queda Livre', font, (255, 255, 255), screen, 50, 100)
        draw_text('Fase 2: Lançamento Vertical', font, (255, 255, 255), screen, 50, 200)
        draw_text('Fase 3: Lançamento Horizontal', font, (255, 255, 255), screen, 50, 300)
        draw_text('Fase 4: Lançamento Oblíquo', font, (255, 255, 255), screen, 50, 400)
        draw_text('Opções', font, (255, 255, 255), screen, 50, 500)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        mainClock.tick(60)

def fase1():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Fase 1: Queda Livre', font, (255, 255, 255), screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)


def fase2():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Fase 2: Lançamento Vertical', font, (255, 255, 255), screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)

def fase3():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Fase 3: Lançamento Horizontal', font, (255, 255, 255), screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)

def fase4():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Fase 4: Lançamento Oblíquo', font, (255, 255, 255), screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Opções', font, (255, 255, 255), screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)

main_menu()