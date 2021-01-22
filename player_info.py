
import variable
import pandas as pd

from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import leaguegamefinder, playbyplay, playercareerstats
from nba_api.stats.library.parameters import Season, SeasonType

import matplotlib
import matplotlib.font_manager
from matplotlib.patches import Circle, Rectangle, Arc, ConnectionPatch

nba_players = players.get_players()
nba_teams = teams.get_teams()


def find_player(player_name):
    player_info = [
        player for player in nba_players if player['full_name'] == player_name][0]
    print(player_info['id'])
    print(variable.seasonType)
