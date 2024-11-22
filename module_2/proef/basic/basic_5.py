from RobotArm import RobotArm


# Import the challenges (in this case challenges/example.py)
from challenges.example import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)
robotArm.help
robotArm.moveRight()
robotArm.grab()
kleur=robotArm.scan()
if kleur  == "red":
    robotArm.moveLeft()
else:
    robotArm.moveRight()
robotArm.drop()

robotArm.report()  