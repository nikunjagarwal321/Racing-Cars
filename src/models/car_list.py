import csv
from .car import Car


class CarList:
    """This class represents list of car objects
        
        attrs:
            cars: list of cars
    """

    cars = None

    def __init__(self, filename):
        """ args:
                filename(str) : path to csv file of cars 
        """
        CarList.cars = CarList.get_cars_list_from_file(filename)

    @staticmethod
    def get_cars_list_from_file(filename):
        """Extracts and returns list of cars and their attributes
            from the csv file 

            args:
                filename(str) : path to csv file of cars 

            return:
                car_list(list) : list of cars
        """

        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            cars_list = list()
            heading = next(csv_reader)
            for row in csv_reader:
                car = Car(row[0], row[1], row[2], row[3], row[4])
                cars_list.append(car)
        return cars_list

    @staticmethod
    def get_car_by_id(car_id):
        """Returns car which matches the given id

            args:
                car_id(string): id of car to be searched

            return:
                car(Car): car object which matches the id  
        """
        for car in CarList.cars:
            if car.get_car_id() == car_id:
                return car
        return None
