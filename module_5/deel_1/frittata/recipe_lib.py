import math

UNIT_PIECES = 'piece'
UNIT_SPOONS = 'spoon'
UNIT_TEASPOONS = 'teaspoon'
UNIT_CUPS = 'cup'

TXT_PIECES = '|'
TXT_SPOONS = 'eetlepel|eetlepels'
TXT_TEASPOONS = 'theelepel|theelepels'
TXT_CUPS = 'kopje|kopjes'

# failsafe input of a number of persons
def input_nr_persons(prompt: str) -> int:
  while True:
    try:
      nr_persons = int(input(prompt))
      if nr_persons > 0: 
        return nr_persons
      print('getal moet groter zijn dan 0')
    except:
      print('voer een geldig geheel getal in!')


def round_piece(amount: float) -> int:
  return math.ceil(amount)

def round_quarter(amount: float) -> float:
  if amount >= 10:
    return round(amount)
  else:
    quarters = amount * 4
    remainder = quarters - math.floor(quarters)
    if remainder >= 0.5:
      return math.ceil(quarters) / 4
    else:
      return math.floor(quarters) / 4


def str_single_plural(amount: float, txt: str) -> str:
  parts = txt.split("|")
  return parts[0] if amount == 1 else parts[1]


def str_units(amount: float, unit: str) -> str:
  if unit == UNIT_SPOONS:
    return str_single_plural(amount, TXT_SPOONS)
  elif unit == UNIT_TEASPOONS:
    return str_single_plural(amount, TXT_TEASPOONS)
  elif unit == UNIT_CUPS:
    return str_single_plural(amount, TXT_CUPS)
  else:
    return unit


TXT_FRACTIONS = ('','¼','½','¾')
def str_amount_fraction(amount: float) -> str:  
  amount = round_quarter(amount) 
  ints = int(amount)
  quarter = int((amount - ints) / 0.25)
  str_ints = str(ints) if ints > 0 else ''
  return str_ints + TXT_FRACTIONS[quarter]


ML_SPOON = 15 
ML_TEASPOON = 5
ML_CUP = 240 

def unit2ml(amount: float, unit: str) -> float:
  pass

GRAM_PER_ML_SALT = 1.2
GRAM_PER_ML_PEPPER = 0.3
GRAM_PER_ML_CHEESE = 0.45
GRAM_PER_ML_SPINACH = 0.15

def ml2gram(amount_ml: float, gram_per_ml: float) -> float:
  pass

