from classFiles.DataParser import DataParser
from classFiles.Path import Path
from classFiles.RobotManager import RobotManager
from utils.Constants import *

from utils.Constants import path


def main():
    # Create Object of Path class
    dataReader = Path(path)
    # Read the File
    read_file = dataReader.readFile()
    # Process the File - Extract and Clean the coordinate information
    file_content = DataParser.getDataFromFile(read_file)
    # Robot Navigator
    robotManager = RobotManager(CURRENT_BATTERY_STATUS, battery_consumption_per_unit_distance)
    # The below method is used so that the method moveRobot can be reused for a similar data.
    distance_metric = robotManager.moveRobot(file_content)
    # If the method is successful, the robot has completed its task.
    print("Robot Navigated Successfully")


if __name__ == '__main__':
    main()