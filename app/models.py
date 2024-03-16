from django.db import models

# Create your models here.
class Talaba(models.Model):
    ism = models.CharField(max_length = 36)
    fam = models.CharField(max_length = 36)
    yosh = models.IntegerField()
    login = models.IntegerField()
    parol = models.IntegerField()

    def __str__(self) -> str:
        return self.ism + " " + self.fam
