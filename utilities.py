import random

def generate_welcome_letter(player, team):
    name = player["name"].split()
    first_name = name[0]
    last_name = name[1]
    with open ("output/welcome_letters/{}_{}.txt".format(first_name, last_name), "w") as file:
        file.write ("""Dear {},\n
{} will be playing on the {}.
Their first practice is on {}.""".format(
            player["guardian(s)"], 
            player["name"],
            team["team_name"].upper(),
            team["first_practice_info"]))