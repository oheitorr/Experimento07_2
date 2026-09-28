import pygame


class Enemy:

    def __init__(self, x, y, especial=False, habilidade=None):

        self.largura = 45
        self.altura = 45

        self.rect = pygame.Rect(
            x,
            y,
            self.largura,
            self.altura
        )

        self.velocidade = 2

        self.direcao = 1

        self.limite_esquerdo = x - 100
        self.limite_direito = x + 100

        self.vida_maxima = 30
        self.vida = self.vida_maxima

        self.especial = especial
        self.habilidade = habilidade

    def atualizar(self):

        self.rect.x += self.velocidade * self.direcao
    
        if self.rect.left <= self.limite_esquerdo:
        
            self.rect.left = self.limite_esquerdo
    
            self.direcao = 1
    
        if self.rect.right >= self.limite_direito:
        
            self.rect.right = self.limite_direito
    
            self.direcao = -1

    def receber_dano(self, dano):

        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

    def esta_vivo(self):

        return self.vida > 0

    def desenhar(self, tela):
        if self.especial:
            pygame.draw.rect(tela, (255, 200, 50), self.rect)
        else:
            pygame.draw.rect(tela, (220, 80, 120), self.rect)