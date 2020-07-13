import sys
from src import winner_finder
from src.models.car_list import CarList
from src.models.part_list import PartList
from src.models.team_list import TeamList


def initialize(teams_file_name, cars_file_name, parts_file_name):
    """It opens the csv files, converts it into list of respective model type
        and stores it as class variable 
    """

    TeamList(teams_file_name)
    CarList(cars_file_name)
    PartList(parts_file_name)


def print_winner(winning_team):
    """ It prints the output of winning team in the desired format

    args: 
        winning team(TeamsFastestCar): team with fastest car

    """

    print("===============Winner===============")
    print("Team : {team_name}".format(team_name=winning_team.get_team_name()))
    print(
        "Car Name :  {car_name}".format(car_name=winning_team.get_car_name())
    )
    print(
        "Maximum Speed Achieved : {speed_achieved}".format(
            speed_achieved=winning_team.get_max_speed()
        )
    )
    print(
        "Funds Spent : {funds_spent}".format(
            funds_spent=winning_team.get_funds_spent()
        )
    )
    print("Parts : ")
    parts = ""
    for part in winning_team.get_parts():
        print(part.get_part_id())


def main():
    teams_file_name = sys.argv[1]
    cars_file_name = sys.argv[2]
    parts_file_name = sys.argv[3]
    initialize(teams_file_name, cars_file_name, parts_file_name)
    winning_team = winner_finder.get_winner()
    print_winner(winning_team)


if __name__ == "__main__":
    main()
