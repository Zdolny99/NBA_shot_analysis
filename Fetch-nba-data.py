import json
import pandas
import requests
import nba_api
import pandas as pd
import time

from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo

response = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=201935,
    season_nullable='2018-19',
    season_type_all_star='Regular Season'
)

content = json.loads(response.get_json())

all_players = players.get_players()
all_players_id = [p['id'] for p in all_players]

len(all_players_id)

active_players = []
for p in all_players:
    if p['is_active']:
        active_players.append(p['id'])

print(len(active_players))

season_years = [i for i in range(1990, 2022)]


def get_season_no(season_year):
    '''
    Converts season start year to season string (example: 2020 -> '2020-21')
    :param season_year: int
    :return: str
    '''
    assert isinstance(season_year, int)
    assert 1990 <= season_year <= 2022
    return str(season_year) + '-' + str(season_year + 1)[-2:]


def get_data_player_year(player_id, season_year):
    '''
    Fetches data for a given player for a given season
    :param player_id: int
    :param season_year: int
    :return: Dataframe
    '''
    assert isinstance(player_id, int)
    assert isinstance(season_year, int)
    assert 1990 <= season_year <= 2022

    url_base = 'https://stats.nba.com/stats/shotchartdetail'
    print("player_id", player_id)
    season = get_season_no(season_year)
    print("season", season)
    headers = {
        'Host': 'stats.nba.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Referer': 'https://stats.nba.com/',
        "x-nba-stats-origin": "stats",
        "x-nba-stats-token": "true",
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    parameters = {
        'ContextMeasure': 'FGA',
        'LastNGames': 0,
        'LeagueID': '00',
        'Month': 0,
        'OpponentTeamID': 0,
        'Period': 0,
        'PlayerID': player_id,
        'SeasonType': 'Regular Season',
        'TeamID': 0,
        'VsDivision': '',
        'VsConference': '',
        'SeasonSegment': '',
        'Season': season,
        'RookieYear': '',
        'PlayerPosition': '',
        'Outcome': '',
        'Location': '',
        'GameSegment': '',
        'GameId': '',
        'DateTo': '',
        'DateFrom': ''
    }
    response = requests.get(url_base, params=parameters, headers=headers)
    content = json.loads(response.content)
    # transform contents into dataframe
    results = content['resultSets'][0]
    headers = results['headers']
    rows = results['rowSet']
    df = pd.DataFrame(rows)
    df.columns = headers
    return df


def get_player_data(player_id):
    '''
    Fetches player metadata
    :param player_id: int
    :return: Dataframe
    '''
    assert isinstance(player_id, int)
    url_base = 'https://stats.nba.com/stats/commonplayerinfo?LeagueID=&PlayerID='
    print("player_id", player_id)
    headers = {
        'Host': 'stats.nba.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Referer': 'https://stats.nba.com/',
        "x-nba-stats-origin": "stats",
        "x-nba-stats-token": "true",
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    response = requests.get(url_base + str(player_id), headers=headers)
    content = json.loads(response.content)
    # transform contents into dataframe
    results = content['resultSets'][0]
    headers = results['headers']
    rows = results['rowSet']
    df = pd.DataFrame(rows)
    df.columns = headers
    return df


df = {}

for i in range(2536, 4832):
    player_id = all_players_id[i]
    try:
        player_info = get_player_data(player_id)
        from_year = player_info['FROM_YEAR'][0]
        to_year = player_info['TO_YEAR'][0]
    except:
        to_year = 2021
        from_year = 1990
    if to_year is None:
        to_year = 2021
    if from_year is None:
        from_year = 1990

    if to_year >= 1990:
        for season_year in range(max(from_year, 1990), min(to_year, 2021) + 1):
            print(season_year)
            try:
                time.sleep(1)
                dft = get_data_player_year(player_id, season_year)
                dft.to_csv('./Data/' + str(player_id) + '-' + str(season_year) + '.csv', index=False)
                if season_year not in df:
                    df[season_year] = dft
                else:
                    df[season_year] = pd.concat([df[season_year], dft], axis=0)
                print('success')
            except:
                print('unsuccessful')
                pass
