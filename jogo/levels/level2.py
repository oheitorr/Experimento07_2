import pygame

from enemy import Enemy
from checkpoint import Checkpoint


class Level2:

    def __init__(self):

        self.largura = 2400
        self.altura = 700

        self.cor_fundo = (25, 25, 35)

        self.plataformas = [
            # Chão
            pygame.Rect(0, 600, 2400, 100),

            # Plataformas
            pygame.Rect(100, 500, 200, 30),
            pygame.Rect(400, 450, 200, 30),
            pygame.Rect(700, 500, 200, 30),
            pygame.Rect(1000, 400, 200, 30),
            pygame.Rect(1300, 480, 200, 30),
            pygame.Rect(1600, 400, 200, 30),
            pygame.Rect(1900, 480, 200, 30),
            pygame.Rect(2200, 400, 150, 30),
        ]

        # Inimigos
        self.inimigos = [
            Enemy(450, 405),
            Enemy(750, 455),
            Enemy(1350, 435),
            Enemy(1650, 355),

            Enemy(
                1950,
                435,
                especial=True,
                habilidade="marshmallow"
            ),
        ]

        # Checkpoint
        self.checkpoints = [
            Checkpoint(1150, 340)
        ]

        # Saída
        self.saida = pygame.Rect(
            2300,
            330,
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
                (100, 70, 50),
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