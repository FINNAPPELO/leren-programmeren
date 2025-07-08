from functions import *
from test_lib1 import test, report

expected = [2, 3, 5, 7]
result = priemgetallen_tot(10)
test('TEST: priemgetallen_tot_en_met(10)', expected, result)

expected = []
result = priemgetallen_tot(1)
test('TEST: priemgetallen_tot_en_met(1)', expected, result)

expected = [2, 3, 5, 7, 11]
result = eerste_priemgetallen(5)
test('TEST: eerste_n_priemgetallen(5)', expected, result)

expected = [2]
result = eerste_priemgetallen(1)
test('TEST: eerste_n_priemgetallen(1)', expected, result)

expected = [11, 13, 17, 19]
result = priemgetallen_in_bereik(10, 20)
test('TEST: priemgetallen_tussen(10,20)', expected, result)

expected = []
result = priemgetallen_in_bereik(14, 16)
test('TEST: priemgetallen_tussen(14,16)', expected, result)

report()