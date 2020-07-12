import csv
from .part import Part


class PartList:
    """This class represents list of part objects
        
        attrs:
            parts: list of parts
    """

    parts = None

    def __init__(self, filename):
        """ args:
            filename(str) : path to csv file of parts 
        """
        PartList.parts = PartList.get_parts_list_from_file(filename)

    @staticmethod
    def get_parts_list_from_file(filename):
        """Extracts and returns list of parts and their attributes
            from the csv file 

            args:
                filename(str) : path to csv file of parts 

            return:
                parts_list(list) : list of parts
        """

        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            parts_list = list()
            heading = next(csv_reader)
            for row in csv_reader:
                part = Part(row[0], row[1], row[2], row[3])
                parts_list.append(part)
        return parts_list

    @staticmethod
    def get_parts_by_id(part_list_id):
        """Returns part which matches the given id

            args:
                part_id(string): id of part to be searched

            return:
                part(Part): part object which matches the id  
        """

        parts = list()
        for part in PartList.parts:
            if part.get_part_list_id() == part_list_id:
                parts.append(part)
        return parts
