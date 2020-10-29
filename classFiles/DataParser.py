import re


class DataParser:
    """This class is responsible for parsing and cleaning the data read from the URL"""

    @staticmethod
    def getDataFromFile(file):
        processed_list = []
        extract_coordinates = re.findall(r'\{(.*?)\}', file)
        for locations in extract_coordinates:
            location = [float(d) for d in locations.split(',')]
            processed_list.append(location)
        return processed_list