import pygame
import sys
from pygame.locals import *
from lancamentoVertical import LancamentoVertical
from lancamentoHorizontal import LancamentoHorizontal
from lancamentoObliquo import LancamentoObliquo

class MainMenu():

    def __init__(self, screenSize = (1024, 768), fps=100, title='Menu', icon=None):
        self.menuRunning = True

        self.screenSize = screenSize # Define o Tamanho da tela
        self.fps = fps # Quantidade de frames por segundo
        self.title = title # Nome do jogo
        self.icon = icon # ícone do jogo

        self.initMenu()

    def initMenu(self):
        self.screen = pygame.display.set_mode(self.screenSize)
        pygame.display.set_caption(self.title)

        if(self.icon != None):
            pygame.display.set_icon(self.icon)
        
        self.menuClock = pygame.time.Clock()

        pygame.font.init()
        self.menuFont = pygame.font.SysFont("Roboto", 35)

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
        
    def draw_button(self, text, font, color, surface, x, y):
        butobj = font.render(text, 1, color)
        butrect = butobj.get_rect()
        butrect.center = (x, y)
        surface.blit(butobj, butrect)

    def main_menu(self):
        while self.menuRunning:

            self.menuClock.tick(self.fps)
            self.screen.fill((15, 15, 15))

            for event in pygame.event.get():
                self.menuEvent(event)

            self.menuRender()
            self.draw_text('Menu Principal', self.menuFont, (255, 255, 255), self.screen, 20, 20)
            
            mx, my = pygame.mouse.get_pos()
        
            if self.button_1.collidepoint((mx, my)):
                if self.click:
                    self.fase1(event)

            if self.button_2.collidepoint((mx, my)):
                if self.click:
                    self.fase2(event)

            if self.button_3.collidepoint((mx, my)):
                if self.click:
                    self.fase3(event)

            if self.button_4.collidepoint((mx, my)):
                if self.click:
                    self.fase4(event)

            self.click = False
            
            pygame.display.update()

        pygame.quit()

    def menuEvent(self, event):
        if(event.type == pygame.QUIT):
            self.menuRunning = False

        if(event.type == pygame.KEYDOWN):
            if(event.type == pygame.K_ESCAPE):
                self.menuRunning = False

        if(event.type == MOUSEBUTTONDOWN):
            if event.button == 1:
                self.click = True

    '''
    def fase1(self, event):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            self.menuClock.tick(self.fps)
    '''
            
    
    def fase2(self, event):
        running = True
        while running:

            lancamento_vertical = LancamentoVertical()
            lancamento_vertical.initGame()
            lancamento_vertical.gameMain()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            self.menuClock.tick(self.fps)
    

            
    
    def fase3(self, event):
        running = True
        while running:
            
            lancamento_horizontal = LancamentoHorizontal()
            lancamento_horizontal.initGame()
            lancamento_horizontal.gameMain()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            self.menuClock.tick(self.fps)
    
    def fase4(self, event):
        running = True
        while running:

            lancamento_obliquo = LancamentoObliquo()
            lancamento_obliquo.initGame()
            lancamento_obliquo.gameMain()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            self.menuClock.tick(self.fps)

    def menuRender(self):
        self.button_1 = pygame.Rect(40, 100, 400, 50)
        self.button_2 = pygame.Rect(40, 200, 400, 50)
        self.button_3 = pygame.Rect(40, 300, 400, 50)
        self.button_4 = pygame.Rect(40, 400, 400, 50)

        pygame.draw.rect(self.screen, (30, 30, 160), self.button_1)
        pygame.draw.rect(self.screen, (30, 30, 160), self.button_2)
        pygame.draw.rect(self.screen, (30, 30, 160), self.button_3)
        pygame.draw.rect(self.screen, (30, 30, 160), self.button_4)

        self.draw_text('Fase 1 - Queda Livre', self.menuFont, (255, 255, 255), self.screen, 50, 112.5)
        self.draw_text('Fase 2 - Lançamento Vertical', self.menuFont, (255, 255, 255), self.screen, 50, 212.5)
        self.draw_text('Fase 3 - Lançamento Horizontal', self.menuFont, (255, 255, 255), self.screen, 50, 312.5)
        self.draw_text('Fase 4 - Lançamento Oblíquo', self.menuFont, (255, 255, 255), self.screen, 50, 412.5)

menu = MainMenu()
menu.main_menu()
