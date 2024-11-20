from RobotArm import RobotArm


# Import the challenges (in this case challenges/example.py)
from challenges.example import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[1],0)
robotArm.moveRight()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.drop()
robotArm.report()
