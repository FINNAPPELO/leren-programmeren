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

def format_ingredient(amount, unit, txt, is_piece=False):
    if is_piece:
        return f'{amount} {str_single_plural(amount, txt)}'
    else:
        return f'{str_amount_fraction(amount)} {str_units(amount, unit)} {txt}'

print(format_ingredient(amount_eggs, None, TXT_EGGS, is_piece=True))
print(format_ingredient(amount_milk, UNIT_MILK, TXT_MILK))
print(format_ingredient(amount_salt, UNIT_SALT, TXT_SALT))
print(format_ingredient(amount_pepper, UNIT_PEPPER, TXT_PEPPER))
print(format_ingredient(amount_oil, UNIT_OIL, TXT_OIL))
print(format_ingredient(amount_onions, None, TXT_ONIONS, is_piece=True))
print(format_ingredient(amount_garlics, None, TXT_GARLICS, is_piece=True))
print(format_ingredient(amount_paprikas, None, TXT_PAPRIKAS, is_piece=True))
print(format_ingredient(amount_spinach, UNIT_SPINACH, TXT_SPINACH))
print(format_ingredient(amount_cheese, UNIT_CHEESE, TXT_CHEESE))
print('-----------------------------------------------')