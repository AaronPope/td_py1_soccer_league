# Aaron Pope
# 05/17/2018
# Treehouse TechDegree - Python, Unit 1: Build a Soccer League


import csv
import utilities
import datetime

# Don't execute unless this is the main script
if __name__ == "__main__":

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

    def add_player_to_team (player, team):
        team["roster"].append(player)
        # return (team_name, player_list)
        utilities.generate_welcome_letter (player, team)

    def print_team_roster (team):
        print ("--- {} ---".format(team["team_name"].upper()))
        for player in team["roster"]:
            print ("{}, {}, {}".format(
                player["name"],
                player["experience"],
                player["guardian(s)"]
            ))
        print("\n")

    def get_experienced_players_count(players):
        number_of_experienced_players = 0
        for player in players:
            if player["Soccer Experience"] == "YES":
                number_of_experienced_players += 1
        return number_of_experienced_players

    # TODO: Check for valid team name
    def experienced_players_on_team(team_name):
        experienced_players_on_team = 0
        for player in teams[team_name]["roster"]:
            if player["experience"] == "YES":
                experienced_players_on_team += 1
        # Uncomment for debugging... explicitly in the console, a way that's probably ill-advised
        # print ("Experienced players on {}: {}".format(team_name, experienced_players_on_team))
        return experienced_players_on_team

    # TODO: this
    def write_team_to_file(team):
        with open ("output/teams.txt", "a") as file:
        # write to the file
            file.write("--- {} ---\n".format(team["team_name"]))
            for player in team["roster"]:
                file.write("{}, {}, {}\n".format(
                    player["name"],
                    player["experience"],
                    player["guardian(s)"]
                ))
            file.write("\n")

    def write_teams_to_file():    
        write_team_to_file(teams["sharks"])
        write_team_to_file(teams["dragons"])
        write_team_to_file(teams["raptors"])

    with open ("soccer_players.csv") as file:
        reader = csv.DictReader(file)
        soccer_players = list(reader)
        players_per_team = len(soccer_players) // len(teams)
        # TODO: Remove this "debug" item
        print ("PLAYERS PER TEAM: {}".format(players_per_team))
        
        experienced_player_quota = get_experienced_players_count(soccer_players) // len(teams)
        # TODO: Remove this "debug" item
        print ("EXPERIENCED PLAYERS PER TEAM: {}".format(experienced_player_quota))

        # Loop through the list of players
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
            
    # TODO: Remove this
    print_team_roster(teams["sharks"])
    print_team_roster (teams["dragons"])
    print_team_roster (teams["raptors"])

    write_teams_to_file()


# ---------------------- #
# DELIVERABLES REFERENCE #
# ---------------------- #
#
# Teams should have the same number of players
    # and the experienced players should be divided equally across the three teams
# Create a text file names 'teams.txt' that includes:
    # the name of a team
    # the players on the team
# Sample output
    # Sharks
    # Frank Jones, YES, Jim and Jan Jones
    # Sarah Palmer, YES, Robin and Sari Washington
    # Joe Smith, NO, Bob and Jamie Smith

# EXTRA CREDIT (1/2)
    # Create 18 text files, to serve as welcome letters to the players' guardians
        # 1 file should be created for each player
        # Use the players name as the name of the file
            # lowercase
            # underscore between first and last name
            # E.g. - "jimmy_johns.txt

# EXTRA CREDIT (2/2)
    # Ensure that each file includes the following: 
        # Begin with "Dear [guardian(s) name(s)]"
        # player's name
        # team name
        # date & time of first practice
