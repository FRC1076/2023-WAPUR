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
    "TASK":"CRATE",
    # "TASK" is what the robot will do in auton. Options are on the lines below.
    # "CRATE" to push crate
    # "BALL_R" for pushing ball starting in the right corner
    # "BALL_L" for pushing ball starting in the left corner
    
    "GYRO_STARTING_VALUE":0, #Starting value of the gyroscope, in degrees
    "BALL_TURN_TIME":1.5, #Expected time for the turns while going for the ball

    #In the TASK_LISTs, the value after a FORWARD command is time time.
    #In the TASK_LISTs, the value after a TURN_LEFT or TURN_RIGHT is the target angle.
    'CRATE_TASK_LIST':{
        'FORWARD_1':3,
    },
    'BALL_R_TASK_LIST':{
        'FORWARD_1':1, 
        'TURN_LEFT':-90,
        'FORWARD_2':3,
        'TURN_RIGHT':0,
        'FORWARD_3':3,
    },
    'BALL_L_TASK_LIST':{
        'FORWARD_1',
        'TURN_RIGHT',
        'FORWARD_2',
        'TURN_LEFT',
        'FORWARD_3',
    },
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