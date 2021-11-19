import pygame

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

class Game():

    '''
        Classe reponsável por gerenciar o jogo
    '''

    def __init__(self, screenSize = (1024, 768), fps=100, title ='', icon=None):

        self.gameRunning = True

        self.screenSize = screenSize # Define o Tamanho da tela
        self.fps = fps # Quantidade de frames por segundo
        self.title = title # Nome do jogo
        self.icon = icon # ícone do jogo 