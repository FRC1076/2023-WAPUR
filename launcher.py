import wpilib
import wpilib.drive
import wpimath.controller
from wpimath.controller import PIDController
import rev

class Launcher:
    def __init__(self, config):

        motorType = rev.CANSparkMaxLowLevel.MotorType.kBrushless
        self.topMotor = rev.CANSparkMax(config["TOP_MOTOR_ID"], motorType) # launcher top-bottom
        self.bottomMotor = rev.CANSparkMax(config["BOTTOM_MOTOR_ID"], motorType) # launcher top-bottom

        # unsure how pistons work, however this is a similar layout to motorType
        self.pistonType = # piston configuration name
        self.ejectPiston =  # piston responsible for pushing ball out
        self.aimPiston = # piston responsible for aiming the launcher
                              
    def intake(self):
        intakeSpeed = self.config["INTAKE_SPEED"]
        self.topMotor.set(intakeSpeed)
        self.bottomMotor.set(intakeSpeed)

    def eject(self):
        ejectSpeed = self.config["EJECT_SPEED"]
        self.topMotor.set(ejectSpeed)
        self.bottomMotor.set(ejectSpeed)
        # extend ejectPiston

    def aimDown(self):
        # retract aimPiston

    def aimUp(self):
        # extend aimPiston