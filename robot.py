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

from robotconfig import robotconfig, MODULE_NAMES
from controller import Controller
from launcher import Launcher
from tankdrive import TankDrive

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        controllers = self.initControllers(robotconfig["CONTROLLERS"])
        self.driver = controllers[0]
        self.operator = controllers[1]
        self.launcher = Launcher(robotconfig["LAUNCHER"])
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
    
    def initAuton(self, config):
        return
    
    def teleopInit(self):
        return

    def robotPeriodic(self):
        return True
    
    # left bumper = intake
    # right bumper = eject
    # y = AimUp
    # a = AimDown
    def teleopPeriodic(self):

        if self.operator.xboxController.getYButtonPressed():
            self.launcher.aimUp()

        if self.operator.xboxController.getLeftBumper():
            self.launcher.intake()
        else:
            self.launcher.stop()

        if self.operator.xboxController.getAButtonPressed():
            self.launcher.aimDown()

        #called once when button is released, which gets the launcher into ejecting mode
        if self.operator.xboxController.getRightBumperReleased():
            self.launcher.startEject()

        #if in ejecting mode, run the eject function
        if self.launcher.inEjectingPhase:
            self.launcher.eject()
        
        self.teleopDrivetrain()

        return
    
    def teleopDrivetrain(self):
        self.drivetrain.getTankDrive().arcadeDrive(self.driver.xboxController.getRightX()/2, self.driver.xboxController.getLeftY())
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