class TeamsFastestCar:
    """This class represents team and the fastest car of that team"""

    def __init__(
        self,
        team_name=None,
        car_name=None,
        max_speed=None,
        funds_spent=None,
        parts=None,
    ):
        """
            attrs:
                team_name(string): name of team
                car_name(string): name of fastest car of team
                max_speed(int): max speed of fastest car in a team
                funds(int): min amount of money spent by team to achieve max speed
                parts(list): list of parts which should be added to the car

        """

        self.__team_name = team_name
        self.__car_name = car_name
        self.__max_speed = max_speed
        self.__funds_spent = funds_spent
        self.__parts = parts

    def get_team_name(self):
        return self.__team_name

    def set_team_name(self, team_name):
        self.__team_name = team_name

    def get_car_name(self):
        return self.__car_name

    def set_car_name(self, car_name):
        self.__car_name = car_name

    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def get_funds_spent(self):
        return self.__funds_spent

    def set_funds_spent(self, funds_spent):
        self.__funds_spent = funds_spent

    def get_parts(self):
        return self.__parts

    def set_parts(self, parts):
        self.__parts = parts
