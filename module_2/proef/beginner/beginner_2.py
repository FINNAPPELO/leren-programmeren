from RobotArm import RobotArm


# Import the challenges (in this case challenges/example.py)
from challenges.beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)
robotArm.moveRight()
for i in range(6):
    robotArm.grab()
    kleur=robotArm.scan()
    if kleur == "green":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
robotArm.report()