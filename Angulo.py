import pygame
import numpy as np
from Game import Objeto, Foguete, Game, Jogador

class Angulo():

    def __init__(self):    

        self.jogo = Game()
        self.obstaculo_1 = Objeto()
        self.obstaculo_2 = Objeto()
        self.astronauta = Foguete()
        self.jogador_1 = Jogador()
        self.jogador_2 = Jogador()
        self.jogador_3 = Jogador()
        self.jogador_4 = Jogador()

        self.movimento_iniciado = False

        self.jogador_1.x = 890
        self.jogador_1.y = 100
        self.jogador_1.largura = 50
        self.jogador_1.altura = 200

        self.jogador_2.x = 890
        self.jogador_2.y = 30
        self.jogador_2.largura = 50
        self.jogador_2.altura = 50

        self.jogador_3.x = 890
        self.jogador_3.y = 320
        self.jogador_3.largura = 50
        self.jogador_3.altura = 50

        self.jogador_4.x = 890
        self.jogador_4.y = 100
        self.jogador_4.largura = 50
        self.jogador_4.altura = 10

        self.obstaculo_1.x = self.jogo.screenSize[0] / 2
        self.obstaculo_1.y = 0
        self.obstaculo_1.largura = 50
        self.obstaculo_1.altura = 230

        self.obstaculo_2.largura = 50
        self.obstaculo_2.altura = 400
        self.obstaculo_2.x = self.jogo.screenSize[0] / 2
        self.obstaculo_2.y = self.jogo.screenSize[1] - self.obstaculo_2.altura

        self.astronauta.x_inicial = 70
        self.astronauta.y_inicial = self.jogo.screenSize[1] - 70

        self.astronauta.x = self.astronauta.x_inicial
        self.astronauta.y = self.astronauta.y_inicial

        self.astronauta.alfa = 60 * (np.pi / 180)

        self.astronauta.vel_inicial = (1 / self.jogo.fps) * 100
        self.astronauta.vel_y = self.astronauta.vel_inicial * np.sin(self.astronauta.alfa)
        self.astronauta.vel_x = self.astronauta.vel_inicial * np.cos(self.astronauta.alfa)

        self.initGame() # inicializa o jogo

    def initGame(self):

        '''
            Função responsável por inicializar e configurar a tela do jogo,
            essa função não possui parâmetros
        '''
    
        self.jogo.screen = pygame.display.set_mode(self.jogo.screenSize)
        self.jogo.title = "Fase 3"
        pygame.display.set_caption(self.jogo.title)

        if(self.jogo.icon != None):
            pygame.display.set_icon(self.jogo.icon)

        self.jogo.gameClock = pygame.time.Clock()

    def gameMain(self):

        '''
            Loop principal do jogo, essa função não possui parâmetros
        '''

        while self.jogo.gameRunning:

            self.jogo.screen.fill((128,128,128))
            self.jogo.deltaTime = self.jogo.gameClock.tick(self.jogo.fps)

            for event in pygame.event.get():
                self.gameEvent(event)

            self.gameUpdate()
            self.jogo.gameImage()
            self.jogo.angulo_Image()
            self.gameRender()

            if(self.movimento_iniciado == False):
                for event in pygame.event.get():

                   if (event.type == pygame.KEYDOWN):
                       if (event.key == pygame.K_a):
                          self.jogador_4.altura = self.jogador_4.altura + 10
                          self.astronauta.alfa = self.astronauta.alfa + 5 * (np.pi / 180)
                          self.astronauta.vel_y = self.astronauta.vel_inicial * np.sin(self.astronauta.alfa)
                          self.astronauta.vel_x = self.astronauta.vel_inicial * np.cos(self.astronauta.alfa)
                      
                       if (event.key == pygame.K_d):
                          self.jogador_4.altura = self.jogador_4.altura - 10
                          self.astronauta.alfa = self.astronauta.alfa - 5 * (np.pi / 180)
                          self.astronauta.vel_y = self.astronauta.vel_inicial * np.sin(self.astronauta.alfa)
                          self.astronauta.vel_x = self.astronauta.vel_inicial * np.cos(self.astronauta.alfa)
                      
                if (self.jogador_4.altura >  self.jogador_1.altura):
                        self.jogador_4.altura = 10

            pygame.display.update()

        pygame.quit()

    def gameEvent(self, event):

        '''
            Função responsável por gerenciar os eventos do display event 
        '''

        if(event.type == pygame.QUIT):
            self.jogo.gameRunning = False

        if(event.type == pygame.KEYDOWN):

            if(event.key == pygame.K_ESCAPE):
                self.jogo.gameRunning = False
            elif(event.key == pygame.K_SPACE):
                self.movimento_iniciado = True

    '''
        def gameReset(self):

            start_message = gameFont.render("Aperte a tecla 'E' para iniciar o lançamento", 1, (255,255,255))
            screen.blit(start_message, (screenSize[0] / 2 - start_message.get_width() , screenSize[1] / 3))
    '''

    def gameUpdate(self):

        '''
            Função responsável por atualizar a lógica do jogo
        '''

        if(self.movimento_iniciado == True):
            # movimento na horizontal (M.R.U)
            self.astronauta.x = self.astronauta.x + self.astronauta.vel_x * self.jogo.deltaTime

            # movimento na vertical (M.U.V)
            self.astronauta.vel_y = self.astronauta.vel_y - self.astronauta.g * self.jogo.deltaTime
            self.astronauta.y = self.astronauta.y - self.astronauta.vel_y * self.jogo.deltaTime

        # cria rect do jogador, máquina e da bola para utilizar com a função colliderect do módulo Rect
        rectastronauta = pygame.Rect((self.astronauta.x - self.astronauta.raio, self.astronauta.y - self.astronauta.raio, 2 * self.astronauta.raio, 2 * self.astronauta.raio))
        rectobstaculo_1 = pygame.Rect((self.obstaculo_1.x, self.obstaculo_1.y, self.obstaculo_1.largura, self.obstaculo_1.altura))
        rectobstaculo_2 = pygame.Rect((self.obstaculo_2.x, self.obstaculo_2.y, self.obstaculo_2.largura, self.obstaculo_2.altura))

        if (self.astronauta.last_vel_x != self.astronauta.vel_x or self.astronauta.last_vel_y != self.astronauta.vel_y):

            # verifica se o astronauta colidiu com o obstáculo
            if(pygame.Rect.colliderect(rectastronauta, rectobstaculo_1) or pygame.Rect.colliderect(rectastronauta, rectobstaculo_2)):
                self.movimento_iniciado = False
                self.astronauta.vel_y = self.astronauta.vel_inicial * np.sin(self.astronauta.alfa)
                self.astronauta.vel_x = self.astronauta.vel_inicial * np.cos(self.astronauta.alfa)
                self.astronauta.x = self.astronauta.x_inicial
                self.astronauta.y = self.astronauta.y_inicial

        # salva a direção que o astronauta está indo
        self.astronauta.dir_x = self.astronauta.vel_x
        self.astronauta.dir_y = -self.astronauta.vel_y

        # normalização do vetor direção
        if(self.astronauta.dir_x != 0 and self.astronauta.dir_y != 0):
            tmp_normal = np.sqrt(np.power(self.astronauta.dir_x, 2) + np.power(self.astronauta.dir_y, 2))

            self.astronauta.dir_x = self.astronauta.dir_x / tmp_normal
            self.astronauta.dir_y = self.astronauta.dir_y / tmp_normal

        if (self.astronauta.x > 1024 or self.astronauta.x < 0 or self.astronauta.y < 0 or self.astronauta.y > 768):
             self.movimento_iniciado = False
             self.astronauta.vel_y = self.astronauta.vel_inicial * np.sin(self.astronauta.alfa)
             self.astronauta.vel_x = self.astronauta.vel_inicial * np.cos(self.astronauta.alfa)
             self.astronauta.x = self.astronauta.x_inicial
             self.astronauta.y = self.astronauta.y_inicial

    def gameRender(self):

        '''
            Função responsável por desenhar na tela do jogo
        '''
        # desenha o botao do jogador
        pygame.draw.rect(self.jogo.screen, (255, 255, 0), (self.jogador_1.x, self.jogador_1.y, self.jogador_1.largura, self.jogador_1.altura))
        pygame.draw.rect(self.jogo.screen, (255, 0, 255), (self.jogador_2.x, self.jogador_2.y, self.jogador_2.largura, self.jogador_2.altura))
        pygame.draw.rect(self.jogo.screen, (255, 0, 255), (self.jogador_3.x, self.jogador_3.y, self.jogador_3.largura, self.jogador_3.altura))
        pygame.draw.rect(self.jogo.screen, (0, 0, 0), (self.jogador_4.x, self.jogador_4.y, self.jogador_4.largura, self.jogador_4.altura))
        
        # desenha o astronauta
        pygame.draw.circle(self.jogo.screen, (0, 0, 0), (self.astronauta.x, self.astronauta.y), self.astronauta.raio)

        # desenha o objeto_1
        pygame.draw.rect(self.jogo.screen, (255, 255, 255), (self.obstaculo_1.x, self.obstaculo_1.y, self.obstaculo_1.largura, self.obstaculo_1.altura))

        # desenha a objeto_2
        pygame.draw.rect(self.jogo.screen, (255, 255, 255), (self.obstaculo_2.x, self.obstaculo_2.y, self.obstaculo_2.largura, self.obstaculo_2.altura))
       
        # desenha uma linha indicando a direção
        pygame.draw.line(self.jogo.screen, (255, 255, 255), (self.astronauta.x, self.astronauta.y), 
            (
                (self.astronauta.x + self.astronauta.dir_x * self.astronauta.raio * 3), 
                (self.astronauta.y + self.astronauta.dir_y * self.astronauta.raio * 3)
            ))               
