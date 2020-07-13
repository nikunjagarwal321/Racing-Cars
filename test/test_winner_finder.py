import unittest
from src import winner_finder
from src.models.car import Car
from src.models.car_list import CarList
from src.models.part import Part
from src.models.part_list import PartList
from src.models.team import Team
from src.models.team_list import TeamList


class TestWinnerFinder(unittest.TestCase):
    """
    Unittests to test different functions of winner_function script
    """

    def setUp(self):
        """
        Setup function to initialize different model lists
        """

        part1 = Part("PARTLIST_5E6B2", "PART_1F2BA", 1386, 50)
        part2 = Part("PARTLIST_5E6B2", "PART_95365", 1546, 42)
        part3 = Part("PARTLIST_06D40", "PART_C5965", 2725, 32)
        part4 = Part("PARTLIST_06D40", "PART_FAEF0", 3834, 25)
        part5 = Part("PARTLIST_33599", "PART_AC9B8", 3769, 26)
        car1 = Car("CARID_1402", "MODEL_B1BFE", 124, 160, "PARTLIST_5E6B2")
        car2 = Car("CARID_7347", "MODEL_39E91", 104, 205, "PARTLIST_06D40")
        car3 = Car("CARID_3861", "MODEL_3B4C7", 120, 201, "PARTLIST_33599")
        team1 = Team("0", "Force India", ["CARID_1402", "CARID_7347"], 9000)
        team2 = Team("2", "Mercedes", ["CARID_3861"], 8770)
        PartList.parts = [part1, part2, part3, part4, part5]
        CarList.cars = [car1, car2, car3]
        TeamList.teams = [team1, team2]

    def test_get_winner(self):
        """
        Unittest to check get_winner function
        """

        winning_team = winner_finder.get_winner()
        self.assertEqual("Force India", winning_team.get_team_name())

    def test_get_fastest_car_in_team(self):
        """
        Unittest to check get_fastest_car function
        """

        teams_fastest_car = winner_finder.get_fastest_car_in_team(
            TeamList.teams[0].get_cars(), TeamList.teams[0].get_funds()
        )
        self.assertEqual("MODEL_39E91", teams_fastest_car.get_car_name())

    def test_get_best_performance_details_of_car(self):
        """
        Unittest to check get_best_performance_details_of_car function
        """

        team = TeamList.teams[0]
        car_id = team.get_cars()[1]
        part3 = PartList.parts[3]
        part2 = PartList.parts[2]
        car = CarList.get_car_by_id(car_id)
        (
            max_achievable_speed,
            parts_picked,
            funds_spent,
        ) = winner_finder.get_best_performance_details_of_car(
            car.get_part_list_id(),
            team.get_funds(),
            car.get_base_speed(),
            car.get_top_speed(),
        )
        self.assertEqual(161, max_achievable_speed)
        self.assertEqual([part3, part2], parts_picked)
        self.assertEqual(6559, funds_spent)


if __name__ == "__main__":
    unittest.main()

