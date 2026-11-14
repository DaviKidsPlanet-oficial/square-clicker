#Fazer test run e fazer arquivo exe!
import os
import sys
import pygame
import time
import random

def resource_path(nome):
    # Works both when running the .py and inside the PyInstaller bundle
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, nome)

#Setup
pygame.init()
Porcentagem_pronto = 10
print(f"Loading: {Porcentagem_pronto:.2f}%") # pyright: ignore[reportUndefinedVariable]

#Square clicker icon
icon_surface = pygame.image.load(resource_path('Icone_jogo.png'))
pygame.display.set_icon(icon_surface)
Porcentagem_pronto += 10
print(f"Loading: {Porcentagem_pronto:.2f}%")

#Color variables
Verde = (0,255,0)
Branco = (255,255,255)
Preto = (0,0,0)
Amarelo = (255,255,100)
Cor_personagem = Verde
Azul = (0,0,255)
Porcentagem_pronto += 10
print(f"Loading: {Porcentagem_pronto:.2f}%")

#Language selection
TEXTOS = {
    "en": {
        "points": "Points", "pts": "points", "x2": "2X Points", "auto": "Automation",
        "per_s": "points/s", "per_click": "points/click",
        "press": "Press 'E' for 1st upgrade, 'D' for 2nd and 'G' for 3rd", "press_x": 200,
        "gold": "Golden Click", "gold_msg": "Golden click!", "max": "MAX", "lvl": "Lv",
        "contrib": "Automation contributed {p} points after {s} seconds.",
        "bye": "Goodbye!",
    },
    "pt": {
        "points": "Pontos", "pts": "pontos", "x2": "2X Pontos", "auto": "Automação",
        "per_s": "pontos/s", "per_click": "pontos/click",
        "press": "Aperte 'E' para a 1ª melhoria, 'D' para a 2ª e 'G' para a 3ª", "press_x": 250,
        "gold": "Clique Dourado", "gold_msg": "Clique dourado!", "max": "MÁX", "lvl": "Nv",
        "contrib": "Automação contribuiu com {p} pontos depois de {s} segundos.",
        "bye": "Tchau!",
    },
}

def escolher_idioma():
    tela_menu = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Square Clicker")
    f_titulo = pygame.font.SysFont("Arial", 48)
    f_texto = pygame.font.SysFont("Arial", 24)
    f_botao = pygame.font.SysFont("Arial", 32)
    botoes = [
        ("en", "English", pygame.Rect(250, 260, 300, 70)),
        ("pt", "Português", pygame.Rect(250, 360, 300, 70)),
    ]
    clock_menu = pygame.time.Clock()
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key in (pygame.K_1, pygame.K_KP1, pygame.K_e):
                    return "en"
                if ev.key in (pygame.K_2, pygame.K_KP2, pygame.K_p):
                    return "pt"
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                for codigo, _, rect in botoes:
                    if rect.collidepoint(ev.pos):
                        return codigo
        tela_menu.fill(Preto)
        titulo = f_titulo.render("Square Clicker", True, Verde)
        tela_menu.blit(titulo, titulo.get_rect(center=(400, 120)))
        sub = f_texto.render("Choose your language / Escolha o idioma", True, Branco)
        tela_menu.blit(sub, sub.get_rect(center=(400, 200)))
        for _, nome, rect in botoes:
            cor = (70, 70, 70) if rect.collidepoint(mouse) else (40, 40, 40)
            pygame.draw.rect(tela_menu, cor, rect, border_radius=8)
            pygame.draw.rect(tela_menu, Branco, rect, 2, border_radius=8)
            txt = f_botao.render(nome, True, Branco)
            tela_menu.blit(txt, txt.get_rect(center=rect.center))
        dica = f_texto.render("1 / 2", True, (150, 150, 150))
        tela_menu.blit(dica, dica.get_rect(center=(400, 480)))
        pygame.display.flip()
        clock_menu.tick(60)

IDIOMA = escolher_idioma()
T = TEXTOS[IDIOMA]

#Character variables
X = 375
Y = 250
Largura_altura = 50
X_circulo = 730
Y_circulo = 85
Raio = 50.0
Porcentagem_pronto += 10
print(f"Loading: {Porcentagem_pronto:.2f}%")

#Game variables
Pontos = float(0)
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Square Clicker")
clock = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 36)
texto_superficie = fonte.render(f"{T['points']}: {Pontos}", True, (255, 255, 255))
texto_rect = texto_superficie.get_rect(center=(80,20))
Pontos_por_click = 1
Pontos_Antes = 0
Porcentagem_pronto += 10
print(f"Loading: {Porcentagem_pronto:.2f}%")
#Shop variables
Hitbox_renda_2x = pygame.draw.circle(tela, Amarelo,(X_circulo, Y_circulo), Raio)
fonte_2Xpontos = pygame.font.SysFont("Arial", 16)
texto_superficie_2Xpontos = fonte_2Xpontos.render(T["x2"], True, (255, 255, 255))
texto_rect_2Xpontos = texto_superficie_2Xpontos.get_rect(center=(730, 85))
Vezes_compradas_2x = 0
Preço_2x = int(50 * (Vezes_compradas_2x +1))
Porcentagem_pronto += 10
print(f"Loading: {Porcentagem_pronto:.2f}%")
#Item 2
Hitbox_automação = pygame.draw.circle(tela, Azul,(X_circulo, Y_circulo + 100), Raio)
Vezes_compradas_automacao = 0
Preço_automacao = 100 * (Vezes_compradas_automacao + 1)
Automacao = False
texto_superficie_automacao = fonte_2Xpontos.render(f"{Preço_automacao} {T['pts']}", True, (255, 255, 255), (0,0,0))
texto_rect_automacao = texto_superficie_automacao.get_rect(center=(X_circulo, Y_circulo-130))
tela.blit(texto_superficie_automacao, texto_rect_automacao)
texto_superficie_automacao = fonte_2Xpontos.render(T["auto"], True, (255, 255, 255), (0,0,0))
texto_rect_automacao = texto_superficie_automacao.get_rect(center=(X_circulo, Y_circulo - 110))
Pontos_automação = 0.8
Segundos_automacao = 12
Mostrar_contribuição = False
Porcentagem_pronto += 10
print(f"Loading: {Porcentagem_pronto:.2f}%")
#Item 3 (Golden Click)
Nivel_dourado = 0
Nivel_dourado_max = 10
Chance_por_nivel = 5          # % per level (max 10 x 5 = 50%)
Preço_dourado = 200
Dourado = (255,200,0)
Dourado_loja = (255,140,0)
Dourado_ate = 0               # time when the golden color/message ends
Dourado_duracao = 5           # seconds
#Points/second variables
Pontos_por_S = 0
texto_superficie_porS = fonte_2Xpontos.render(f"{Pontos_por_S} {T['per_s']}    {Pontos_por_click} {T['per_click']}", True, (255, 255, 255), (0,0,0))
texto_rect_porS = texto_superficie_porS.get_rect(center=(200,80))
Pontos_por_S_Antes = 0
Porcentagem_pronto += 10
print(f"Loading: {Porcentagem_pronto:.2f}%")
#Screen variables
Largura = 800
Altura = 600
tela = pygame.display.set_mode((Largura, Altura)) #Width and height
Porcentagem_pronto += 10
print(f"Loading: {Porcentagem_pronto:.2f}%")

#Startup commands
rodando = True

Timer = time.time()
Timer_2 = time.time()
# Upgrade animation state (spin + color change)
upgrade_anim = False
upgrade_anim_start = 0
upgrade_anim_duration = 0.5  # seconds
upgrade_anim_color = None
Porcentagem_pronto += 10
print(f"Loading: {Porcentagem_pronto:.2f}%")

while rodando:
    Pontos = float(Pontos)
    Agora_2 = time.time()
    qto_passou_2 = Agora_2 - Timer_2
    if qto_passou_2 >= 1:
       Pontos_por_S = Pontos - Pontos_Antes
       Pontos_por_S_Antes = Pontos_por_S
       Timer_2 = time.time()
       Pontos_por_S = 0
    
    if qto_passou_2 < 0.016919851303100587:
        Pontos_Antes = Pontos
    
    


    tela.fill(Preto)
    Teclas_apertadas = pygame.key.get_pressed()

    if Teclas_apertadas [pygame.K_e]:
        if Pontos >= Preço_2x:
            Pontos -= Preço_2x
            Pontos_por_click *= 2
            Vezes_compradas_2x += 1
            Preço_2x = Pontos_por_click * 50 + (Preço_2x/10)
            Preço_2x -= int(Preço_2x/10)

            # Start upgrade animation (spin + color pulse)
            upgrade_anim = True
            upgrade_anim_start = time.time()
            upgrade_anim_color = (255, 255, 0)

    if Teclas_apertadas [pygame.K_d]:
        if Pontos >= Preço_automacao:
            Pontos -= Preço_automacao
            Vezes_compradas_automacao +=1
            if Vezes_compradas_automacao <= 5:
                Segundos_automacao = Segundos_automacao - 2
                Pontos_automação += 0.2
            if Vezes_compradas_automacao == 6:
                Segundos_automacao = 1
                Pontos_automação += 0.2
            if Vezes_compradas_automacao > 5:
                Pontos_automação += (Pontos_automação*Vezes_compradas_automacao)/6
                Pontos_automação = f"{Pontos_automação:.2f}"
                Pontos_automação = float(Pontos_automação)
            Preço_automacao *= 2
            Preço_automacao += Preço_automacao/50 + (0.2 * Vezes_compradas_automacao)
            Automacao = True
            print(Vezes_compradas_automacao)

            # Start upgrade animation (spin + color pulse)
            upgrade_anim = True
            upgrade_anim_start = time.time()
            upgrade_anim_color = (0, 255, 255)

    # draw clickable square
    player_rect = pygame.Rect(X, Y, Largura_altura, Largura_altura)

    # apply upgrade animation (spin + color pulse)
    player_color = Cor_personagem
    rotation_angle = 0
    if upgrade_anim:
        elapsed = time.time() - upgrade_anim_start
        t = min(elapsed / upgrade_anim_duration, 1.0)
        rotation_angle = 720 * t  # two full rotations
        if upgrade_anim_color is not None:
            player_color = tuple(
                int(Cor_personagem[i] + (upgrade_anim_color[i] - Cor_personagem[i]) * t)
                for i in range(3)
            )
        if t >= 1.0:
            upgrade_anim = False

    if time.time() < Dourado_ate and not upgrade_anim:
        player_color = Dourado

    player_surf = pygame.Surface((Largura_altura, Largura_altura), pygame.SRCALPHA)
    player_surf.fill(player_color)
    rotated = pygame.transform.rotate(player_surf, rotation_angle)
    rot_rect = rotated.get_rect(center=player_rect.center)
    tela.blit(rotated, rot_rect)

    pygame.draw.circle(tela, Amarelo, (X_circulo, Y_circulo), Raio, 0)
    pygame.draw.circle(tela, Azul, (X_circulo, Y_circulo+110), Raio, 0)
    pygame.draw.circle(tela, Dourado_loja, (X_circulo, Y_circulo+220), Raio, 0)

    
    tela.blit(texto_superficie, texto_rect)
    if Pontos > 1000000000000000000000:
        texto_superficie = fonte.render(f"{T['points']}: {Pontos/1000000000000000:.2f}Qua", True, (255, 255, 255))
    if Pontos < 1000000000000000000 and Pontos > 1000000000000000:
        texto_superficie = fonte.render(f"{T['points']}: {Pontos/1000000000000:.2f}T", True, (255, 255, 255))
    if Pontos < 1000000000000000 and Pontos > 1000000000000:
        texto_superficie = fonte.render(f"{T['points']}: {Pontos/1000000000:.2f}B", True, (255, 255, 255))
    texto_rect = texto_superficie.get_rect(center=(150,20))
    if Pontos < 1000000000000 and Pontos > 1000000:
        texto_superficie = fonte.render(f"{T['points']}: {Pontos/1000000:.2f}M", True, (255, 255, 255))
    else: 
        texto_superficie = fonte.render(f"{T['points']}: {int(Pontos)}", True, (255, 255, 255))
    

    tela.blit(texto_superficie_2Xpontos, texto_rect_2Xpontos)
    texto_superficie_2Xpontos = fonte_2Xpontos.render(T["x2"], True, (255, 255, 255), (0,0,0))
    texto_rect_2Xpontos = texto_superficie_2Xpontos.get_rect(center=(X_circulo, Y_circulo - 10))
    tela.blit(texto_superficie_2Xpontos, texto_rect_2Xpontos)
    if Preço_2x > 1000000000000:
        texto_superficie_2Xpontos = fonte_2Xpontos.render(f"{Preço_2x/1000000000:.2f}B {T['pts']}", True, (0, 0, 0))
    texto_rect_2Xpontos = texto_superficie_2Xpontos.get_rect(center=(150,20))
    if Preço_2x < 1000000000000 and Preço_2x > 1000000:
        texto_superficie_2Xpontos = fonte_2Xpontos.render(f"{Preço_2x/1000000:.2f}M {T['pts']}", True, (0, 0, 0))
    else: 
        texto_superficie_2Xpontos = fonte_2Xpontos.render(f"{int(Preço_2x)} {T['pts']}", True, (255, 255, 255), (0,0,0))
    texto_rect_2Xpontos = texto_superficie_2Xpontos.get_rect(center=(X_circulo, Y_circulo+10))
    tela.blit(texto_superficie_2Xpontos, texto_rect_2Xpontos)
    texto_superficie_2Xpontos = fonte_2Xpontos.render(T["press"], True, (255, 255, 255), (0,0,0))
    texto_rect_2Xpontos = texto_superficie_2Xpontos.get_rect(center=(T["press_x"],50))
    tela.blit(texto_superficie_2Xpontos, texto_rect_2Xpontos)
    #Points/s
    
    tela.blit(texto_superficie_porS, texto_rect_porS)
    if Pontos_por_S_Antes > 1000000000000:
        texto_superficie_porS = fonte_2Xpontos.render(f"{(int(Pontos_por_S_Antes)/1000000000):.2f}B {T['per_s']}    {Pontos_por_click} {T['per_click']}", True, (255, 255, 255))
    if Pontos_por_S_Antes < 1000000000000 and Pontos_por_S_Antes > 1000000:
        texto_superficie_porS = fonte_2Xpontos.render(f"{Pontos_por_S_Antes/1000000:.2f}M {T['per_s']}   {Pontos_por_click} {T['per_click']}", True, (255, 255, 255))
    if Pontos_por_S_Antes < 1000000 and Pontos_por_S_Antes > 0: 
        texto_superficie_porS = fonte_2Xpontos.render(f"{int(Pontos_por_S_Antes)} {T['per_s']}  {Pontos_por_click} {T['per_click']}", True, (255, 255, 255), (0,0,0))
    if Pontos_por_S_Antes <= 0:
         texto_superficie_porS = fonte_2Xpontos.render(f"0 {T['per_s']}     {Pontos_por_click} {T['per_click']}", True, (255, 255, 255), (0,0,0))
    texto_rect_porS = texto_superficie_porS.get_rect(center=(200,80))
    #Automation (Item 2)
    tela.blit(texto_superficie_automacao, texto_rect_automacao)
    if Preço_2x > 1000000000000:
        texto_superficie_automacao = fonte_2Xpontos.render(f"{int(Preço_automacao/1000000000)}B {T['pts']}", True, (255, 255, 255))
    texto_rect_automacao = texto_superficie_automacao.get_rect(center=(150,20))
    if Preço_automacao < 1000000000000 and Preço_automacao > 1000000:
        texto_superficie_automacao = fonte_2Xpontos.render(f"{int(Preço_automacao/1000000)}M {T['pts']}", True, (255, 255, 255))
    else: 
        texto_superficie_automacao = fonte_2Xpontos.render(f"{int(Preço_automacao)} {T['pts']}", True, (255, 255, 255), (0,0,0))
    texto_rect_automacao = texto_superficie_automacao.get_rect(center=(X_circulo, Y_circulo+120))
    tela.blit(texto_superficie_automacao, texto_rect_automacao)
    texto_superficie_automacao = fonte_2Xpontos.render(T["auto"], True, (255, 255, 255), (0,0,0))
    texto_rect_automacao = texto_superficie_automacao.get_rect(center=(X_circulo, Y_circulo + 100))
    #Golden Click (Item 3)
    t_nome = fonte_2Xpontos.render(T["gold"], True, Branco, Preto)
    tela.blit(t_nome, t_nome.get_rect(center=(X_circulo, Y_circulo + 210)))
    if Nivel_dourado >= Nivel_dourado_max:
        t_preco = fonte_2Xpontos.render(T["max"], True, Branco, Preto)
    else:
        t_preco = fonte_2Xpontos.render(f"{int(Preço_dourado)} {T['pts']}", True, Branco, Preto)
    tela.blit(t_preco, t_preco.get_rect(center=(X_circulo, Y_circulo + 230)))
    t_nivel = fonte_2Xpontos.render(f"{T['lvl']} {Nivel_dourado}/{Nivel_dourado_max} ({Nivel_dourado * Chance_por_nivel}%)", True, Branco, Preto)
    tela.blit(t_nivel, t_nivel.get_rect(center=(X_circulo, Y_circulo + 275)))
    if time.time() < Dourado_ate:
        t_msg = fonte.render(T["gold_msg"], True, Dourado, Preto)
        tela.blit(t_msg, t_msg.get_rect(center=(330, 150)))
    
    X_mouse, Y_mouse = pygame.mouse.get_pos()
    Mouse = pygame.Rect(X_mouse, Y_mouse, 5, 10)
    pygame.draw.rect(tela, Branco, Mouse)

    Hitbox_personagem = player_rect
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_g:
            if Nivel_dourado < Nivel_dourado_max and Pontos >= Preço_dourado:
                Pontos -= Preço_dourado
                Nivel_dourado += 1
                Preço_dourado = int(200 * 2 ** Nivel_dourado)
                upgrade_anim = True
                upgrade_anim_start = time.time()
                upgrade_anim_color = Dourado_loja
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if Mouse.colliderect(Hitbox_personagem):
                if not Largura_altura >= 300:
                    Largura_altura += 5
                    Pontos = Pontos + Pontos_por_click
                    if random.random() * 100 < Nivel_dourado * Chance_por_nivel:
                        Pontos = Pontos + Pontos_por_click   # golden click = double points
                        Dourado_ate = time.time() + Dourado_duracao
            if not Largura_altura <= 50:
                Largura_altura -= 5

    pygame.display.flip()
    clock.tick(60)
    if Automacao:
        Agora = time.time()
        qto_passou = Agora - Timer
        if qto_passou >= Segundos_automacao:
            Mostrar_contribuição = True
            Pontos += Pontos_automação
            Timer = time.time()
        if qto_passou >= 3:
            Mostrar_contribuição = False
        else:
            Mostrar_contribuição = True
    if Mostrar_contribuição:
        #I dunno what was the variable i was using for the player color so Ill change the 2 variables LOL
        if Pontos_automação > 1000000000:
            Pontos_automação = f"{Pontos_automação/1000000000:.2f}B"
        elif Pontos_automação > 1000000:
            Pontos_automação = f"{Pontos_automação/1000000:.2f}M"
        else:
            pass
        Pontos_automação = float(Pontos_automação)
        Cor_personagem = Azul
        Pontos_automação = f"{Pontos_automação:.2f}"
        Pontos_automação = float(Pontos_automação)
        texto_superficie_2Xpontos = fonte_2Xpontos.render(T["contrib"].format(p=Pontos_automação, s=Segundos_automacao), True, (Azul), (Branco))
        texto_rect_2Xpontos = texto_superficie_2Xpontos.get_rect(center=(230,100))
        tela.blit(texto_superficie_2Xpontos, texto_rect_2Xpontos)
    else:
        Cor_personagem = Verde
print(T["bye"])
