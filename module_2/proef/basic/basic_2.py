from RobotArm import RobotArm
from challenges.example import challenges
robotArm = RobotArm(challenges[2],0)
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
robotArm.moveRight()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.moveRight()
robotArm.drop()

robotArm.report()
