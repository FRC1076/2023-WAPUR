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
from networktables import NetworkTables

from robotconfig import robotconfig, MODULE_NAMES
from controller import Controller
"""
from swervedrive import SwerveDrive
from swervemodule import SwerveModule
from swervemodule import ModuleConfig

from swervedrive import BalanceConfig
from swervedrive import TargetConfig
from swervedrive import BearingConfig
from swervedrive import VisionDriveConfig

from swervometer import FieldConfig
from swervometer import RobotPropertyConfig
from swervometer import Swervometer

from elevator import Elevator
from grabber import Grabber
from vision import Vision
from logger import Logger
from dashboard import Dashboard

from tester import Tester
"""

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        controllers = self.initControllers(robotconfig["CONTROLLERS"])
        self.driver = controllers[0]
        self.operator = controllers[1]
        self.drivetrain = self.initDrivetrain()
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
    
    def initDrivetrain(self):
        print("initDrivetrain")
        motor_type = rev.CANSparkMaxLowLevel.MotorType.kBrushless
        self.motor1 = rev.CANSparkMax(10,motor_type)
        # self.motor2 = rev.CANSparkMax(2)
        # self.motor3 = rev.CANSparkMax(3)
        # self.motor4 = rev.CANSparkMax(4)
        # left_side = wpilib.MotorControllerGroup([motor1, motor2])
        # right_side = wpilib.MotorControllerGroup([motor3, motor4])

        # # Create Drivetrain
        # return wpilib.drive.DifferentialDrive(left_side, right_side)
        return False
    
    def initAuton(self, config):
        return
    
    def initTeleop(self):
        return

    def robotPeriodic(self):
        return True
    
    def teleopPeriodic(self):
        driver = self.driver.xboxController
        self.motor1.set(driver.getLeftX()/2)
        return
    
    def teleopDrivetrain(self):
        return
    
    def teleopElevatorGrabber(self):
        return
    
    def autonomousInit(self): #this or initAuton?
        self.timer = wpilib.Timer()
        self.timer.start()
        return
    
    def autonomousPeriodic(self):
        if self.timer.get() < 1.0:
            self.motor1.set(0.5)
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