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

}

visionConfig = {

}

launcherConfig = {
    "TOP_MOTOR_ID": 1,
    "BOTTOM_MOTOR_ID": 2,
    "INTAKE_SPEED": 0.1,
    "EJECT_SPEED": -0.1,

    "AIM_CAN_ID": 0,
    "AIM_MODULE_TYPE": wpilib.PneumaticsModuleType.CTREPCM,
    "AIM_FORWARD_CHANNEL": 0,
    "AIM_REVERSE_CHANNEL": 1,

    "EJECT_CAN_ID": 0,
    "EJECT_MODULE_TYPE": wpilib.PneumaticsModuleType.CTREPCM,
    "EJECT_FORWARD_CHANNEL": 2,
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
}