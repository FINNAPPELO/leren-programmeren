from RobotArm import RobotArm
from challenges.medium import challenges
robotArm = RobotArm(challenges[2],0)
for i in range(4):
    robotArm.moveRight()
    for i in range(6) :
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    robotArm.moveRight()
for i in range(6) :
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()



robotArm.report()