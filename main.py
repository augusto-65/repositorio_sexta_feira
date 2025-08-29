#este é um comentário de uma linha

import pgzrun
import random

# Constantes do jogo
LARGURA = 800
ALTURA = 600
FPS = 60

# Configurações do menu
menu_ativo = True
jogo_iniciado = False
musica_ativa = True

# Definições de pontuação e vidas
pontuacao = 0
vidas = 3

# Criando o herói
heroi = Actor("heroi_parado", pos=(400, 300))
velocidade_heroi = 5

# Inimigos
inimigos = [Actor("inimigo", pos=(random.randint(50, LARGURA-50), random.randint(50, ALTURA-50))) for _ in range(5)]
velocidade_inimigo = 2

# Obstáculos
obstaculos = [Actor("obstaculo", pos=(random.randint(100, LARGURA-100), random.randint(100, ALTURA-100))) for _ in range(3)]

# Música e sons
def tocar_musica():
    if musica_ativa:
        sounds.musica_de_fundo.play(loops=-1, volume=0.5)

def parar_musica():
    sounds.musica_de_fundo.stop()

# Função de animação do herói
def atualizar_heroi():
    if keyboard.left:
        heroi.x -= velocidade_heroi
        heroi.image = "heroi_esquerda"
    elif keyboard.right:
        heroi.x += velocidade_heroi
        heroi.image = "heroi_direita"
    if keyboard.up:
        heroi.y -= velocidade_heroi
    elif keyboard.down:
        heroi.y += velocidade_heroi
    if not (keyboard.left or keyboard.right or keyboard.up or keyboard.down):
        heroi.image = "heroi_parado"

# Função de movimento dos inimigos
def mover_inimigos():
    global pontuacao
    for inimigo in inimigos:
        inimigo.x += random.choice([-velocidade_inimigo, velocidade_inimigo])
        inimigo.y += random.choice([-velocidade_inimigo, velocidade_inimigo])
        if inimigo.x > LARGURA: inimigo.x = LARGURA
        if inimigo.x < 0: inimigo.x = 0
        if inimigo.y > ALTURA: inimigo.y = ALTURA
        if inimigo.y < 0: inimigo.y = 0
        if heroi.colliderect(inimigo):
            inimigo.pos = (random.randint(50, LARGURA-50), random.randint(50, ALTURA-50))  # Reseta a posição do inimigo
            diminuir_vidas()

# Função para gerar obstáculos
def gerar_obstaculos():
    for obstaculo in obstaculos:
        obstaculo.x += random.choice([-2, 2])
        obstaculo.y += random.choice([-2, 2])
        if obstaculo.x > LARGURA: obstaculo.x = LARGURA
        if obstaculo.x < 0: obstaculo.x = 0
        if obstaculo.y > ALTURA: obstaculo.y = ALTURA
        if obstaculo.y < 0: obstaculo.y = 0
        if heroi.colliderect(obstaculo):
            diminuir_vidas()

# Função para diminuir as vidas
def diminuir_vidas():
    global vidas
    vidas -= 1
    if vidas <= 0:
        game_over()

# Função de game over
def game_over():
    global jogo_iniciado, menu_ativo
    jogo_iniciado = False
    menu_ativo = True
    sounds.musica_de_fundo.stop()

# Tela de Menu
def desenhar_menu():
    screen.fill((0, 0, 0))  # Cor de fundo preta para o menu
    screen.draw.text("Menu do Jogo", center=(LARGURA // 2, 100), fontsize=50, color="white")
    screen.draw.text("Iniciar Jogo", center=(LARGURA // 2, 200), fontsize=30, color="white")
    screen.draw.text("Música: On" if musica_ativa else "Música: Off", center=(LARGURA // 2, 250), fontsize=30, color="white")
    screen.draw.text("Sair", center=(LARGURA // 2, 300), fontsize=30, color="white")
    screen.draw.text(f"Pontuação: {pontuacao}", center=(LARGURA // 2, 400), fontsize=30, color="white")
    screen.draw.text(f"Vidas: {vidas}", center=(LARGURA // 2, 450), fontsize=30, color="white")

# Tela de Jogo
def desenhar_jogo():
    screen.blit("background.png", (0, 0))  # Carregar o fundo do jogo (imagem)
    heroi.draw()
    for inimigo in inimigos:
        inimigo.draw()
    for obstaculo in obstaculos:
        obstaculo.draw()
    screen.draw.text(f"Pontuação: {pontuacao}", (10, 10), fontsize=30, color="white")
    screen.draw.text(f"Vidas: {vidas}", (LARGURA - 120, 10), fontsize=30, color="white")

def ao_clicar_na_tela(pos):
    global menu_ativo, jogo_iniciado, musica_ativa
    if menu_ativo:
        if 200 < pos[1] < 230:
            jogo_iniciado = True
            menu_ativo = False
            tocar_musica()
        elif 250 < pos[1] < 280:
            musica_ativa = not musica_ativa
            if musica_ativa:
                tocar_musica()
            else:
                parar_musica()
        elif 300 < pos[1] < 330:
            exit()

def atualizar():
    if jogo_iniciado:
        atualizar_heroi()
        mover_inimigos()
        gerar_obstaculos()

def desenhar():
    if menu_ativo:
        desenhar_menu()
    else:
        desenhar_jogo()

# Iniciar o jogo
pgzrun.go()
