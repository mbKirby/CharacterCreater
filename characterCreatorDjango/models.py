from django.contrib.auth.models import User
from django.db import models

class Character(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='users'
    )
    name = models.CharField(max_length=100)
    characterLevel = models.PositiveIntegerField()
    age=models.PositiveIntegerField()
    sex=models.CharField(max_length=100)
    height=models.PositiveIntegerField()
    weight=models.PositiveIntegerField()
    hair=models.CharField(max_length=100)
    eye=models.CharField(max_length=100)
    skinColor=models.CharField(max_length=100)
    backstory=models.CharField(max_length=100)
    armorClass=models.PositiveIntegerField()
    hitPoints=models.PositiveIntegerField()
    currentHitPoints=models.IntegerField(null=True)
    Speed=models.PositiveIntegerField()
    passivePerception=models.PositiveIntegerField()
    darkVision=models.PositiveIntegerField()
    background=models.CharField(max_length=100)
    raceSelection=models.CharField(max_length=100)
    subClassSelection=models.CharField(max_length=100)
    classSelection=models.CharField(max_length=100)
    subRaceSelection=models.CharField(max_length=100, blank=True, null=True)
    alignmentSelection=models.CharField(max_length=100)
    chosenProficiencies=models.CharField(max_length=100)
    cha=models.PositiveIntegerField()
    con=models.PositiveIntegerField()
    dex=models.PositiveIntegerField()
    int=models.PositiveIntegerField()
    str=models.PositiveIntegerField()
    wis=models.PositiveIntegerField()
    languageToolProficienciesSelection=models.CharField(max_length=100)
    cantripsSelection=models.CharField(max_length=100)
    equipment=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} level: {self.characterLevel}'