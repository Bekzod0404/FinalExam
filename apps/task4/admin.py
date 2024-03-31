from django.contrib import admin

from apps.task4.models import SportType, CountyLeague, Team, Match


# Register your models here.

@admin.register(SportType)
class SportTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(CountyLeague)
class CountyLeagueAdmin(admin.ModelAdmin):
    list_display = ["Country", "League"]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "sport_type"]


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ["team1", "team2", "team1_score", "team2_score", "match_date", "action", "country_league"]