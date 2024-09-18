naam = input('wat is de gast heer zij/haar naam? ')
gastheer = False
gasten = True
drank = True
chips = True
start_condition_1 = gastheer and gasten and drank
start_condition_2 =  gastheer or (gasten and drank and chips )
start_condition_3 =  gastheer and drank 
if naam.lower() == 'finn' or  start_condition_1 or start_condition_2 or start_condition_3 and not naam.lower()=='wilfred bouman':
    print('Start the Party')
else:
    print("no party")