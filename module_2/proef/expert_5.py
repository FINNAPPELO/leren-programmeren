from RobotArm import RobotArm
from challenges.expert import challenges

robotArm = RobotArm(challenges[5], 0)

color_counts = {'red': 0, 'green': 0, 'blue': 0}
for _ in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color in color_counts:
        color_counts[color] += 1
    robotArm.drop()
    robotArm.moveRight()

most_common_color = max(color_counts, key=lambda c: (color_counts[c], -ord(c[0])))

for _ in range(9):
    robotArm.moveLeft() 
robotArm.moveRight()

for _ in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == most_common_color:
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    else:
        robotArm.drop()
    robotArm.moveRight()

robotArm.report()