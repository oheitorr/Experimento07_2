import pygame

from enemy import Enemy
from checkpoint import Checkpoint


class Level5:

    def __init__(self):

        self.largura = 3000
        self.altura = 700

        self.cor_fundo = (35, 20, 25)

        self.plataformas = [
            # Chão
            pygame.Rect(0, 600, 3000, 100),

            # Plataformas
            pygame.Rect(100, 500, 180, 30),
            pygame.Rect(400, 430, 180, 30),
            pygame.Rect(700, 500, 160, 30),
            pygame.Rect(950, 400, 180, 30),
            pygame.Rect(1250, 480, 160, 30),
            pygame.Rect(1500, 360, 180, 30),
            pygame.Rect(1800, 450, 160, 30),
            pygame.Rect(2050, 350, 180, 30),
            pygame.Rect(2300, 450, 160, 30),
            pygame.Rect(2550, 380, 180, 30),
            pygame.Rect(2800, 500, 150, 30),
        ]

        # Inimigos
        self.inimigos = [
            Enemy(430, 385),
            Enemy(730, 455),
            Enemy(980, 355),
            Enemy(1280, 435),
            Enemy(1530, 295),
            Enemy(1830, 405),
            Enemy(2080, 285),
            Enemy(2330, 405),
            Enemy(2580, 315),
        ]

        # Checkpoint
        self.checkpoints = [
            Checkpoint(1450, 300),
            Checkpoint(2400, 390)
        ]

        # Saída
        self.saida = pygame.Rect(
            2850,
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
                (100, 65, 50),
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