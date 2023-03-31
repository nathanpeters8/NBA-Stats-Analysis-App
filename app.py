from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import scoreboard
from nba_api.stats.static import teams
from nba_api.stats.static import players

import string
import pandas as pd

def main_menu():
    print()
    print()
    print("NBA Stats Analysis")
    print()
    print("1: Player Career Stats")
    print()
    print()
    
    number = str(input("Select a number: "))
    selection_manager(number)


def selection_manager(number):
    if number == "1":
        name = str(input("Player's Full Name: "))
        player = get_player_id(name)

        stats = playercareerstats.PlayerCareerStats(player_id=player["id"])
        df = stats.get_data_frames()[0]
        df = df.set_axis(df['SEASON_ID'].tolist(), axis='index', copy=True)
        df = df.drop(columns='SEASON_ID')

        with pd.option_context('display.max_rows', None,
                                'display.max_columns', None,
                                'display.precision', 3):
            print(df)
            
        print()
        print()
        selection_manager(number)

    else:
        print()
        print("Number not recognized. Please try again: ")
        main_menu()



def get_player_id(name):
    #name = string.capwords(name)
    nba_players = players.get_players()
    return [player for player in nba_players if player['full_name'] == name][0]

   


def main():

    main_menu()

if __name__ == "__main__":
    main()