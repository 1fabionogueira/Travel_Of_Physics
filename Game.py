import pygame
import numpy as np
import os

screenSize = (1280, 720)

screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption('Protótipo')

pygame.font.init()

gamefont = pygame.font.SysFont('Arial', 35)

gameClock = pygame.time.Clock()

FPS = 100

g = 0.001 
alfa = 58 * np.pi / 180

##############################################

class Gobjeto:
    x = 0
    y = 0

    largura = 0
    altura = 0

obstaculo_1 = Gobjeto()
obstaculo_2 = Gobjeto()

###### obstáculo 1 ######

obstaculo_1.x = screenSize[0] / 2
obstaculo_1.y = 0
obstaculo_1.largura = 40
obstaculo_1.altura = 220

###### obstáculo 2 ######

obstaculo_2.largura = 40
obstaculo_2.altura = 460
obstaculo_2.x = screenSize[0] / 2
obstaculo_2.y = screenSize[1] - obstaculo_2.altura

################################################

class Gastronauta:
    vel_x = 0
    vel_y = 0
    vel_inicial = 0

    raio = 0

    x_inicial = 0
    y_inicial = 0
    x = 0
    y = 0

astronauta = Gastronauta()

astronauta.raio = 15

astronauta.x_inicial = 70
astronauta.y_inicial = screenSize[1] - 70

astronauta.x = astronauta.x_inicial
astronauta.y = astronauta.y_inicial

astronauta.vel_inicial = (1 / FPS) * 100
astronauta.vel_y = astronauta.vel_inicial * np.sin(alfa)
astronauta.vel_x = astronauta.vel_inicial * np.cos(alfa)

##############################################

## imagem do canhão
canhão_largura, canhão_altura = 100, 100
canhão_image = pygame.image.load(os.path.join('Projeto_Semestre/assets', 'cannon.png'))
canhão = pygame.transform.scale(canhão_image, (canhão_largura, canhão_altura))

##############################################

def gameMain():
    gameRunning = True

    while gameRunning:
        screen.fill((128, 128, 128))

        screen.blit(canhão, (0, screenSize[1] - canhão_altura))

        deltaTime = gameClock.tick(FPS)

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                gameRunning = False
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    gameRunning = False

        update(deltaTime)
        render(deltaTime)

        pygame.display.update()

    pygame.quit()

def update(deltaTime):

    # movimento horizontal
    astronauta.x = astronauta.x + astronauta.vel_x * deltaTime

    # movimento vertical 
    astronauta.vel_y = astronauta.vel_y - g * deltaTime
    astronauta.y = astronauta.y - astronauta.vel_y * deltaTime

    # cria rect do jogador, máquina e da bola para utilizar com a função colliderect do módulo Rect
    rectastronauta = pygame.Rect((astronauta.x - astronauta.raio, astronauta.y + astronauta.raio, 2 * astronauta.raio, 2 * astronauta.raio))
    rectobstaculo_1 = pygame.Rect((obstaculo_1.x, obstaculo_1.y, obstaculo_1.largura, obstaculo_1.altura))
    rectobstaculo_2 = pygame.Rect((obstaculo_2.x, obstaculo_2.y, obstaculo_2.largura, obstaculo_2.altura))

    # verifica se o astronauta colidiu com o obstáculo
    if(pygame.Rect.colliderect(rectastronauta, rectobstaculo_1) or pygame.Rect.colliderect(rectastronauta, rectobstaculo_2)):
        astronauta.vel_x = 0 * astronauta.vel_x

    # verifica as colisões do astronauta no obstáculo (reverte a velocidade_x se ocorrer colisão, ou seja, faz um espelhamento em relação a horizontal)
    if(astronauta.x >= screenSize[0] - 2 * astronauta.raio or astronauta.x <= 0 + 2 * astronauta.raio):
        astronauta.vel_x = 0 * astronauta.vel_x

    # if(astronauta.y >= screenSize[1] - astronauta.raio):
        # astronauta.vel_y = (-1) * astronauta.vel_y * .70

def render(deltaTime):

    # criar objetos
    pygame.draw.rect(screen, (255, 255, 255), (obstaculo_1.x, obstaculo_1.y, obstaculo_1.largura, obstaculo_1.altura), border_bottom_left_radius = 20, border_bottom_right_radius = 20)
    pygame.draw.rect(screen, (255, 255, 255), (obstaculo_2.x, obstaculo_2.y, obstaculo_2.largura, obstaculo_2.altura), border_top_left_radius = 20, border_top_right_radius = 20)
    pygame.draw.circle(screen, (0, 0, 0), (astronauta.x, astronauta.y), astronauta.raio)
    

gameMain()