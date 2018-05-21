# Aaron Pope
# 05/17/2018
# Treehouse TechDegree - Python, Unit 1: Build a Soccer League


import csv
import datetime
import os
import utilities


# Don't execute unless this is the main script
if __name__ == "__main__":

    # Check for existence of output directories
    #  If they don't exist, create them
    if not os.path.exists("output"):
        os.makedirs("output")
    if not os.path.exists("output/welcome_letters"):
        os.makedirs("output/welcome_letters")

    # Clear the teams output each time the script is run
    with open ("output/teams.txt", "w") as file:
        file.write("")

    # Divide players into three teams
        # Sharks
        # Dragons
        # Raptors    
    teams = {
        "sharks": {
            "team_name": "Sharks", 
            "roster": [],
            "first_practice_info": datetime.datetime(2018, 5, 15, 13)},
        "dragons": {
            "team_name": "Dragons", 
            "roster": [],
            "first_practice_info": datetime.datetime(2018, 5, 17, 17)},
        "raptors": {
            "team_name": "Raptors", 
            "roster": [],
            "first_practice_info": datetime.datetime(2018, 5, 18, 9)},
    }


    # Add a player to a team
    def add_player_to_team (player, team):
        team["roster"].append(player)
        utilities.generate_welcome_letter (player, team)


    # Iterate through the list of all players
    # Return the number of players that have soccer experience
    def get_experienced_players_count(players):
        number_of_experienced_players = 0
        for player in players:
            if player["Soccer Experience"] == "YES":
                number_of_experienced_players += 1
        return number_of_experienced_players


    # Iterate through a provided team's roster
    # Return the number of exprienced players on that roster
    # (Different from the above because it's for a specific team's roster, not the player list)
    def experienced_players_on_team(team_name):
        experienced_players_on_team = 0
        for player in teams[team_name]["roster"]:
            if player["experience"] == "YES":
                experienced_players_on_team += 1
        return experienced_players_on_team

    # Save the provided team's roster to the output file 'teams.txt'
    def write_team_to_file(team):
        with open ("output/teams.txt", "a") as file:
            file.write("--- {} ---\n".format(team["team_name"]))
            for player in team["roster"]:
                file.write("{}, {}, {}\n".format(
                    player["name"],
                    player["experience"],
                    player["guardian(s)"]
                ))
            file.write("\n")

    # Loop through all teams in the team dictionary 
    #   and call the function to write them to the output file 'teams.txt'
    def write_teams_to_file():    
        for team in teams:
            write_team_to_file(teams[team])


    # Open the CSV file
    with open ("soccer_players.csv") as file:
        reader = csv.DictReader(file)

        # Create a list of players, using the reader
        soccer_players = list(reader)

        # Determine the number of players that should be on a team
        #  [# of players] / [# of teams]
        #  NOTE: This asssumes a number of players even divisible across all teams, 
        #           sufficient for this purpose
        players_per_team = len(soccer_players) // len(teams)
  
        # Determine the number of expereienced players that should be on a team
        # [# of experienced players] / [# of teams]
        experienced_player_quota = get_experienced_players_count(soccer_players) // len(teams)

        # Loop through the list of players and insert them into teams
        for soccer_player in soccer_players:
            # Extract the required information from the list object
            # Keys from CSV: 
                # Name
                # Height (inches)
                # Soccer Experience
                # Guardian Name(s)
            player_info = { "name": soccer_player["Name"], 
                            "experience": soccer_player["Soccer Experience"], 
                            "guardian(s)": soccer_player["Guardian Name(s)"]}

            # Experienced players
            if player_info["experience"] == "YES":
                if experienced_players_on_team("sharks") < experienced_player_quota:
                    add_player_to_team(player_info, teams["sharks"])
                elif experienced_players_on_team("dragons") < experienced_player_quota:
                    add_player_to_team(player_info, teams["dragons"])
                else:
                    add_player_to_team(player_info, teams["raptors"])
            # New players
            else:
                if len (teams["sharks"]["roster"]) - experienced_players_on_team("sharks") < players_per_team - experienced_player_quota:
                    add_player_to_team(player_info, teams["sharks"])
                elif len (teams["dragons"]["roster"]) - experienced_players_on_team("dragons") < players_per_team - experienced_player_quota:
                    add_player_to_team(player_info, teams["dragons"])
                else:
                    add_player_to_team(player_info, teams["raptors"])

    # After the players have been assigned to appropriate teams, 
    #  call function to write to 'teams.txt'
    write_teams_to_file()