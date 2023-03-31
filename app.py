from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import scoreboard
from nba_api.stats.static import teams
from nba_api.stats.static import players


#Basic Examples 

#Nikola Jokic career stats
career = playercareerstats.PlayerCareerStats(player_id='203999')
print(career.get_data_frames()[0]) 
#print(career.get_json())
#print(career.get_dict())


#Today's scoreboard
games = scoreboard.Scoreboard()
todays_games = games.get_data_frames()[0]
#print(todays_games['GAMECODE'])


#get specific team info
nba_teams = teams.get_teams()
nuggets = [team for team in nba_teams if team['full_name'] == 'Denver Nuggets'][0]
print(nuggets)

#get specific player info
nba_players = players.get_players()
jokic = [player for player in nba_players if player['full_name'] == 'Nikola Jokic'][0]
print(jokic)
