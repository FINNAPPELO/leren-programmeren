from RobotArm import RobotArm

from challenges.expert import challenges

robotArm = RobotArm(challenges[1],0)
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
for i in range(4):
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(5):
        robotArm.moveLeft()
robotArm.moveLeft()
for i in range(3):
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(5):
        robotArm.moveLeft()
robotArm.moveLeft()


for i in range(2):
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(5):
        robotArm.moveLeft()
robotArm.moveLeft()
for i in range(1):
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(5):
        robotArm.moveLeft()


robotArm.report()
