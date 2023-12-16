from collections import namedtuple
import wpilib

DEADZONE = 0.1

# Drive Types
ARCADE = 1
TANK = 2
SWERVE = 3

controllerConfig = {
    "DRIVER": {
        "ID": 1,
        "DEADZONE": DEADZONE,
        "LEFT_TRIGGER_AXIS": 2,
        "RIGHT_TRIGGER_AXIS": 3,
    },
    "OPERATOR": {
        "ID": 2,
        "DEADZONE": DEADZONE,
        "LEFT_TRIGGER_AXIS": 2,
        "RIGHT_TRIGGER_AXIS": 3,
    }
}

swervometerConfig = {

}

drivetrainConfig = {
    "FRONT_RIGHT_ID": 5,
    "FRONT_LEFT_ID": 7,
    "REAR_RIGHT_ID": 3,
    "REAR_LEFT_ID": 2,
}

visionConfig = {

}

launcherConfig = {
    "TOP_MOTOR_ID": 4,
    "BOTTOM_MOTOR_ID": 1,
    "INTAKE_SPEED": 0.8,
    "EJECT_SPEED": -1,

    "PNEU_MODULE_TYPE": wpilib.PneumaticsModuleType.CTREPCM,
    "AIM_FORWARD_CHANNEL": 0,
    "AIM_REVERSE_CHANNEL": 2,

    "EJECT_FORWARD_CHANNEL": 1,
    "EJECT_REVERSE_CHANNEL": 3,
}

autonConfig = {
    "TASK":"BALL_START_L",
    # "TASK" is what the robot will do in auton. Options are on the lines below.
    # "CRATE" to push crate
    # "BALL_START_R" for pushing ball starting in the right corner
    # "BALL_START_L" for pushing ball starting in the left corner
    
    "GYRO_STARTING_VALUE":0, #Starting value of the gyroscope, in degrees
    "BALL_TURN_TIME":1.5, #Expected time for the turns while going for the ball

    #In the task lists, the value after a FORWARD command is time.
    #In the tasklists, the value after a CLOCKWISE or COUNTERCLOCKWISE is the absolute target angle.
    #In the tasklists, the value after a CLOCKWISE_RELATIVE_ANGLE or COUNTERCLOCKWISE_RELATIVE_ANGLE is the change in angle
    #STOPs stop the robot
    'CRATE':[ #Go for the crates by pushing them accross the line
        ["FORWARD", 2],
        ["STOP"],
    ],
    'BALL_START_R':[ #Going for the ball, starting in the right corner
        ["COUNTERCLOCKWISE_RELATIVE_ANGLE", 90],
        ["STOP"],
        ["FORWARD", 1],
        ["STOP"],
        ["CLOCKWISE", 0],
        ["STOP"],
        ["FORWARD", 1.5],
    ],
    'BALL_START_L':[ #Going for the ball, starting in the left corner
        ["CLOCKWISE_RELATIVE_ANGLE", 90],
        ["STOP"],
        ["FORWARD", 1],
        ["STOP"],
        ["COUNTERCLOCKWISE", 0],
        ["STOP"],
        ["FORWARD", 1.5],
    ]
}

MODULE_NAMES = namedtuple('MODULE_NAMES', [
])

loggingConfig = {

}

dashboardConfig = {

}

robotconfig = {
    "AUTON": autonConfig,
    "CONTROLLERS": controllerConfig,
    "DRIVETRAIN": drivetrainConfig,
    "LAUNCHER": launcherConfig,  
}