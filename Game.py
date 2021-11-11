import pygame
import numpy as np
import math
import os

class Objeto():

    '''
        Define a classe do Objeto, atribuindo valores genéricos
        aos parâmetros
    '''

    x = 0
    y = 0

    largura = 0
    altura = 0

class Astronauta():

    '''
        Define a classe do Astronauta, atribuindo valores genéricos
        aos parâmetros
    '''

    x_inicial = 0
    y_inicial = 0

    x = 0
    y = 0

    raio = 0

    vel_inicial = 0
    vel_x = 0
    vel_y = 0

    dir_x = 0
    dir_y = 0

    last_vel_x = 0
    last_vel_y = 0


class Game():

    '''
        Classe reponsável por gerenciar o jogo
    '''

    def __init__(self, screenSize = (1024, 768), fps=100, title='alfa', icon=None):

        self.gameRunning = True

        self.screenSize = screenSize # Define o Tamanho da tela
        self.fps = fps # Quantidade de frames por segundo
        self.title = title # Nome do jogo
        self.icon = icon # ícone do jogo

        self.initGame() # inicializa o jogo

        # ângulo de abertura do canhão (°)
        self.alfa = 60 * np.pi / 180

        # Define o obstaculo_1 como objeto da classe Objeto 

        self.obstaculo_1 = Objeto()

        self.obstaculo_1.x = self.screenSize[0] / 2
        self.obstaculo_1.y = 0
        self.obstaculo_1.largura = 20
        self.obstaculo_1.altura = 230

        # Define o obstaculo_2 como objeto da classe Objeto
         
        self.obstaculo_2 = Objeto()

        self.obstaculo_2.largura = 20
        self.obstaculo_2.altura = 400
        self.obstaculo_2.x = self.screenSize[0] / 2
        self.obstaculo_2.y = self.screenSize[1] - self.obstaculo_2.altura

        # Define-se astronauta como objeto da classe Astronauta

        self.astronauta = Astronauta()

        self.astronauta.raio = 15

        self.astronauta.x_inicial = 70
        self.astronauta.y_inicial = self.screenSize[1] - 70

        self.astronauta.x = self.astronauta.x_inicial
        self.astronauta.y = self.astronauta.y_inicial

        self.astronauta.vel_inicial = (1 / self.fps) * 108
        self.astronauta.vel_y = self.astronauta.vel_inicial * np.sin(self.alfa)
        self.astronauta.vel_x = self.astronauta.vel_inicial * np.cos(self.alfa)


    def loadSpriteSheetPacket(self):
        pass

    def loadImagePacket(self):
        pass

    def initGame(self):

        '''
            Função responsável por inicializar e configurar a tela do jogo,
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

            self.screen.fill((128,128,128))
            self.deltaTime = self.gameClock.tick(self.fps)

            for event in pygame.event.get():
                self.gameEvent(event)

            self.gameUpdate()
            self.gameRender()

            pygame.display.update()

        pygame.quit()

    def gameEvent(self, event):

        '''
            Função responsável por gerenciar os eventos do display
            event -> contém a estrutura do evento (veja a documentação 
            do pygame para mais detalhes)
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

        # gravidade (m/s²)
        self.g = (1 / self.deltaTime ** 2) * 0.11

        # movimento horizontal
        self.astronauta.x = self.astronauta.x + self.astronauta.vel_x * self.deltaTime

        # movimento vertical 
        self.astronauta.vel_y = self.astronauta.vel_y - self.g * self.deltaTime
        self.astronauta.y = self.astronauta.y - self.astronauta.vel_y * self.deltaTime

        # cria rect do jogador, máquina e da bola para utilizar com a função colliderect do módulo Rect
        rectastronauta = pygame.Rect((self.astronauta.x - self.astronauta.raio, self.astronauta.y - self.astronauta.raio, 2 * self.astronauta.raio, 2 * self.astronauta.raio))
        rectobstaculo_1 = pygame.Rect((self.obstaculo_1.x, self.obstaculo_1.y, self.obstaculo_1.largura, self.obstaculo_1.altura))
        rectobstaculo_2 = pygame.Rect((self.obstaculo_2.x, self.obstaculo_2.y, self.obstaculo_2.largura, self.obstaculo_2.altura))

        if self.astronauta.last_vel_x != self.astronauta.vel_x or self.astronauta.last_vel_y != self.astronauta.vel_y:

            # verifica se o astronauta colidiu com o obstáculo
            if(pygame.Rect.colliderect(rectastronauta, rectobstaculo_1) or pygame.Rect.colliderect(rectastronauta, rectobstaculo_2)):
                self.astronauta.vel_x = -.75 * self.astronauta.vel_x
                self.astronauta.last_vel_x = self.astronauta.vel_x

            # verifica as colisões do astronauta no obstáculo (reverte a velocidade_x se ocorrer colisão, ou seja, faz um espelhamento em relação a horizontal)
            if(self.astronauta.x >= self.screenSize[0] - 2 * self.astronauta.raio or self.astronauta.x <= 0 + 2 * self.astronauta.raio):
                self.astronauta.vel_x = -.75 * self.astronauta.vel_x
                self.astronauta.last_vel_x = self.astronauta.vel_x

        # if(astronauta.y >= screenSize[1] - astronauta.raio):
            # astronauta.vel_y = (-1) * astronauta.vel_y * .70

        keys = pygame.key.get_pressed()
 
        # salva a direção que o astronauta está indo
        self.astronauta.dir_x = self.astronauta.vel_x
        self.astronauta.dir_y = -self.astronauta.vel_y

        # normalização do vetor direção
        if(self.astronauta.dir_x != 0 and self.astronauta.dir_y != 0):
            tmp_normal = math.sqrt(math.pow(self.astronauta.dir_x, 2) + math.pow(self.astronauta.dir_y, 2))

            self.astronauta.dir_x = self.astronauta.dir_x / tmp_normal
            self.astronauta.dir_y = self.astronauta.dir_y / tmp_normal

    def gameRender(self):

        '''
            Função responsável por desenhar na tela do jogo
        '''
        
        # desenha o astronauta
        pygame.draw.circle(self.screen, (0, 0, 0), (self.astronauta.x, self.astronauta.y), self.astronauta.raio)

        # desenha o objeto_1
        pygame.draw.rect(self.screen, (255, 255, 255), (self.obstaculo_1.x, self.obstaculo_1.y, self.obstaculo_1.largura, self.obstaculo_1.altura))

        # desenha a objeto_2
        pygame.draw.rect(self.screen, (255, 255, 255), (self.obstaculo_2.x, self.obstaculo_2.y, self.obstaculo_2.largura, self.obstaculo_2.altura))
       
        # desenha uma linha indicando a direção
        pygame.draw.line(self.screen, (255, 255, 255), (self.astronauta.x, self.astronauta.y), 
            (
                (self.astronauta.x + self.astronauta.dir_x * self.astronauta.raio * 3), 
                (self.astronauta.y + self.astronauta.dir_y * self.astronauta.raio * 3)
            ))
    
        # Imagem do canhão
        canhão_largura, canhão_altura = 100, 100
        canhão_image = pygame.image.load(os.path.join('assets', 'cannon.png'))
        canhão = pygame.transform.scale(canhão_image, (canhão_largura, canhão_altura))

        self.screen.blit(canhão, (0, self.screenSize[1] - canhão_altura))

# Inicia o jogo
game = Game()
game.gameMain()