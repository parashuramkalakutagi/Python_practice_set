# import pandas as pd
# import random
#
# # Read player data from the Excel file
# file_path = 'fc.xlsx'
# df = pd.read_excel(file_path)
#
# # Define the number of players to select for each team
# team_size = 11
#
# def create_unique_team(dataframe, team_size):
#     unique_team = []
#     selected_teams = set()
#     selected_captains = set()
#     selected_vice_captains = set()
#
#     while len(unique_team) < team_size:
#         # Sort players by the number of teams selected in ascending order
#         sorted_players = dataframe.sort_values(by='Selected By', ascending=True)
#
#         for _, row in sorted_players.iterrows():
#             player = row['Players']
#             if player not in selected_teams and player not in selected_captains and player not in selected_vice_captains:
#                 unique_team.append(player)
#                 selected_teams.add(player)
#                 selected_captains.add(player)
#                 selected_vice_captains.add(player)
#                 break
#
#     return unique_team
#
# def select_captain_and_vice_captain(team):
#     captain = random.choice(team)
#     remaining_players = [player for player in team if player != captain]
#     vice_captain = random.choice(remaining_players)
#     return captain, vice_captain
#
# if __name__ == "_main_":
#     unique_team = create_unique_team(df, team_size)
#     captain, vice_captain = select_captain_and_vice_captain(unique_team)
#
#     print("Unique Team:")
#     for i, player in enumerate(unique_team, start=1):
#         print(f"{i}. {player}")
#
#     print(f"Captain: {captain}")
#     print(f"Vice-Captain: {vice_captain}")










import pandas as pd
import random


# Read player data from the Excel file
file_path = '../../Python Practicefile/fc.xlsx'
df = pd.read_excel(file_path)

# Define the number of players to select for each team
team_size = 11

def create_unique_team(dataframe, team_size):
    selected_players = set()
    unique_team = []

    while len(unique_team) < team_size:
        sorted_players = dataframe[~dataframe['Players'].isin(selected_players)].sort_values(by='Selected By', ascending=True)
        if sorted_players.empty:
            break
        player = sorted_players.iloc[0]['Players']
        unique_team.append(player)
        selected_players.add(player)

    return unique_team


def create_unique_team_2(dataframe, team_size, existing_team):
    selected_players = set()
    unique_team = []

    while len(unique_team) < team_size:
        sorted_players = dataframe[~dataframe['Players'].isin(selected_players)].sort_values(by='Selected By',
                                                                                             ascending=True)
        if sorted_players.empty:
            break
        players = sorted_players.iloc[0]['Players']
        for first_team in existing_team:
            if first_team != players:
                unique_team.append(players)
                selected_players.add(players)


    return unique_team



def select_captain_and_vice_captain(team):
    captain = random.choice(team)
    remaining_players = [player for player in team if player != captain]
    vice_captain = random.choice(remaining_players)
    return captain, vice_captain

if __name__ == "__main__":
    unique_team = create_unique_team(df, team_size)
    captain, vice_captain = select_captain_and_vice_captain(unique_team)

    print("Unique Team:")
    for i, player in enumerate(unique_team, start=1):
        print(f"{i}. {player}")

    print(f"Captain: {captain}")
    print(f"Vice-Captain: {vice_captain}")

    second_unique_team = create_unique_team_2(df,team_size,unique_team)

    print(second_unique_team)






















