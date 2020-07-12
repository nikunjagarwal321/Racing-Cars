class Team:
    """This class represents team and its attributes"""

    def __init__(self, team_id, team_name, cars, funds):
        """
            attrs:
                team_id(string): id of team
                team_name(string): name of team
                cars(list): list of cars that belong to the team
                funds(int): funds available to the team

        """
        self.__team_id = team_id
        self.__team_name = team_name
        self.__cars = cars
        self.__funds = int(funds)

    def get_team_id(self):
        return self.__team_id

    def set_team_id(self, team_id):
        self.__team_id = team_id

    def get_team_name(self):
        return self.__team_name

    def set_team_name(self, team_name):
        self.__team_name = team_name

    def get_cars(self):
        return self.__cars

    def set_cars(self, cars):
        self.__cars = cars

    def get_funds(self):
        return self.__funds

    def set_funds(self, funds):
        self.__funds = funds
