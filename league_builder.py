# Aaron Pope
# 05/17/2018
# Treehouse TechDegree - Python, Unit 1: Build a Soccer League


import csv

# Don't execute unless this is the main script
if __name__ == "__main__":

# Divide players into three teams
    # Sharks
    # Dragons
    # Raptors    
    sharks = ("Sharks", [])
    dragons = ("Dragons", [])
    raptors = ("Raptors", [])

    def add_player_to_team (player, team):
        team_name, player_list = team
        player_list.append(player)
        return (team_name, player_list)

    with open ("soccer_players.csv") as file:
        reader = csv.DictReader(file)
        soccer_players = list(reader)

        for soccer_player in soccer_players:
            player_info = ( soccer_player["Name"], 
                            soccer_player["Soccer Experience"], 
                            soccer_player["Guardian Name(s)"])
            if len(sharks[1]) < 6:
                add_player_to_team(player_info, sharks)
            elif len(dragons[1]) < 6:
                add_player_to_team(player_info, dragons)
            else:
                add_player_to_team(player_info, raptors)

    print (sharks)
    print (dragons)
    print (raptors)



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
