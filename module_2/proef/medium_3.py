from RobotArm import RobotArm
from challenges.medium import challenges
robotArm = RobotArm(challenges[3],0)
for i in range(8):
    robotArm.moveRight()
for i in range (8):
    robotArm.grab()
    kleur=robotArm.scan()
    if kleur == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()





robotArm.report()