from RobotArm import RobotArm

from challenges.expert import challenges

robotArm = RobotArm(challenges[2],0)


row_length = 10

for current_position in range(row_length):  
    robotArm.grab()
    
    if robotArm.scan() == 'red':
        steps_to_end = row_length - 1 - current_position
        
        for _ in range(steps_to_end):
            robotArm.moveRight()
        robotArm.drop()
        
        for _ in range(steps_to_end):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    
    if current_position < row_length - 1:
        robotArm.moveRight()

robotArm.report()