from django.db import models

# Create your models here.

class Novel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Character(models.Model):
    name = models.CharField(max_length=100)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name='characters')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.novel.title})"
    

class ShadowSlaveCharacter(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE, related_name='shadow_slave_data')
    aspect_rank = models.CharField(max_length=100)
    aspect = models.CharField(max_length=150)
    rank = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.character.name} - Rank: {self.rank}'
    
class LotmCharacter(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE, related_name="lotm_data")
    pathway = models.CharField(max_length=100)
    sequence = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.character.name} - Pathway: {self.pathway} - Sequence: {self.sequence}'
    