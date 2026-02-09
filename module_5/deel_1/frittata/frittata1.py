from recipe_lib import *
from frittata_ingredients import *


print('=============== Frittata recept ===============')

nr_persons = input_nr_persons('Aantal personen: ')

factor = nr_persons / RECIPE_PERSONS

amount_eggs = round_piece(AMOUNT_EGGS * factor)

amount_milk = round_quarter(AMOUNT_MILK * factor)

amount_salt = round_quarter(AMOUNT_SALT * factor)

amount_pepper = round_quarter(AMOUNT_PEPPER * factor)

amount_oil = round_quarter(AMOUNT_OIL * factor)

amount_onions = round_piece(AMOUNT_ONIONS * factor)

amount_garlics = round_piece(AMOUNT_GARLICS * factor)

amount_spinach = round_quarter(AMOUNT_SPINACH * factor)

amount_paprikas = round_piece(AMOUNT_PAPRIKAS * factor)

amount_cheese = round_quarter(AMOUNT_CHEESE * factor)

print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')

def get_form(amount, text):
    parts = text.split("|")
    return parts[0] if amount == 1 else parts[1]

print(f'{amount_eggs} {get_form(amount_eggs, TXT_EGGS)}')
print(f'{amount_milk} {get_form(amount_milk, TXT_CUPS)}')
print(f'{amount_salt} {get_form(amount_salt, TXT_TEASPOONS)}')
print(f'{amount_pepper} {get_form(amount_pepper, TXT_TEASPOONS)}')
print(f'{amount_oil} {get_form(amount_oil, TXT_SPOONS)}')
print(f'{amount_onions} {get_form(amount_onions, TXT_ONIONS)}')
print(f'{amount_garlics} {get_form(amount_garlics, TXT_GARLICS)}')
print(f'{amount_paprikas} {get_form(amount_paprikas, TXT_PAPRIKAS)}')
print(f'{amount_spinach} {get_form(amount_spinach, TXT_CUPS)}')
print(f'{amount_cheese} {get_form(amount_cheese, TXT_CUPS)}')
print('-----------------------------------------------')