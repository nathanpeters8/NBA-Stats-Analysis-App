from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import scoreboard
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.static import teams
from nba_api.stats.static import players

#Finding Games

#Get team id
nba_teams = teams.get_teams()
nuggets = [team for team in nba_teams if team['abbreviation'] == 'DEN'][0]
nuggets_id = nuggets['id']
print(nuggets_id)


#query all games that nuggets have played in
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=nuggets_id)
games = gamefinder.get_data_frames()[0]
print("All Games: ")
print(games.head())
print(games.tail())

#Filter games from specific season
games_2223 = games[games.SEASON_ID.str[-4:] == '2022']
print("Games From 2022-2033 Season:")
print(games_2223.head())
print(games_2223.tail())


#Filter games against specific team
clippers_games_2223 = games_2223[games_2223.MATCHUP.str.contains('LAC')]
print("Nuggets vs Clippers 2022-2023 series")
print(clippers_games_2223.head())


#Specific game data for Nuggets
recent_clippers_game = clippers_games_2223.sort_values('GAME_DATE').iloc[-1]
print("Nuggets stats from most recent H2H against Clippers:")
print(recent_clippers_game)



