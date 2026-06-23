from django.db import models

class Tarefa(models.Model):
    STATUS = [
        ('Pendente', 'Pendente'),
        ('Concluída', 'Concluída'),
    ]

    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS)
    prazo = models.DateField()

    def __str__(self):
        return self.nome