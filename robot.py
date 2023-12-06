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
        self.autonCounter = 0
        return
    
    def autonomousPeriodic(self):
        #self.gyroAngle = ((self.gyro.getAngle() + 360) % 360)
        #self.gryoAngle = self.gryo.getAngle()
        self.task = robotconfig["AUTON"]["TASK"]
        self.taskList = robotconfig["AUTON"][self.task]
        self.currentTask = self.taskList[self.autonCounter]
        if(self.currentTask[0] == "FORWARD" and self.timer.get()<self.currentTask[1]):
            self.drivetrain.forward(1)
        #elif(self.currentTask[0] == "TURN_LEFT"):
        #    self.drivetrain.counterclockwise(1)
        elif(self.currentTask[0] == "STOP"):
            #self.drivetrain.stop()
            pass
        elif(self.currentTask[0] == "TURN_LEFT" and abs(self.drivetrain.getGyro().getAngle()) < self.currentTask[1]):
            print(self.drivetrain.getGyro().getAngle())
            self.drivetrain.counterclockwise(1)

        else:
            self.autonCounter += 1
        """
        if(self.task == "CRATE"):
            self.crateForwardTime = robotconfig["AUTON"]["CRATE_TASK_LIST"]["FORWARD_1"]
            if(self.timer.get()<self.crateForwardTime):
                self.drivetrain.forward(1)
        if(self.task == "BALL_R"):
            self.ballTurnTime = robotconfig["AUTON"]["BALL_TURN_TIME"]
            self.ball_rForward_1 = robotconfig["AUTON"]["BALL_R"]["FORWARD_1"]
            self.ball_rForward_2 = robotconfig["AUTON"]["BALL_R"]["FORWARD_2"]+self.ballTurnTime + self.ball_rForward_1
            self.ball_rForward_3 = robotconfig["AUTON"]["BALL_R"]["FORWARD_3"]+self.ballTurnTime + self.ball_rForward_2
            self.ball_rTurn_left = robotconfig["AUTON"]["BALL_R"]["TURN_LEFT"]
            self.ball_rTurn_right = robotconfig["AUTON"]["BALL_R"]["TURN_RIGHT"]
            if(self.timer.get()<self.ball_lForward_1):
                TankDrive.forward(1)
            elif(self.gyroAngle>self.ball_rTurn_left
                TankDrive.counterclockwise(1)
            elif(self.timer.get()<self.ball_rForward_2):
                TankDrive.forward(1)
            elif(self.gyroAngle<self.ball_rTurn_right):
                TankDrive.clockwise(1)
            elif(self.timer.get()<self.ball_rForward_3):
                TankDrive.forward(1)

            
        if(self.task=="BALL_L"):
            self.ball_lForward_1 = robotconfig["AUTON"]["BALL_L"]["FORWARD_1"]
            self.ball_lForward_2 = robotconfig["AUTON"]["BALL_L"]["FORWARD_2"]
            self.ball_lForward_3 = robotconfig["AUTON"]["BALL_L"]["FORWARD_3"]
            self.ball_lTurn_right = robotconfig["AUTON"]["BALL_L"]["TURN_RIGHT"]
            self.ball_lTurn_left = robotconfig["AUTON"]["BALL_L"]["TURN_LEFT"]
            self.ballTurnTime = robotconfig["AUTON"]["BALL_TURN_TIME"]
        
        return
        """
    
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