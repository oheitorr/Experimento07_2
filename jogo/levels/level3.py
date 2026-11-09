import pygame

from enemy import Enemy
from checkpoint import Checkpoint


class Level3:

    def __init__(self):

        self.largura = 2600
        self.altura = 700

        self.cor_fundo = (35, 25, 20)

        self.plataformas = [
            # Chão
            pygame.Rect(0, 600, 2600, 100),

            # Plataformas
            pygame.Rect(100, 500, 180, 30),
            pygame.Rect(380, 420, 180, 30),
            pygame.Rect(650, 500, 180, 30),
            pygame.Rect(920, 400, 180, 30),
            pygame.Rect(1200, 470, 180, 30),
            pygame.Rect(1480, 350, 180, 30),
            pygame.Rect(1760, 450, 180, 30),
            pygame.Rect(2040, 360, 180, 30),
            pygame.Rect(2320, 480, 180, 30),
        ]

        # Inimigos
        self.inimigos = [
            Enemy(420, 375),
            Enemy(690, 455),
            Enemy(960, 355),
            Enemy(1240, 425),
            Enemy(1520, 305),
            Enemy(1800, 405),
            Enemy(2080, 315),
        ]

        # Checkpoint
        self.checkpoints = [
            Checkpoint(1300, 410)
        ]

        # Saída
        self.saida = pygame.Rect(
            2400,
            410,
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
                (110, 70, 45),
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