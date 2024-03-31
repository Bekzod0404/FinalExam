from django.db import models
from django.db.models import CharField


# Create your models here.

class SportType(models.Model):
    name = CharField(max_length=100)

    class Meta:
        verbose_name = 'Sport Type'
        verbose_name_plural = 'Sport Types'
        db_table = 'sport_types'

    def __str__(self):
        return self.name


class CountyLeague(models.Model):
    avatar = models.ImageField(upload_to='team_avatars')
    Country = models.CharField(max_length=100)
    League = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Country League'
        verbose_name_plural = 'Country Leagues'
        db_table = 'country_leagues'

    def __str__(self):
        return self.Country + ' ' + self.League


class Team(models.Model):
    avatar = models.ImageField(upload_to='team_avatars')
    name = models.CharField(max_length=100)
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        db_table = 'teams'

    def __str__(self):
        return self.name


class Match(models.Model):
    match_action = [
        ('started', 'started'),
        ('finished', 'finished'),
        ('upcoming', 'Upcoming'),
    ]

    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
    team1_score = models.IntegerField(default=0)
    team2_score = models.IntegerField(default=0)
    match_date = models.DateTimeField()
    action = models.CharField(max_length=10, choices=match_action, default='upcoming')
    country_league = models.ForeignKey(CountyLeague, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'
        db_table = 'matches'

    def __str__(self):
        return f'{self.team1} vs {self.team2}'
