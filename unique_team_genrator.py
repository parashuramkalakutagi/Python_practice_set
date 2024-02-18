import pandas as pd
import random

# Read player data from the Excel file
file_path = 'fc.xlsx'
df = pd.read_excel(file_path)

# Define the number of players to select for each team
team_size = 11
def unique_teams(dataframe,team_size):
    selected_players_1 = set()
    selected_players_2 = set()
    unique_team_1 = []
    captain_1 = []
    captain_2 = []
    vice_captain_1 = []
    vice_captain_2 = []
    unique_team_2 = []

    while len(unique_team_1) < team_size:
            # Sort players by the number of teams selected in ascending order
            sorted_players = dataframe.sort_values(by='Selected By', ascending=True)

            for _, row in sorted_players.iterrows():
                player = row['Players']
                if player not in selected_players_1:
                    unique_team_1.append(player)
                    selected_players_1.add(player)
                    break

    while len(unique_team_2) < team_size:
        sorted_players = dataframe.sort_values(by='Selected By', ascending=True)
        if sorted_players.empty:
            break
        for _, row in sorted_players.iterrows():
            player = row['Players']
            if player not in selected_players_2:
                if player not in unique_team_1:
                    unique_team_2.append(player)

    cap = random.choice(unique_team_1)
    captain_1.append(cap)
    remaining_players = [player for player in unique_team_1 if player != cap]
    vice_captain_1.append(random.choice(remaining_players))

    captain = random.choice(unique_team_2)
    captain_2.append(captain)
    remaining_player = [player for player in unique_team_2 if player != captain]
    vice_captain_2.append(random.choice(remaining_player))


    return unique_team_1 , unique_team_2,captain_1,vice_captain_1,vice_captain_2,captain_2


# def select_captain_and_vice_captain(team):
#     captain = random.choice(team)
#     remaining_players = [player for player in team if player != captain]
#     vice_captain = random.choice(remaining_players)
#     return captain, vice_captain



if __name__ == '__main__':
    my_teams = list(unique_teams(df,team_size))


    for i , player in enumerate(my_teams[0],start=1):
        print(f'{i}, {player}')
    print(f'captain : {my_teams[2]}')
    print(f'vice_captain : {my_teams[3]}')

    for i , player in enumerate(my_teams[1],start=1):
        print(f'{i}, {player}')
    print(f'captain : {my_teams[4]}')
    print(f'vice_captain : {my_teams[5]}')



    # print("Unique Team 1:")
    # for i, player in enumerate(my_teams[0],start=1):
    #     print(f" {i}, {player}")
    # captain, vice_captain = select_captain_and_vice_captain(my_teams[0])
    # print(f'Captain {captain} , vice-captain :{vice_captain}')
    #
    #
    # print("Unique Team Two")
    #
    # for i, player in enumerate(my_teams[1],start=1):
    #     print(f'{i} , {player}')
    # captain, vice_captain = select_captain_and_vice_captain(my_teams[1])
    # print(f'Captain {captain} , vice-captain :{vice_captain}')
    #









