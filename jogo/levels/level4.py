import pygame

from enemy import Enemy
from checkpoint import Checkpoint


class Level4:

    def __init__(self):

        self.largura = 2800
        self.altura = 700

        self.cor_fundo = (20, 30, 35)

        self.plataformas = [
            # Chão
            pygame.Rect(0, 600, 2800, 100),

            # Plataformas
            pygame.Rect(100, 500, 180, 30),
            pygame.Rect(400, 430, 180, 30),
            pygame.Rect(700, 500, 150, 30),
            pygame.Rect(950, 380, 180, 30),
            pygame.Rect(1250, 470, 160, 30),
            pygame.Rect(1500, 350, 180, 30),
            pygame.Rect(1800, 450, 160, 30),
            pygame.Rect(2050, 330, 180, 30),
            pygame.Rect(2350, 430, 180, 30),
            pygame.Rect(2600, 500, 150, 30),
        ]

        # Inimigos
        self.inimigos = [
            Enemy(430, 385),
            Enemy(720, 455),
            Enemy(980, 335),
            Enemy(1280, 425),
            Enemy(1530, 305),
            Enemy(1830, 405),
            Enemy(2080, 285),
            Enemy(2380, 385),
        ]

        # Checkpoint
        self.checkpoints = [
            Checkpoint(1450, 290)
        ]

        # Saída
        self.saida = pygame.Rect(
            2650,
            430,
            50,
            70
        )

    def desenhar(self, tela, camera_x):

        # Fundo
        tela.fill(self.cor_fundo)

        # Plataformas
        for plataforma in self.plataformas:

            plataforma_tela = plataforma.copy()
            plataforma_tela.x -= camera_x

            pygame.draw.rect(
                tela,
                (90, 70, 55),
                plataforma_tela
            )

        # Checkpoints
        for checkpoint in self.checkpoints:

            checkpoint_tela = checkpoint.rect.copy()
            checkpoint_tela.x -= camera_x

            pygame.draw.rect(
                tela,
                (120, 60, 30),
                checkpoint_tela
            )

        # Saída
        saida_tela = self.saida.copy()
        saida_tela.x -= camera_x

        pygame.draw.rect(
            tela,
            (80, 180, 100),
            saida_tela
        )