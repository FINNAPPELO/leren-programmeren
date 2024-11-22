from RobotArm import RobotArm
from challenges.expert import challenges

robotArm = RobotArm(challenges[5], 0)

rood =0
blauw=0
geel=0
stapel_meestekleur=0
for i in range (9):
    robotArm.moveRight()
    robotArm.grab()
    kleur=robotArm.scan()
    robotArm.drop()
    if kleur=='red':
        rood+=1
    elif kleur=='blue':
        blauw+=1
    else:
        geel+=1
for i in range(9):
    robotArm.moveLeft()
if rood > blauw and rood > geel:
    for i in range (9):
        robotArm.moveRight()
        robotArm.grab()
        kleur_1=robotArm.scan()
        if kleur_1=='red':
            plek=robotArm.stackIndex()
            while robotArm.stackIndex() > stapel_meestekleur:
                robotArm.moveLeft()
            robotArm.drop()
            for i in range (plek):
                robotArm.moveRight()
        else:
            robotArm.drop()
elif blauw>rood and blauw>geel:
    for i in range (9):
        robotArm.moveRight()
        robotArm.grab()
        kleur_1=robotArm.scan()
        if kleur_1=='blue':
            plek=robotArm.stackIndex()
            while robotArm.stackIndex() > stapel_meestekleur:
                robotArm.moveLeft()
            robotArm.drop()
            for i in range (plek):
                robotArm.moveRight()
        else:
            robotArm.drop()
elif geel>rood and geel>blauw:
    for i in range (9):
        robotArm.moveRight()
        robotArm.grab()
        kleur_1=robotArm.scan()
        if kleur_1=='yellow':
            plek=robotArm.stackIndex()
            while robotArm.stackIndex() > stapel_meestekleur:
                robotArm.moveLeft()
            robotArm.drop()
            for i in range (plek):
                robotArm.moveRight()
        else:
            robotArm.drop()
else:
    print('.')
  
    robotArm.moveRight()
    robotArm.grab()
    kleur_2=robotArm.scan()
    robotArm.drop()
    for i in range (9):
        robotArm.grab()
        if robotArm.scan()==kleur_2:
            plek=robotArm.stackIndex()
            while robotArm.stackIndex() > stapel_meestekleur:
                robotArm.moveLeft()
            robotArm.drop()
            robotArm.moveRight()
            for i in range (plek):
                robotArm.moveRight()
        else:
            robotArm.drop()
            robotArm.moveRight()

print(rood)
print(blauw)
print(geel)
robotArm.report()
