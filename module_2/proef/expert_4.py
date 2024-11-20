from RobotArm import RobotArm
from challenges.expert import challenges

robotArm = RobotArm(challenges[4], 0)


stapel_rood = 7 
stapel_groen = 8 
stapel_blauw = 9   
for i in range(6): 
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == "red":
        while robotArm.stackIndex() < stapel_rood:
            robotArm.moveRight()
        robotArm.drop()
    elif kleur == "green":
        while robotArm.stackIndex() < stapel_groen:
            robotArm.moveRight()
        robotArm.drop()
    elif kleur == "blue":
        while robotArm.stackIndex() < stapel_blauw:
            robotArm.moveRight()
        robotArm.drop()
    else:
        continue
    while robotArm.stackIndex() > i + 1:
        robotArm.moveLeft()
    while robotArm.stackIndex() < i + 1:
        robotArm.moveRight()
robotArm.report()
