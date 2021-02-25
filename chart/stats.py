import pandas as pd
import matplotlib
import matplotlib.font_manager
from matplotlib.patches import Circle, Rectangle, Arc, ConnectionPatch

from nba_api.stats.endpoints import shotchartdetail, leaguegamefinder, playergamelog, playernextngames, commonplayerinfo, playercareerstats
from nba_api.stats.static import players, teams

nba_players = players.get_players()
nba_teams = teams.get_teams()


def get_player_info(player_id):
    commoninfo = commonplayerinfo.CommonPlayerInfo(player_id=player_id)

    return {'commoninfo': commoninfo.get_dict()}


def get_player_stats(player_id, season_year, season_type):
    career = playercareerstats.PlayerCareerStats(
        player_id=player_id, per_mode36='Totals')

    season = career.get_dict()
    season_stats = season['resultSets'][0]['rowSet'][-1]

    ppg = season_stats[26] / season_stats[6]
    ast = season_stats[21] / season_stats[6]
    reb = season_stats[20] / season_stats[6]

    return {'careerstats': season, 'PTS': "{:.1f}".format(ppg), 'AST': "{:.1f}".format(ast), 'REB': "{:.1f}".format(reb)}


def get_ids(player_name, team_name):
    player_info = [
        player for player in nba_players if player['full_name'] == player_name][0]
    player_id = player_info['id']

    team_info = [
        team for team in nba_teams if team['abbreviation'] == team_name][0]
    team_id = team_info['id']

    return {'player_id': player_id, 'team_id': team_id}


def get_games(player_id, season_year, season_type):
    game = playergamelog.PlayerGameLog(
        player_id=player_id, season=season_year, season_type_all_star=season_type)

    next_game = playernextngames.PlayerNextNGames(
        number_of_games="1", player_id=player_id, season_all=season_year, season_type_all_star=season_type)

    return {'game': game.get_dict(), 'nextgame': next_game.get_dict()}
