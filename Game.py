from pygame.image import load
from pygame.transform import scale
from os.path import join 

class Objeto():

    '''
        Define a classe do Objeto, atribuindo valores genéricos
        aos parâmetros
    '''

    x = 0
    y = 0

    largura = 0
    altura = 0

class Foguete():

    '''
        Define a classe do Astronauta, atribuindo valores genéricos
        aos parâmetros
    '''

    x_inicial = 0
    y_inicial = 0

    x = 0
    y = 0

    raio = 15

    vel_inicial = 0
    vel_x = 0
    vel_y = 0

    dir_x = 0
    dir_y = 0

    last_vel_x = 0
    last_vel_y = 0

    # ângulo de abertura do canhão (°)
    alfa = 0

    # gravidade (m/s²)
    g = 9.80665 / (100 ** 2)

class Jogador():

    '''
       Classe responsável por poder alterar variavel
    '''
    x = 0
    y = 0
    largura = 0
    altura = 0

class Game():

    '''
        Classe reponsável por gerenciar o jogo
    '''

    def __init__(self, screenSize = (1280, 720), fps=100, title ='', icon=None):

        self.gameRunning = True

        self.screenSize = screenSize # Define o Tamanho da tela
        self.fps = fps # Quantidade de frames por segundo
        self.title = title # Nome do jogo
        self.icon = icon # ícone do jogo 

    def draw_text(self, text, font, color, surface, x, y):

        '''
            Função responsável por escrever na tela
        '''
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    
    def gameImage(self):

        '''
            Função responsável por renderizar e colocar a imagem no jogo
        '''

        # Imagem do canhão
        canhão_largura, canhão_altura = 100, 100
        canhão_image = load(join('assets/cannon.png'))
        canhão = scale(canhão_image, (canhão_largura, canhão_altura))

        self.screen.blit(canhão, (0, self.screenSize[1] - canhão_altura))