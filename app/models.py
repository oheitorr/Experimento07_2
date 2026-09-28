from django.db import models


class Jogador(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Pontuacao(models.Model):
    jogador = models.ForeignKey(
        Jogador,
        on_delete=models.CASCADE
    )

    pontos = models.IntegerField()

    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.jogador.nome} - {self.pontos}"