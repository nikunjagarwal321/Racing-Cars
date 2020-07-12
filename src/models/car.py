class Car:
    """This class represents cars"""

    def __init__(self, car_id, car_name, base_speed, top_speed, part_list_id):
        """
            attrs:
                car_id(string): id of car
                car_name(string): name of car
                base_speed(int): base speed of car
                top_speed(int): top speed of car
                part_list_id(string): id of parts list which can be added to car

        """

        self.__car_id = car_id
        self.__car_name = car_name
        self.__base_speed = int(base_speed)
        self.__top_speed = int(top_speed)
        self.__part_list_id = part_list_id

    def get_car_id(self):
        return self.__car_id

    def set_car_id(self, car_id):
        self.__car_id = car_id

    def get_car_name(self):
        return self.__car_name

    def set_car_name(self, car_name):
        self.__car_name = car_name

    def get_base_speed(self):
        return self.__base_speed

    def set_base_speed(self, base_speed):
        self.__base_speed = base_speed

    def get_top_speed(self):
        return self.__top_speed

    def set_top_speed(self, top_speed):
        self.__top_speed = top_speed

    def get_part_list_id(self):
        return self.__part_list_id

    def set_part_list_id(self, part_list_id):
        self.__part_list_id = part_list_id
