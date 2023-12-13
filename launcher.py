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
        #self.inEjectingPhase = False

        self.topMotor = ctre.TalonSRX(config["TOP_MOTOR_ID"]) # launcher top-bottom
        self.bottomMotor = ctre.TalonSRX(config["BOTTOM_MOTOR_ID"]) # launcher top-bottom
        # CAN ID
        # module type
        # forward port
        # backward port, piston configuration name
        self.ejectPiston =  DoubleSolenoid(config["EJECT_CAN_ID"],config["EJECT_MODULE_TYPE"],
                                        config["EJECT_FORWARD_CHANNEL"], config["EJECT_REVERSE_CHANNEL"]) 
                                        # piston responsible for pushing ball out
        self.aimPiston = DoubleSolenoid(config["AIM_CAN_ID"],config["AIM_MODULE_TYPE"],
                                        config["AIM_FORWARD_CHANNEL"], config["AIM_REVERSE_CHANNEL"]) 
                                        # piston responsible for aiming the launcher

        # uses the motors                  
    def intake(self):
        intakeSpeed = self.config["INTAKE_SPEED"]
        self.topMotor.set(intakeSpeed)
        self.bottomMotor.set(intakeSpeed)
        

        # uses the pistons
    def eject(self):
        ejectSpeed = self.config["EJECT_SPEED"]
        
        self.launchTimer.start()
        currentTimer = self.launchTimer.get()

        #if inEjecting Phase:

        # gets the motors running before ejecting
        self.topMotor.set(ejectSpeed)
        self.bottomMotor.set(ejectSpeed)

        if currentTimer < 1.0:
            print("motors starting up")

        # extending piston, then retracting it and getting rid of the timer
        if currentTimer > 1.0 and currentTimer < 2.0:
            self.ejectPiston.set(wpilib.DoubleSolenoid.Value.kForward)
            print("piston is extending")
        elif currentTimer > 2.0 and currentTimer < 3.0:
            self.ejectPiston.set(wpilib.DoubleSolenoid.Value.kReverse)
            print("piston is retracting")
        else:
            print("stuff completed")
            self.launchTimer.stop()
            self.launchTimer.reset()
            #self.inEjectingPhase = False
        
            
        
        # extend ejectPiston

    def aimDown(self):
        # retract aimPiston

        self.aimPiston.set(wpilib.DoubleSolenoid.Value.kReverse)

    def aimUp(self):
        # extend aimPiston
        self.aimPiston.set(wpilib.DoubleSolenoid.Value.kForward)