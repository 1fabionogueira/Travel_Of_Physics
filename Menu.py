import pygame
from Explore import Explorar
from Angulo import Angulo
from VariaVelocidade import VariaVelocidade
from VelAngulo import VelAngulo

class MainMenu():

    def __init__(self, screenSize = (1280, 768), fps=100, title='Menu', icon=None):
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
        self.titleFont = pygame.font.SysFont("Roboto", 75)
        self.menuFont = pygame.font.SysFont("Roboto", 45)

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def main_menu(self):
        while self.menuRunning:

            self.menuClock.tick(self.fps)
            self.screen.fill((15, 15, 15))

            for event in pygame.event.get():
                self.menuEvent(event)

            self.menuRender()
            
            mx, my = pygame.mouse.get_pos()

            if self.button_2.collidepoint((mx, my)):
                if self.click:
                    self.fase2(event)

            if self.button_1.collidepoint((mx, my)):
                if self.click:
                    self.fase1(event)

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

        if(event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 1:
                self.click = True

    
    def fase1(self, event):

        running = True
        while running:

            variavelocidade = VariaVelocidade()
            variavelocidade.initGame()
            variavelocidade.gameMain()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()
            self.menuClock.tick(self.fps)

    def fase2(self, event):

        running = True
        while running:
            
            angulo = Angulo()
            angulo.initGame()
            angulo.gameMain()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()
            self.menuClock.tick(self.fps)
    
    def fase3(self, event):

        running = True
        while running:

            velangulo = VelAngulo()
            velangulo.initGame()
            velangulo.gameMain()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()
            self.menuClock.tick(self.fps)
        
    def fase4(self, event):

        running = True
        while running:

            explore = Explorar()
            explore.initGame()
            explore.gameMain()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()
            self.menuClock.tick(self.fps)

    def menuRender(self):
        '''
            Função responsável por renderizar os botões e textos do Main Menu
        '''

        WHITE = (255, 255, 255)
        BLUEISH = (30, 30, 160)

        menuPrincipal = self.titleFont.render('Travel Of Physics', 1, (WHITE))
        Fase1 = self.menuFont.render('Variando a Velocidade', 1, (WHITE))
        Fase2 = self.menuFont.render('Variando o Ângulo', 1, (WHITE))
        Fase3 = self.menuFont.render('Velocidade e Ângulo', 1, (WHITE))
        Fase4 = self.menuFont.render('Explore', 1, (WHITE))
        
        self.button_1 = pygame.Rect((self.screenSize[0] / 2 - 0.5 * Fase1.get_width()) - 10, 200, Fase1.get_width() + 20, 50)
        self.button_2 = pygame.Rect((self.screenSize[0] / 2 - 0.5 * Fase2.get_width()) - 10, 300, Fase2.get_width() + 20, 50)
        self.button_3 = pygame.Rect((self.screenSize[0] / 2 - 0.5 * Fase3.get_width()) - 10, 400, Fase3.get_width() + 20, 50)
        self.button_4 = pygame.Rect((self.screenSize[0] / 2 - 0.5 * Fase4.get_width()) - 10, 500, Fase4.get_width() + 20, 50)

        pygame.draw.rect(self.screen, (BLUEISH), self.button_1)
        pygame.draw.rect(self.screen, (BLUEISH), self.button_2)
        pygame.draw.rect(self.screen, (BLUEISH), self.button_3)
        pygame.draw.rect(self.screen, (BLUEISH), self.button_4)

        self.draw_text('Travel Of Physics', self.titleFont, (WHITE), self.screen, (self.screenSize[0] - 2 * menuPrincipal.get_width()), 20)
        self.draw_text('Variando a Velocidade', self.menuFont, (WHITE), self.screen, ((self.screenSize[0] / 2) - 0.5 * Fase1.get_width()), 212.5)
        self.draw_text('Variando o Ângulo', self.menuFont, (WHITE), self.screen, ((self.screenSize[0] / 2) - 0.5 * Fase2.get_width()), 312.5)
        self.draw_text('Velocidade e Ângulo', self.menuFont, (WHITE), self.screen, ((self.screenSize[0] / 2) - 0.5 * Fase3.get_width()), 412.5)
        self.draw_text('Explore', self.menuFont, (WHITE), self.screen, ((self.screenSize[0] / 2) - 0.5 * Fase4.get_width()), 512.5)

menu = MainMenu()
menu.main_menu()