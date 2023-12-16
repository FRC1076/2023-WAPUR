import ctre
import wpilib

class TankDrive:
    def __init__(self, config):
        print("initDrivetrain")
        self.motor1 = ctre.WPI_TalonSRX(config["FRONT_RIGHT_ID"])
        self.motor2 = ctre.WPI_TalonSRX(config["FRONT_LEFT_ID"])
        self.motor3 = ctre.WPI_TalonSRX(config["REAR_RIGHT_ID"])
        self.motor4 = ctre.WPI_TalonSRX(config["REAR_LEFT_ID"])
        self.left_side = wpilib.MotorControllerGroup(self.motor1, self.motor2)
        self.right_side = wpilib.MotorControllerGroup(self.motor3, self.motor4)

        self.drive = wpilib.drive.DifferentialDrive(self.left_side, self.right_side)
        return

    def forward(self, speed):
        self.drive.tankDrive(speed,-speed)
    
    def backward(self, speed):
        self.drive.tankDrive(-speed,speed)

    def counterclockwise(self, speed):
        self.drive.tankDrive(-speed,-speed)

    def clockwise(self, speed):
        self.drive.tankDrive(speed,speed)