from RobotArm import RobotArm


# Import the challenges (in this case challenges/example.py)
from challenges.example import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)
#robotArm.showSolution()
#robotArm.wait()
robotArm.grab()
for i in range (2):
    robotArm.moveRight()
robotArm.drop()
for i in range (2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveRight()
robotArm.grab()
for i in range (2):
    robotArm.moveLeft()
robotArm.drop()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()



robotArm.report()