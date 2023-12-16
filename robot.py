import math
import time
import sys
import os
from datetime import datetime

import wpilib
import wpilib.drive
import wpimath.controller
from wpilib import interfaces
import rev
import ctre
from navx import AHRS
#from networktables import NetworkTables

from robotconfig import robotconfig, MODULE_NAMES
from controller import Controller
from tankdrive import TankDrive

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        controllers = self.initControllers(robotconfig["CONTROLLERS"])
        self.driver = controllers[0]
        self.operator = controllers[1]
        self.drivetrain = TankDrive(robotconfig["DRIVETRAIN"])
        return
    
    def initLogger(self, dir):
        return #Logger.getLogger(dir)
    
    def initControllers(self, config):
        ctrls = []
        self.log(config)
        for ctrlConfig in config.values():
            self.log(ctrlConfig)
            ctrlID = ctrlConfig['ID']
            ctrl = wpilib.XboxController(ctrlID)
            dz = ctrlConfig['DEADZONE']
            lta = ctrlConfig['LEFT_TRIGGER_AXIS']
            rta = ctrlConfig['RIGHT_TRIGGER_AXIS']
            ctrls.append(Controller(ctrl, dz, lta, rta))
        return ctrls
    
    def initVision(self, config):
        return
    
    def initElevator(self, config):
        return
    
    def initGrabber(self, config):
        return
    
    def initDrivetrain(self, config):
        
        return
        return TankDrive(config)
    
    def initAuton(self, config):
        return
    
    def teleopInit(self):
        return

    def robotPeriodic(self):
        return True
    
    def teleopPeriodic(self):
        return
    
    def teleopDrivetrain(self):
        return
    
    def teleopElevatorGrabber(self):
        return
    
    def autonomousInit(self): #this or initAuton?
        return
    
    def autonomousPeriodic(self):
        return
    
    def teleopManeuver(self):
        return
    
    def deadzoneCorrection(self, val, deadzone):
        return

    def log(self, *dataToLog):
        return

if __name__ == "__main__":
    if sys.argv[1] == 'sim':
        TEST_MODE = True
    wpilib.run(MyRobot)