from abc import ABC, abstractmethod

class DriveStrategy(ABC):

    @abstractmethod
    def drive(self):
        pass

class NormalDriveStrategy(DriveStrategy):

    def __init__(self):
        pass


    def drive(self):
        print("this is the normal drive")

class OffRodeDriveStrategy(DriveStrategy):

    def __init__(self):
        pass

    def drive(self):
        print("this is the OffRodeDrive drive")

class SpeedyDriveStrategy(DriveStrategy):

    def drive(self):
        print("this is the Speedy Drive stretegy")



class Vehicle:

    def __init__(self, drive_strategy):
        self.drive_strategy = drive_strategy

    def drive(self):
        self.drive_strategy.drive()


vehicle = Vehicle(OffRodeDriveStrategy())
vehicle.drive()
