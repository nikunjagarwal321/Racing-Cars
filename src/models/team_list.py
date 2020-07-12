import csv
from .team import Team


class TeamList:
    """This class represents list of team objects
        
        attrs:
            teams: list of teams
    """

    teams = None

    def __init__(self, filename):
        """ args:
                filename(str) : path to csv file of teams
        """
        TeamList.teams = TeamList.get_teams_list_from_file(filename)

    @staticmethod
    def get_teams_list_from_file(filename):
        """Extracts and returns list of teams and their attributes
            from the csv file 

            args:
                filename(str) : path to csv file of teams

            return:
                teams_list(list) : list of teams
        """

        with open(filename) as csv_file:
            csv_reader = list(csv.reader(csv_file))
            no_of_rows = len(list(csv_reader))
            teams_list = list()
            i = 1
            while i < no_of_rows:
                cars_id_list = list()
                team_id = csv_reader[i][0]
                team_name = csv_reader[i][1]
                funds = csv_reader[i][3]
                while i < no_of_rows and csv_reader[i][0] == team_id:
                    cars_id_list.append(csv_reader[i][2])
                    i = i + 1
                team = Team(team_id, team_name, cars_id_list, funds)
                teams_list.append(team)
        return teams_list
