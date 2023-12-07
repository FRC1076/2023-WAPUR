class Controller:
    def __init__(self, config):
        self.xboxController = config[0]
        self.deadzone = config[1]
        self.leftTriggerAxis = config[2]
        self.rightTriggerAxis = config[3]