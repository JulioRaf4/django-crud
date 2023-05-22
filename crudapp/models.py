from django.db import models


class Pessoa(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    bornDate = models.DateField(null=True)
    cpf = models.CharField(max_length=11, null=True)

    def __str__(self) -> str:
        return self.name
