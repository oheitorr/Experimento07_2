import pygame

from player import Player
from level import Level
from enemy import Enemy
from checkpoint import Checkpoint
from levels.level1 import Level1
from levels.level2 import Level2
from levels.level3 import Level3
from levels.level4 import Level4
from levels.level5 import Level5


class Game:

    def __init__(self):

        self.largura = 1000
        self.altura = 600

        self.tela = pygame.display.set_mode(
            (self.largura, self.altura)
        )

        pygame.display.set_caption("Experimento 07")

        self.clock = pygame.time.Clock()

        self.rodando = True

        self.player = Player(100, 400)

        self.fase_atual = 1

        self.niveis = [
            Level1(),
            Level2(),
            Level3(),
            Level4(),
            Level5()
        ]

        self.level = self.niveis[self.fase_atual - 1]

        self.ultimo_checkpoint = (
            self.player.rect.x,
            self.player.rect.y
        )

        self.camera_x = 0

    def eventos(self):

        for evento in pygame.event.get():
        
            if evento.type == pygame.QUIT:
                self.rodando = False
    
            if evento.type == pygame.KEYDOWN:
            
                if evento.key == pygame.K_w:
                    self.player.pular()
    
                if evento.key == pygame.K_h:
                    self.player.receber_dano(10)
    
                if evento.key == pygame.K_ESCAPE:
                    self.rodando = False

                if evento.key == pygame.K_LSHIFT or evento.key == pygame.K_RSHIFT:
                    self.player.dash()
    
            if evento.type == pygame.MOUSEBUTTONDOWN:
            
                if evento.button == 1:
                    self.atacar()

    def atualizar(self):

        teclas = pygame.key.get_pressed()

        self.player.atualizar(teclas)

        self.player.no_chao = False

        for plataforma in self.level.plataformas:
        
            if self.player.rect.colliderect(plataforma):
            
                if self.player.velocidade_y >= 0:
                
                    self.player.rect.bottom = plataforma.top

                    self.player.velocidade_y = 0

                    self.player.no_chao = True

                    self.player.pulos_realizados = 0

        for checkpoint in self.level.checkpoints:

            if self.player.rect.colliderect(checkpoint.rect):
            
                checkpoint.ativar()

                self.ultimo_checkpoint = (
                    checkpoint.rect.x,
                    checkpoint.rect.y - 70
                )

                self.player.vida = self.player.vida_maxima
                self.player.atualizar_sprite()

        for inimigo in self.level.inimigos:

            inimigo.atualizar()

            if self.player.rect.colliderect(inimigo.rect):
            
                self.player.receber_dano(10)


        for inimigo in self.level.inimigos:
        
            if not inimigo.esta_vivo():

                if inimigo.habilidade == "dash":
                    self.player.desbloquear_dash()

                elif inimigo.habilidade == "marshmallow":
                    self.player.desbloquear_salto_marshmallow()


        self.level.inimigos = [
            inimigo
            for inimigo in self.level.inimigos
            if inimigo.esta_vivo()
        ]

        if self.player.vida <= 0:
                
                self.respawn()

        self.camera_x = self.player.rect.x - 400

        if self.camera_x < 0:
            self.camera_x = 0

        limite_camera = self.level.largura - self.largura

        if self.camera_x > limite_camera:
            self.camera_x = limite_camera

        if hasattr(self.level, "saida"):

            if self.player.rect.colliderect(self.level.saida):

                self.proxima_fase()

    def atacar(self):
            
        if not self.player.atacar():
            return

        area_ataque = self.player.obter_area_ataque()

        for inimigo in self.level.inimigos:
                
            if area_ataque.colliderect(inimigo.rect):
                    
                inimigo.receber_dano(
                    self.player.dano_ataque
                )

    def proxima_fase(self):

        if self.fase_atual >= 5:
            return

        self.fase_atual += 1

        self.level = self.niveis[
            self.fase_atual - 1
        ]

        self.player.rect.x = 100
        self.player.rect.y = 400

        self.player.velocidade_y = 0

        self.player.vida = self.player.vida_maxima

        self.player.atualizar_sprite()

        self.ultimo_checkpoint = (
            self.player.rect.x,
            self.player.rect.y
        )

    def desenhar(self):

    # Desenha a fase
        self.level.desenhar(
            self.tela,
            self.camera_x
        )
    
        # Desenha os inimigos
        for inimigo in self.level.inimigos:

            inimigo_tela = inimigo.rect.copy()
            inimigo_tela.x -= self.camera_x

        if inimigo.especial:
            pygame.draw.rect(
                self.tela,
                (255, 200, 50),
                inimigo_tela
        )
        else:
            pygame.draw.rect(
                self.tela,
                (220, 80, 120),
                inimigo_tela
            )
    
        # Desenha os checkpoints
        for checkpoint in self.level.checkpoints:
        
            checkpoint_tela = checkpoint.rect.copy()
            checkpoint_tela.x -= self.camera_x
    
            pygame.draw.rect(
                self.tela,
                (120, 60, 30),
                checkpoint_tela
            )
    
        # Desenha a saída
        if hasattr(self.level, "saida"):
        
            saida_tela = self.level.saida.copy()
            saida_tela.x -= self.camera_x
    
            pygame.draw.rect(
                self.tela,
                (80, 180, 100),
                saida_tela
            )
    
        # Desenha o jogador
        self.player.desenhar(
            self.tela,
            self.camera_x
        )
    
        # Barra de vida
        self.desenhar_vida()

    def executar(self):

        while self.rodando:

            self.clock.tick(60)

            self.eventos()

            self.atualizar()

            self.desenhar()

            pygame.display.flip()

        pygame.quit()

    def desenhar_vida(self):

        largura_barra = 250
        altura_barra = 25

        x = 20
        y = 20

        # Fundo da barra
        pygame.draw.rect(
            self.tela,
            (60, 60, 60),
            (x, y, largura_barra, altura_barra)
        )

        # Quantidade de vida atual
        largura_vida = int(
            largura_barra *
            (self.player.vida / self.player.vida_maxima)
        )

        pygame.draw.rect(
            self.tela,
            (120, 55, 30),
            (x, y, largura_vida, altura_barra)
        )

        # Borda
        pygame.draw.rect(
            self.tela,
            (255, 255, 255),
            (x, y, largura_barra, altura_barra),
            2
        )
        
    def respawn(self):
        self.player.rect.x = self.ultimo_checkpoint[0]
        self.player.rect.y = self.ultimo_checkpoint[1]
    
        self.player.velocidade_y = 0
    
        self.player.vida = self.player.vida_maxima
    
        self.player.atualizar_sprite()