class Part:
    """This class represents parts of car"""

    def __init__(self, part_list_id, part_id, price, speed_boost):
        """
            attrs:
                part_list_id(string): id of list to which part belongs to
                part_id(string): id of part
                price(int): price of part
                speed_boost(int): boost in speed that the part gives to car

        """
        self.__part_list_id = part_list_id
        self.__part_id = part_id
        self.__price = int(price)
        self.__speed_boost = int(speed_boost)

    def get_part_list_id(self):
        return self.__part_list_id

    def set_part_list_id(self, part_list_id):
        self.__part_list_id = part_list_id

    def get_part_id(self):
        return self.__part_id

    def set_part_id(self, part_id):
        self.__part_id = part_id

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_speed_boost(self):
        return self.__speed_boost

    def set_speed_boost(self, speed_boost):
        self.__speed_boost = speed_boost
