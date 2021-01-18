# https://towardsdatascience.com/make-a-simple-nba-shot-chart-with-python-e5d70db45d0d
import variable
import pandas as pd
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import leaguegamefinder, playbyplay, playercareerstats
from nba_api.stats.library.parameters import Season, SeasonType

nba_players = players.get_players()


def find_player(player_name):
    player_info = [
        player for player in nba_players if player['full_name'] == player_name][0]
    print(player_info)
