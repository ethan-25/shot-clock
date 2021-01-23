import variable

import pandas as pd
import seaborn
import datetime

from nba_api.stats.endpoints import shotchartdetail, leaguegamefinder, playbyplay, playercareerstats
from nba_api.stats.static import players, teams
from nba_api.stats.library.parameters import Season, SeasonType

import matplotlib
import matplotlib.font_manager
from matplotlib.patches import Circle, Rectangle, Arc, ConnectionPatch

nba_players = players.get_players()
nba_teams = teams.get_teams()


def find_player(player_name):
    player_info = [
        player for player in nba_players if player['full_name'] == player_name][0]
    player_id = player_info['id']
    return player_id


def find_team(team_name):
    team_info = [
        team for team in nba_teams if team['abbreviation'] == team_name][0]
    team_id = team_info['id']
    return team_id


def find_season(season):
    year = datetime.date.today().year
    if len(season) != 7 or season[4] != '-' or not 1976 <= int(season[0:4]) <= year:
        raise ValueError()
    elif int(season[-2:]) != int(season[2:4]) + 1:
        raise ValueError()
    else:
        return season


def display_info():
    print(variable.playerName)
    print(find_player(variable.playerName))
    print(variable.playerTeam)
    print(find_team(variable.playerTeam))
    print(variable.seasonYear)
    print(variable.seasonType)


def createChart():
    shot_detail = shotchartdetail.ShotChartDetail(player_id=find_player(variable.playerName),
                                                  team_id=find_team(variable.playerTeam), context_measure_simple='FGA',
                                                  season_type_all_star=variable.seasonType)
    shot_data = shot_detail.get_data_frames()[0]
