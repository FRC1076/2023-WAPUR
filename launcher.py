import wpilib
import wpilib.drive
import wpimath.controller
from wpimath.controller import PIDController
import rev
from wpilib import DoubleSolenoid
import ctre

class Launcher:
    def __init__(self, config):
        self.launchTimer = wpilib.Timer()

        self.inEjectingPhase = False

        self.topMotor = ctre.WPI_TalonSRX(config["TOP_MOTOR_ID"]) # launcher top-bottom
        self.bottomMotor = ctre.WPI_TalonSRX(config["BOTTOM_MOTOR_ID"]) # launcher top-bottom

        # CAN ID
        # module type
        # forward port
        # backward port, piston configuration name
        #self.ejectPiston =  DoubleSolenoid(config["EJECT_CAN_ID"],config["EJECT_MODULE_TYPE"],
        #                                config["EJECT_FORWARD_CHANNEL"], config["EJECT_REVERSE_CHANNEL"]) 
        #                                # piston responsible for pushing ball out
        #self.aimPiston = DoubleSolenoid(config["AIM_CAN_ID"],config["AIM_MODULE_TYPE"],
        #                                config["AIM_FORWARD_CHANNEL"], config["AIM_REVERSE_CHANNEL"]) 
        self.ejectPiston =  DoubleSolenoid(moduleType=config["EJECT_MODULE_TYPE"],
                                        forwardChannel=config["EJECT_FORWARD_CHANNEL"], reverseChannel=config["EJECT_REVERSE_CHANNEL"]) 
                                        # piston responsible for pushing ball out
        self.aimPiston = DoubleSolenoid(moduleType=config["AIM_MODULE_TYPE"],
                                        forwardChannel=config["AIM_FORWARD_CHANNEL"], reverseChannel=config["AIM_REVERSE_CHANNEL"]) 
                                        # piston responsible for aiming the launcher
        self.ejectSpeed = config["EJECT_SPEED"]
        self.config = config

        # uses the motors                  
    def intake(self):
        intakeSpeed = self.config["INTAKE_SPEED"]
        self.topMotor.set(intakeSpeed)
        self.bottomMotor.set(intakeSpeed)
        
    def startEject(self):
        self.inEjectingPhase = True 
        self.launchTimer.reset()

        # uses the pistons
    def eject(self):
        self.launchTimer.start()
        currentTimer = self.launchTimer.get()

        # gets the motors running before ejecting
        self.topMotor.set(self.ejectSpeed)
        self.bottomMotor.set(self.ejectSpeed)
        
        #if eject doesn't finish before it is called again, will the pistons be in an awkward location?

        # extending piston, then retracting it and getting rid of the timer
        if currentTimer > 1.0 and currentTimer < 2.0:
            self.ejectPiston.set(wpilib.DoubleSolenoid.Value.kForward)
            print("piston forward")
        elif currentTimer > 2.0 and currentTimer < 3.0:
            self.ejectPiston.set(wpilib.DoubleSolenoid.Value.kReverse)
            print("piston reverse")
        elif currentTimer > 3.0:
            print("stuff done")
            self.launchTimer.stop()

            #ends the ejecting motion
            self.inEjectingPhase = False

    def aimDown(self):
        self.aimPiston.set(wpilib.DoubleSolenoid.Value.kForward)

    def aimUp(self):
        self.aimPiston.set(wpilib.DoubleSolenoid.Value.kReverse)
    
    def stop(self):
        self.topMotor.set(0)
        self.bottomMotor.set(0)