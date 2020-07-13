import unittest
from src.models.car import Car
from src.models.part import Part
from src.models.team import Team
from src.models.teams_fastest_car import TeamsFastestCar
from src import winner_finder


class TestModels(unittest.TestCase):
    """
        Unittests to test functions of different models
    """

    def test_car_model(self):
        """
        Unittests to test car model
        """

        car = Car("CARID_1402", "MODEL_B1BFE", 124, 160, "PARTLIST_5E6B2")
        self.assertEqual("CARID_1402", car.get_car_id())
        self.assertEqual("MODEL_B1BFE", car.get_car_name())
        self.assertEqual(124, car.get_base_speed())
        self.assertEqual(160, car.get_top_speed())
        self.assertEqual("PARTLIST_5E6B2", car.get_part_list_id())

    def test_part_model(self):
        """
        Unittests to test part model
        """

        part = Part("PARTLIST_33599", "PART_AC9B8", 3769, 26)
        self.assertEqual("PARTLIST_33599", part.get_part_list_id())
        self.assertEqual("PART_AC9B8", part.get_part_id())
        self.assertEqual(3769, part.get_price())
        self.assertEqual(26, part.get_speed_boost())

    def test_team_model(self):
        """
        Unittests to test team model
        """

        team = Team("0", "Force India", ["CARID_1402", "CARID_7347"], 9000)
        self.assertEqual("0", team.get_team_id())
        self.assertEqual("Force India", team.get_team_name())
        self.assertEqual(["CARID_1402", "CARID_7347"], team.get_cars())
        self.assertEqual(9000, team.get_funds())

    def test_teams_fastest_car(self):
        """
        Unittests to test teams_fastest_car model
        """

        part1 = Part("PARTLIST_33599", "PART_AC9B8", 3769, 26)
        part2 = Part("PARTLIST_33599", "PART_DC4B8", 3421, 14)
        teams_fastest_car = TeamsFastestCar(
            "Mercedes", "MODEL_DF178", 252, 3423, [part1, part2]
        )
        self.assertEqual("Mercedes", teams_fastest_car.get_team_name())
        self.assertEqual("MODEL_DF178", teams_fastest_car.get_car_name())
        self.assertEqual(252, teams_fastest_car.get_max_speed())
        self.assertEqual(3423, teams_fastest_car.get_funds_spent())
        self.assertEqual([part1, part2], teams_fastest_car.get_parts())


if __name__ == "__main__":
    unittest.main()
