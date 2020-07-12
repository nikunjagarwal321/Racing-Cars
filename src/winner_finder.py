import sys
from models.car_list import CarList
from models.part_list import PartList
from models.teams_fastest_car import TeamsFastestCar
from models.team_list import TeamList


def get_winner():
    """Finds and returns the winning team from the list of
        all the teams

    return: 
        winning_team(TeamsFastestCar): team with fastest car
    
    """

    winning_team = None
    fastest_speed = 0
    teams_fastest_car_list = get_teams_fastest_cars_list()
    for teams_fastest_car in teams_fastest_car_list:
        if teams_fastest_car.get_max_speed() > fastest_speed:
            winning_team = teams_fastest_car
            fastest_speed = teams_fastest_car.get_max_speed()
    return winning_team


def get_teams_fastest_cars_list():
    """ Returns the list of all the teams along with their 
        fastest cars

    return: 
        teams_fastest_car_list(TeamsFastestCar[]): 
            List of all the teams with their fastest car

    """

    teams_fastest_car_list = []
    for team in TeamList.teams:
        car_ids = team.get_cars()
        funds = team.get_funds()
        teams_fastest_car = get_fastest_car_in_team(car_ids, funds)
        teams_fastest_car.set_team_name(team.get_team_name())
        teams_fastest_car_list.append(teams_fastest_car)
    return teams_fastest_car_list


def get_fastest_car_in_team(car_ids, funds):
    """ Returns the fastest car in a team from the list of 
        team's cars within available funds 

    args:
        car_ids(list): list of cars' ids
        funds(int): available funds in a team

    return: 
        teams_fastest_car: fastest car of a team
    
    """

    teams_fastest_car = TeamsFastestCar()
    teams_fastest_car.set_max_speed(0)
    for car_id in car_ids:
        car = CarList.get_car_by_id(car_id)
        top_speed = car.get_top_speed()
        base_speed = car.get_base_speed()
        part_list_id = car.get_part_list_id()
        (
            max_achievable_speed,
            parts,
            funds_spent,
        ) = get_best_performance_details_of_car(
            part_list_id, funds, base_speed, top_speed
        )
        if max_achievable_speed > teams_fastest_car.get_max_speed():
            teams_fastest_car.set_car_name(car.get_car_name())
            teams_fastest_car.set_max_speed(max_achievable_speed)
            teams_fastest_car.set_parts(parts)
            teams_fastest_car.set_funds_spent(funds_spent)
    return teams_fastest_car


def get_best_performance_details_of_car(
    part_list_id, funds, base_speed, top_speed
):
    """ Returns the best performance details of the
    car which can be achieved from available funds

    args:
        part_list_id(string): part_id  
        funds(int): available funds for a team
        base_speed(int): base speed of the car
        top_speed(int): max achievable speed of the car

    return: 
        a tuple consisting of 
        max_achievable_speed(int): maximum speed that can be 
            achieved by the car
        parts_picked(list): list of parts to be added to achieve
            the maximum speed 
        funds_spent(int): amount of money spent to achieve
            the maximum speed
    
    """

    parts = PartList.get_parts_by_id(part_list_id)
    max_possible_boost = top_speed - base_speed
    knapsack_matrix = calculate_knapack_matrix(parts, max_possible_boost)
    funds_spent, max_boost_achieved = get_funds_spent_and_boost(
        knapsack_matrix, max_possible_boost, funds
    )
    parts_picked = get_picked_parts(knapsack_matrix, parts, max_boost_achieved)
    max_achievable_speed = min(base_speed + max_boost_achieved, top_speed)
    return max_achievable_speed, parts_picked, funds_spent


def calculate_knapack_matrix(parts, max_possible_boost):
    """ Uses modified 0/1 knapsack problem approach to calculate 
        knapsack matrix to find max possible boost with given parts
        at minimum cost

    args:
        parts(list): list of parts that can be used  
        max_possible_boost(int): maximum boost that is possible for 
            a car which is the difference of top speed and base speed

    return: 
        knapsack_matrix: matrix consisting of min funds to achieve
            particular amount of speed boost
            rows : represent parts
            column : represent speed boost 
            knapsack_matrix[i][j] : represent min price required to 
                achieve speed boost of amount j from 0-i parts
    """

    no_of_parts = len(parts)
    kanpsack_matrix = [
        [sys.maxsize for boost in range(max_possible_boost + 1)]
        for part in range(no_of_parts + 1)
    ]

    for i in range(no_of_parts + 1):
        for j in range(max_possible_boost, -1, -1):
            curr_boost = parts[i - 1].get_speed_boost()
            price_of_part = parts[i - 1].get_price()
            if i == 0:
                kanpsack_matrix[i][j] = sys.maxsize
            elif j <= curr_boost:
                kanpsack_matrix[i][j] = min(
                    price_of_part, kanpsack_matrix[i - 1][j]
                )
            elif kanpsack_matrix[i - 1][j - curr_boost] != sys.maxsize:
                kanpsack_matrix[i][j] = min(
                    kanpsack_matrix[i - 1][j - curr_boost] + price_of_part,
                    kanpsack_matrix[i - 1][j],
                )
    return kanpsack_matrix


def get_funds_spent_and_boost(
    kanpsack_matrix, max_possible_boost, available_funds
):
    """ Returns maximum achievable boost and minimum amount of 
        funds spent from the available funds to achieve that 
        speed boost 

    args:
        knapsack_matrix([[]]): matrix consisting of min funds to achieve
            particular amount of speed boost
        max_possible_boost(int): maximum boost that is possible for 
            a car which is the difference of top speed and base speed
        available_funds(int): available funds for a team

    return: 
        a tuple consisting of 
        max_boost_achieved(int): maximum boost that can be 
            achieved by the car
        funds_spent(int): amount of money spent to achieve
            the maximum speed
    
    """

    no_of_parts = len(kanpsack_matrix) - 1
    funds_spent = 0
    curr_boost = max_possible_boost

    while (
        available_funds < kanpsack_matrix[no_of_parts][curr_boost]
        and curr_boost > 0
    ):
        curr_boost = curr_boost - 1
    if curr_boost != 0:
        funds_spent = kanpsack_matrix[no_of_parts][curr_boost]
    max_boost_achieved = curr_boost
    return funds_spent, max_boost_achieved


def get_picked_parts(kanpsack_matrix, parts, max_boost_achieved):
    """ Returns the parts to be picked to achieve maximum boost using
        minimum funds 

    args:
        knapsack_matrix([[]]): matrix consisting of min funds to achieve
            particular amount of speed boost
        parts(list): list of parts that can be used
        max_boost_achieved(int): maximum boost that can be 
            achieved by the car

    return: 
        parts_picked(list): list of parts required to achieve maximum boost
    
    """

    parts_picked = list()
    no_of_parts = len(parts)
    curr_boost = max_boost_achieved
    curr_funds = kanpsack_matrix[no_of_parts][curr_boost]
    curr_part = no_of_parts
    while curr_part > 0 and curr_boost > 0:
        if curr_funds != kanpsack_matrix[curr_part - 1][curr_boost]:
            parts_picked.append(parts[curr_part - 1])
            curr_boost = curr_boost - parts[curr_part - 1].get_speed_boost()
            curr_funds = curr_funds - parts[curr_part - 1].get_price()
        curr_part = curr_part - 1
    return parts_picked
