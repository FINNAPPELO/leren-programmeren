
gastheer = True
gasten = False
drank = True
chips = False
start_condition_1 = gastheer and gasten and drank
start_condition_2 =  gastheer or (gasten and drank and chips )
start_condition_3 =  gastheer and drank 
if start_condition_1 or start_condition_2 and start_condition_3:
    print('Start the Party')
else:
    print('No Party')