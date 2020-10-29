from classFiles.DataParser import DataParser
from classFiles.Path import Path
from classFiles.RobotManager import RobotManager


def main(path, status, consumption_rate):
    # Create Object of Path class
    dataReader = Path(path)
    # Read the File
    read_file = dataReader.readFile()
    # Process the File - Extract and Clean the coordinate information
    file_content = DataParser.getDataFromFile(read_file)
    # Robot Navigator
    robotManager = RobotManager(status, consumption_rate)
    # The below method is used so that the method moveRobot can be reused for a similar data.
    distance_metric = robotManager.moveRobot(file_content)
    # If the method is successful, the robot has completed its task.
    print("Robot Navigated Successfully")


if __name__ == '__main__':
    path = "https://pastebin.com/raw/mLc80Pen"
    # Assumption: The given coordinates are in Euclidean Space
    battery_consumption_per_unit_distance = 10  # For this unit distance, the robot consumes 1% of the battery.
    current_battery_status = 100  # Current Battery in percentage
    main(path, battery_consumption_per_unit_distance, current_battery_status)