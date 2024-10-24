from RobotArm import RobotArm
# Import the challenges (in this case challenges/example.py)
from challenges.example import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)
robotArm.grab()
for i in range(9):
    robotArm.moveRight()
robotArm.drop()


robotArm.report()