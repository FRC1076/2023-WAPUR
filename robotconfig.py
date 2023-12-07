from collections import namedtuple

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
    "FRONT_RIGHT": {
        "ID": 5,
    },
    "FRONT_LEFT": {
        "ID": 7,
    },
    "REAR_RIGHT": {
        "ID": 3,
    },
    "REAR_LEFT": {
        "ID": 2,
    },
}

visionConfig = {

}

elevatorConfig = {

}

grabberConfig = {

}

autonConfig = {
    "TASK":"BALL_START_L",
    # "TASK" is what the robot will do in auton. Options are on the lines below.
    # "CRATE" to push crate
    # "BALL_R" for pushing ball starting in the right corner
    # "BALL_L" for pushing ball starting in the left corner
    
    "GYRO_STARTING_VALUE":0, #Starting value of the gyroscope, in degrees
    "BALL_TURN_TIME":1.5, #Expected time for the turns while going for the ball

    #In the task lists, the value after a FORWARD command is time time.
    #In the tasklists, the value after a CLOCKWISE or COUNTERCLOCKWISE is the target angle.
    #STOPs don't actually seem to be neccesary, as long as the robot is set up to brake when the drive command ends.
    'CRATE':[ #Go for the crates by pushing them accross the line
        ["FORWARD", 2],
        ["STOP"],
    ],
    'BALL_START_R':[ #Going for the ball, starting in the right corner
        ["COUNTERCLOCKWISE", 90],
        ["STOP"],
        ["FORWARD", 1],
        ["STOP"],
        ["CLOCKWISE", 0],
        ["STOP"],
        ["FORWARD", 1.5],
    ],
    'BALL_START_L':[ #Going for the ball, starting in the left corner
        ["CLOCKWISE", 270],
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
    "CONTROLLERS": controllerConfig,
    "DRIVETRAIN": drivetrainConfig,
    "AUTON": autonConfig,
}