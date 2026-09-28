import pygame


class Level:

    def __init__(self, largura, altura):

        self.largura = largura
        self.altura = altura

        self.plataformas = [
            pygame.Rect(0, 530, 1000, 70),

            pygame.Rect(150, 430, 180, 20),
            pygame.Rect(450, 350, 180, 20),
            pygame.Rect(700, 270, 180, 20),
        ]

    def desenhar(self, tela):

        for plataforma in self.plataformas:

            pygame.draw.rect(
                tela,
                (80, 80, 80),
                plataforma
            )