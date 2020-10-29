import numpy as np


class RobotManager:
    """This class is responsible for the Robot Navigation. At every instance, the robot calculates the distance between 2 points and computes a battery check
    operation. If the battery isn't sufficient, the robot throws a ValueError. If not, the robot moves to the location."""
    def __init__(self, batteryStatus, battery_consumption):
        self.batteryStatus = batteryStatus
        self.battery_consumption = battery_consumption

    def checkBatteryStatus(self, distance):
        if self.batteryStatus > 100 or self.batteryStatus < 0:
            raise ValueError("Enter a Valid Battery Percentage")
        if self.batteryStatus == 0:
            raise ValueError("Please recharge the battery")
        else:
            if self.battery_consumption == 0:
                raise ValueError("Enter a valid Battery Consumption unit")
            elif self.batteryStatus >= (distance / self.battery_consumption):
                self.batteryStatus -= distance / self.battery_consumption
                return True
            else:
                return False

    def moveRobot(self, locationCoordinates):
        for a, b in zip(locationCoordinates, locationCoordinates[1:]):
            dist = np.linalg.norm(np.asarray(a)-np.asarray(b))
            status = self.checkBatteryStatus(dist)
            if status:
                continue
            else:
                print("Current Robot Location:", a)
                raise ValueError("Not enough Battery to move to next location")
