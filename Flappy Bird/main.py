import pygame
import random
import constantes


# inicializando
pygame.init()

tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))

# título
pygame.display.set_caption('Flappy Bird')

# fonte
fonte = pygame.font.SysFont('Arial', 36)

# clock
relogio = pygame.time.Clock()

# posições e velocidade
passaro_x = 50
passaro_y = constantes.ALTURA // 2
velocidade = 0

cano_x = constantes.LARGURA
cano_altura = random.randint(150, 450)


# pontos
pontos = 0
ja_contou_ponto = False

# controle
rodando = True


# loop
while rodando:
    relogio.tick(60)
    tela.fill(constantes.AZUL)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            velocidade = constantes.ALTURA_PULO

    velocidade += constantes.GRAVIDADE
    passaro_y += velocidade

    pygame.draw.circle(tela, constantes.AMARELO, (passaro_x, int(passaro_y)), constantes.TAMANHO_PASSARO)

    cano_x -= constantes.VELOCIDADE_CANO

    if cano_x + constantes.LARGURA_CANO < 0:
        cano_x = constantes.LARGURA
        ja_contou_ponto = False
        cano_altura = random.randint(150, 450)

    pygame.draw.rect(tela, constantes.VERDE, (cano_x, 0, constantes.LARGURA_CANO, cano_altura))
    pygame.draw.rect(tela, constantes.VERDE, (cano_x, cano_altura + constantes.ESPACO_CANOS, constantes.LARGURA_CANO, constantes.ALTURA))

    colidiu_horizontal = (
        passaro_x + constantes.TAMANHO_PASSARO > cano_x and 
        passaro_x - constantes.TAMANHO_PASSARO < cano_x + constantes.LARGURA_CANO
    )

    colidiu_vertical = (
        passaro_y - constantes.TAMANHO_PASSARO < cano_altura or
        passaro_y + constantes.TAMANHO_PASSARO > cano_altura + constantes.ESPACO_CANOS
    )

    colidiu_cano = colidiu_horizontal and colidiu_vertical
    fora_da_tela = passaro_y > constantes.ALTURA or passaro_y < 0

    if colidiu_cano or fora_da_tela:
        rodando = False
    
    if cano_x + constantes.LARGURA_CANO < passaro_x and not ja_contou_ponto:
        pontos += 1
        ja_contou_ponto = True
    
    texto = fonte.render(f'Pontos: {pontos}', True, (255, 255, 255)) 
    tela.blit(texto, (10, 10))


    pygame.display.update()


pygame.quit()