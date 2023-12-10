import wpilib
import wpilib.drive
import wpimath.controller
from wpimath.controller import PIDController
import rev
from wpilib import DoubleSolenoid
import ctre

class Launcher:
    def __init__(self, config):

        
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
        self.topMotor.set(ejectSpeed)
        self.bottomMotor.set(ejectSpeed)
        
        # extend ejectPiston

    def aimDown(self):
        # retract aimPiston

        self.aimPiston.set(wpilib.DoubleSolenoid.Value.kReverse)

    def aimUp(self):
        # extend aimPiston
        self.aimPiston.set(wpilib.DoubleSolenoid.Value.kForward)