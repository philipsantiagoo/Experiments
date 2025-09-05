"""
    JOGO DA COBRINHA
"""

import pygame
import random


# iniciando o pygame
pygame.init()

# janela
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Jogo da cobrinha')

# posição inicial da cobra
cobra = [(100, 50)]
# direção inicial 
direcao = (10, 0)
# posição inical comida
comida = (300, 200)


def desenhar():
    # desenha a rela
    tela.fill((0, 0,0 ))

    # desenha a cobra na tela
    for parte in cobra:
        pygame.draw.rect(tela, color=(0, 255, 0), rect=(*parte, 10, 10))
    
    pygame.draw.rect(tela, color=(255, 0, 0), rect=(*comida, 10, 10))
    pygame.display.update()


rodando = True
relogio = pygame.time.Clock()


while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        # botões
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                direcao = (0, -10)
            elif evento.key == pygame.K_DOWN:
                direcao = (0, 10)
            elif evento.key == pygame.K_LEFT:
                direcao = (-10, 0)
            elif evento.key == pygame.K_RIGHT:
                direcao = (10, 0)
    
    nova_cabeca = (cobra[0][0] + direcao[0], cobra[0][1] + direcao[1])
    cobra.insert(0, nova_cabeca)
    
    # pega a comida
    if nova_cabeca == comida:
        comida = (random.randrange(0, 600, 10), random.randrange(0, 400, 10))
    else:
        cobra.pop()
    
    # colisões
    if nova_cabeca in cobra[1:]:
        rodando = False
    
    if nova_cabeca[0] < 0 or nova_cabeca[0] > 600:
        rodando = False
    
    if nova_cabeca[1] < 0 or nova_cabeca[1] > 400:
        rodando = False

    desenhar()
    relogio.tick(15)

pygame.quit()