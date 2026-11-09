import pygame


class Checkpoint:

    def __init__(self, x, y):

        self.rect = pygame.Rect(
            x,
            y,
            50,
            60
        )

        self.ativo = False

    def ativar(self):

        self.ativo = True

    def desenhar(self, tela):

        pygame.draw.rect(
            tela,
            (120, 60, 30),
            self.rect
        )

        # Chocolate saindo da fonte
        pygame.draw.rect(
            tela,
            (90, 45, 20),
            (
                self.rect.x + 15,
                self.rect.y - 20,
                20,
                20
            )
        )