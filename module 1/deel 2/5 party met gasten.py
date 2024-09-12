agasten = int(input('hoeveel gasten zijn der? '))
naam = input('wat is de gast heer zij/haar naam? ')
gastheer = False
gasten = False
drank = True
chips = True
start_condition_1 = gastheer and gasten and drank
start_condition_2 =  gastheer or (gasten and drank and chips )
start_condition_3 =  gastheer and drank 
if naam.lower() == 'wilfred bouman'  :
    print('No Party')
elif naam.lower() == 'finn' or  (start_condition_1 or start_condition_2 and start_condition_3)  and  agasten>4 and agasten<20:
    print('Start the Party')
else:
    print('No Party')