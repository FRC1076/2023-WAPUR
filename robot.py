import math
import time
import sys
import os
from datetime import datetime

import wpilib
import wpimath
import wpilib.drive
import wpimath.controller
from wpilib import interfaces
import rev
import ctre
from navx import AHRS
from networktables import NetworkTables

from robotconfig import robotconfig, MODULE_NAMES
from controller import Controller
from tankdrive import TankDrive
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
        self.drivetrain = self.initDrivetrain(robotconfig["DRIVETRAIN"])
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
        gyro = wpilib.ADXRS450_Gyro()
        return TankDrive(config, gyro)
    
    def initAuton(self, config):
        return
    
    def teleopInit(self):
        return

    def robotPeriodic(self):
        return True
    
    def teleopPeriodic(self):
        self.teleopDrivetrain()
        return
    
    def teleopDrivetrain(self):
        self.drivetrain.getTankDrive().arcadeDrive(self.driver.xboxController.getRightX()/2, self.driver.xboxController.getLeftY())
        return
    
    def teleopElevatorGrabber(self):
        return
    
    def autonomousInit(self): #this or initAuton?
        self.autonPidController = wpimath.controller.PIDController(0.01, 0.001, 0.0005)
        self.timer = wpilib.Timer()
        self.timer.start()
        self.gyroAtTaskStart = self.drivetrain.getGyro().getAngle()
        self.autonCounter = 0
        return
    
    def autonomousPeriodic(self):
        self.task = robotconfig["AUTON"]["TASK"] #Get the current task set for the robot
        self.taskList = robotconfig["AUTON"][self.task] #Select the tasklist
        self.currentTask = self.taskList[self.autonCounter] #Select the current task
        self.gyroMode = robotconfig["AUTON"]["GYRO_MODE"] #Get the mode of the gyro, whether or not to reset after every task
        if(self.currentTask[0] == "FORWARD" and self.timer.get()<self.currentTask[1]):
            #Go forward for _ seconds
            self.drivetrain.forward(1)
        elif(self.currentTask[0] == "STOP"):
            self.drivetrain.stop()
            #Stop the robot
        elif(self.currentTask[0] == "COUNTERCLOCKWISE" and abs(self.drivetrain.getGyro().getAngle()) < self.currentTask[1]):
            print(self.drivetrain.getGyro().getAngle())
            self.drivetrain.counterclockwise(1)
            #Go counterclockwise to (gyro is ABSOLUTE) or by (gyro is RELATIVE) _ degrees.
        elif(self.currentTask[0] == "CLOCKWISE" and abs(self.drivetrain.getGyro().getAngle()) < self.currentTask[1]):
            print(self.drivetrain.getGyro().getAngle())
            self.drivetrain.clockwise(1)
            #Go counterclockwise to (gyro is ABSOLUTE) or by (gyro is RELATIVE) _ degrees.
        else:
            self.autonCounter += 1 #Go to the next task
            self.timer.restart() #Reset the timer
            self.gyroAtTaskStart = self.drivetrain.getGyro().getAngle()
    
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