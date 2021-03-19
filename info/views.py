from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .stats import *

# Create your views here.

# Main Views


def index(request):
    inputs = PlayerInfo.objects.all()

    form = PlayerInfoForm()

    if request.method == "POST":
        form = PlayerInfoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    contents = {'inputs': inputs, 'form': form}
    # Return a http response
    return render(request, 'index.html', contents)


def viewPlayer(request, pk):  # pk is primary key

    player = PlayerInfo.objects.get(id=pk)

    playerid = get_ids(player.player_name, player.team)['player_id']
    teamid = get_ids(player.player_name, player.team)['team_id']

    playerinfo = get_player_info(
        playerid)['commoninfo']['resultSets'][0]['rowSet'][0]

    season_year = '2020-21'
    season_type = 'Regular Season'

    games = get_games(playerid, season_year, season_type)
    recent_game = games['game']['resultSets'][0]['rowSet'][0]
    next_game = games['nextgame']['resultSets'][0]['rowSet'][0]

    # 2021 Season Stats

    stats_2021 = get_player_stats(
        playerid, season_year, season_type)['careerstats']['resultSets'][0]['rowSet'][-1]

    points = get_player_stats(
        playerid, season_year, season_type)['PTS']

    assists = get_player_stats(
        playerid, season_year, season_type)['AST']

    rebounds = get_player_stats(
        playerid, season_year, season_type)['REB']

    content = {'Player': player.player_name, 'PlayerID': playerid,
               'TeamID': teamid, 'SeasonYear': season_year, 'SeasonType': season_type,
               # 'Headers': games['resultSets'][0]['rowSet'],
               'RecentGame': recent_game,
               'NextGame': next_game,
               'PlayerInfo': playerinfo,
               'CareerStats': stats_2021,
               'PTS': points,
               'AST': assists,
               'REB': rebounds}

    return render(request, 'view_player.html', content)


def deletePlayer(request, pk):
    player = PlayerInfo.objects.get(id=pk)
    content = {'player': player}

    if request.method == "POST":
        player.delete()
        return redirect("/")

    return render(request, 'delete_player.html', content)
