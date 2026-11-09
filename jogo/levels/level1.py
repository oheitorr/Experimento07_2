import pygame
from enemy import Enemy
from checkpoint import Checkpoint


class Level1:

    def __init__(self):

        self.largura = 2400
        self.altura = 700

        self.cor_fundo = (25, 20, 25)

        self.plataformas = [
            pygame.Rect(0, 600, 2400, 100),

            pygame.Rect(100, 500, 250, 30),
            pygame.Rect(450, 430, 250, 30),
            pygame.Rect(800, 500, 250, 30),
            pygame.Rect(1150, 420, 250, 30),
            pygame.Rect(1500, 500, 250, 30),
            pygame.Rect(1850, 430, 250, 30),
            pygame.Rect(2200, 500, 150, 30),
        ]

        self.inimigos = [
            Enemy(520, 385),
            Enemy(900, 455),
            Enemy(1550, 455),
        ]

        self.inimigo_especial = Enemy(
            1900,
            385,
            especial=True,
            habilidade="dash"
        )

        self.inimigos.append(
            self.inimigo_especial
        )

        self.checkpoints = [
            Checkpoint(1100, 360)
        ]

        self.saida = pygame.Rect(
            2300,
            530,
            50,
            70
        )

    def desenhar(self, tela, camera_x):

        tela.fill(self.cor_fundo)

        for plataforma in self.plataformas:

            plataforma_tela = plataforma.copy()

            plataforma_tela.x -= camera_x

            pygame.draw.rect(
                tela,
                (100, 70, 50),
                plataforma_tela
            )

        for checkpoint in self.checkpoints:

            checkpoint_tela = checkpoint.rect.copy()
            checkpoint_tela.x -= camera_x

            pygame.draw.rect(
                tela,
                (120, 60, 30),
                checkpoint_tela
            )

        for inimigo in self.inimigos:

            inimigo_tela = inimigo.rect.copy()
            inimigo_tela.x -= camera_x

            pygame.draw.rect(
                tela,
                (220, 80, 120),
                inimigo_tela
            )

        saida_tela = self.saida.copy()
        saida_tela.x -= camera_x

        pygame.draw.rect(
            tela,
            (80, 180, 100),
            saida_tela
        )