from RobotArm import RobotArm
from challenges.expert import challenges

robotArm = RobotArm(challenges[3], 0)

drop_position = 1

while True:
    if robotArm.stackEmpty() ==True :
        break
    robotArm.grab()
    for _ in range(drop_position):
        robotArm.moveRight()
    robotArm.drop()

    for _ in range(drop_position):
        robotArm.moveLeft()

    drop_position += 1
robotArm.report()