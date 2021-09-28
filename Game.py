import pygame
import math
import os

class Game():
    '''
        Classe reposnsável por gerenciar o jogo
    '''

    def __init__(self, screenSize = (800, 600), fps=60, title='Travel Of Physics', icon=None):

        self.gameRunning = True

        self.screenSize = screenSize
        self.fps = fps
        self.title = title
        self.icon = icon

        self.initGame()

    def loadSpriteSheetPacket(self):
        pass

    def loadImagePacket(self):
        pass

    def initGame(self):

        '''
            Função responsáveç por inicializar e configurar a tela do jogo,
            essa função não possui parâmetros
        '''
        
        self.screen = pygame.display.set_mode(self.screenSize)
        pygame.display.set_caption(self.title)

        if(self.icon != None):
            pygame.display.set_icon(self.icon)

        self.gameClock = pygame.time.Clock()


    def gameMain(self):
        '''
            Loop principal do jogo, essa função não possui parâmetros
        '''

        while self.gameRunning:
            self.deltaTime = self.gameClock.tick(self.fps)

            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                self.gameEvent(event)

            self.gameUpdate()
            self.gameRender()

            pygame.display.update()

        pygame.quit()

    def gameEvent(self, event):
        '''
            Função responsável por gerenciar os eventos do display
            event -> contém a estrutura do evento (veja a documentação do pygame
            para mais detalhes)
        '''

        if(event.type == pygame.QUIT):
            self.gameRunning = False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_ESCAPE):
                self.gameRunning = False

    def gameUpdate(self):
        '''
            Função responsável por atualizar a lógica do jogo
        '''

        pass

    def gameRender(self):
        '''
            Função responsável por desenhar na tela do jogo
        '''

        pass

game = Game()
game.gameMain()




