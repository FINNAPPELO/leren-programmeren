from RobotArm import RobotArm


# Import the challenges (in this case challenges/example.py)
from challenges.beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)
robotArm.moveRight()
for i in range (6):
    robotArm.grab()
    kleur=robotArm.scan()
    if  kleur == "white":
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    elif kleur == 'red':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        exit()
robotArm.report()