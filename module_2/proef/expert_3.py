from RobotArm import RobotArm
from challenges.expert import challenges

robotArm = RobotArm(challenges[3], 0)

drop_position = 1

while True:
    robotArm.grab()
    if robotArm.scan() == '':
        break
    for _ in range(drop_position):
        robotArm.moveRight()
    robotArm.drop()

    for _ in range(drop_position):
        robotArm.moveLeft()

    drop_position += 1
robotArm.report()