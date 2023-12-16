from collections import namedtuple
import wpilib

DEADZONE = 0.1

# Drive Types
ARCADE = 1
TANK = 2
SWERVE = 3

controllerConfig = {
    "DRIVER": {
        "ID": 0,
        "DEADZONE": DEADZONE,
        "LEFT_TRIGGER_AXIS": 2,
        "RIGHT_TRIGGER_AXIS": 3,
    },
    "OPERATOR": {
        "ID": 1,
        "DEADZONE": DEADZONE,
        "LEFT_TRIGGER_AXIS": 2,
        "RIGHT_TRIGGER_AXIS": 3,
    }
}

swervometerConfig = {

}

drivetrainConfig = {
    "FRONT_RIGHT_ID": 0,
    "FRONT_LEFT_ID": 1,
    "REAR_RIGHT_ID": 2,
    "REAR_LEFT_ID": 3,
}

visionConfig = {

}

launcherConfig = {
    "TOP_MOTOR_ID": 4,
    "BOTTOM_MOTOR_ID": 1,
    "INTAKE_SPEED": 0.8,
    "EJECT_SPEED": -0.6,

    "PNEU_MODULE_TYPE": wpilib.PneumaticsModuleType.CTREPCM,
    "AIM_FORWARD_CHANNEL": 0,
    "AIM_REVERSE_CHANNEL": 2,

    "EJECT_FORWARD_CHANNEL": 1,
    "EJECT_REVERSE_CHANNEL": 3,
}

autonConfig = {

}

MODULE_NAMES = namedtuple('MODULE_NAMES', [
])

loggingConfig = {

}

dashboardConfig = {

}

robotconfig = {
    "CONTROLLERS": controllerConfig,
    "LAUNCHER": launcherConfig,  
    "DRIVETRAIN": drivetrainConfig,
}