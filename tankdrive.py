import ctre
import wpilib
from navx import AHRS

class TankDrive:
    
    def __init__(self, config, gyro):
        print("initDrivetrain")
        self.motor1 = ctre.WPI_TalonSRX(config["FRONT_RIGHT"]["ID"])
        self.motor2 = ctre.WPI_TalonSRX(config["FRONT_LEFT"]["ID"])
        self.motor3 = ctre.WPI_TalonSRX(config["REAR_RIGHT"]["ID"])
        self.motor4 = ctre.WPI_TalonSRX(config["REAR_LEFT"]["ID"])
        self.left_side = wpilib.MotorControllerGroup(self.motor2, self.motor4)
        self.right_side = wpilib.MotorControllerGroup(self.motor1, self.motor3)

        self.drive = wpilib.drive.DifferentialDrive(self.left_side, self.right_side)
        #self.gyro= AHRS.create_spi(wpilib._wpilib.SPI.Port.)
        self.gyro = gyro
        
        # # Create Drivetrain
        # return wpilib.drive.DifferentialDrive(left_side, right_side)

    def forward(self, speed):
        self.drive.arcadeDrive(0,-speed)
    
    def backward(self, speed):
        self.drive.arcadeDrive(0,speed)

    def counterclockwise(self, speed):
        self.drive.arcadeDrive(-speed, 0)

    def clockwise(self, speed):
        self.drive.arcadeDrive(speed,0)
    
    def stop(self):
        self.drive.arcadeDrive(0, 0)
    
    def getTankDrive(self):
        return self.drive
    
    def getGyro(self):
        return self.gyro