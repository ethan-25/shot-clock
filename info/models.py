from django.db import models

# Create your models here.


class PlayerInfo(models.Model):
    player_name = models.CharField(max_length=50, default="Ben Simmons")
    team = models.CharField(max_length=3, default="PHI")
