import pygame


class Player:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.largura = 50
        self.altura = 70

        self.velocidade = 5
        self.velocidade_y = 0

        self.gravidade = 0.8
        self.forca_pulo = -14

        self.no_chao = False

        self.tem_salto_marshmallow = False
        self.pulos_realizados = 0

        self.vida_maxima = 100
        self.vida = self.vida_maxima

        self.velocidade_dash = 15
        self.tempo_dash = 0
        self.cooldown_dash = 45

        self.tem_dash = False

        self.sprites = []

        nomes_sprites = [
            "player_idle.png",
            "melt_1.png",
            "melt_2.png",
            "melt_3.png",
            "melt_4.png"
        ]

        self.tempo_invulnerabilidade = 0

        self.direcao = 1

        self.mostrando_ataque = 0
        
        self.dano_ataque = 10
        self.tempo_ataque = 0

        self.velocidade_dash = 15
        self.tempo_dash = 0
        self.cooldown_dash = 0

        for nome in nomes_sprites:
        
            sprite = pygame.image.load(
                f"jogo/assets/player/{nome}"
            ).convert_alpha()

            sprite = pygame.transform.scale(
                sprite,
                (60, 80)
            )

            self.sprites.append(sprite)

        self.sprite = self.sprites[0]

        self.rect = pygame.Rect(
        self.x,
        self.y,
        self.largura,
        self.altura
    )

    def mover(self, teclas):

        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:

            self.rect.x -= self.velocidade
            self.direcao = -1

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:

            self.rect.x += self.velocidade
            self.direcao = 1

    def pular(self):

        if self.no_chao:

            self.velocidade_y = self.forca_pulo
            self.no_chao = False
            self.pulos_realizados = 1

        elif self.tem_salto_marshmallow and self.pulos_realizados < 2:

            self.velocidade_y = self.forca_pulo
            self.pulos_realizados += 1

    def aplicar_gravidade(self):

        self.velocidade_y += self.gravidade

        self.rect.y += self.velocidade_y

    def atualizar(self, teclas):

        if self.tempo_ataque > 0:
            self.tempo_ataque -= 1

        if self.mostrando_ataque > 0:
            self.mostrando_ataque -= 1

        if self.tempo_invulnerabilidade > 0:
            self.tempo_invulnerabilidade -= 1

        if self.cooldown_dash > 0:
            self.cooldown_dash -= 1

        if self.tempo_dash > 0:

            self.rect.x += (
                self.velocidade_dash *
                self.direcao
            )

            self.tempo_dash -= 1

        else:

            self.mover(teclas)

        self.aplicar_gravidade()

    def desenhar(self, tela, camera_x=0):

        posicao = self.rect.copy()
        posicao.x -= camera_x
    
        tela.blit(
            self.sprite,
            posicao
        )
    
        if self.mostrando_ataque > 0:
        
            area = self.obter_area_ataque()
            area.x -= camera_x
    
            pygame.draw.rect(
                tela,
                (255, 255, 255),
                area,
                2
            )

    def receber_dano(self, dano):

        if self.tempo_invulnerabilidade > 0:
            return

        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

        self.atualizar_sprite()

        self.tempo_invulnerabilidade = 60

    def atualizar_sprite(self):

        porcentagem_vida = (
            self.vida / self.vida_maxima
        ) * 100

        if porcentagem_vida > 75:

            indice = 0

        elif porcentagem_vida > 50:

            indice = 1

        elif porcentagem_vida > 25:

            indice = 2

        elif porcentagem_vida > 0:

            indice = 3

        else:

            indice = 4

        self.sprite = self.sprites[indice]

    def atacar(self):

        if self.tempo_ataque > 0:
            return False

        self.tempo_ataque = 20
        self.mostrando_ataque = 8

        return True
    
    def obter_area_ataque(self):
        area = self.rect.copy()
        area.width = 45
        if self.direcao == 1:
            area.left = self.rect.right
        else:
            area.right = self.rect.left
        return area
    
    def dash(self):

        if not self.tem_dash:
            return

        if self.cooldown_dash > 0:
            return

        self.tempo_dash = 8
        self.cooldown_dash = 45

    def desbloquear_dash(self):

        self.tem_dash = True

    def desbloquear_salto_marshmallow(self):

        self.tem_salto_marshmallow = True