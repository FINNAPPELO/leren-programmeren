#import hier je functie "from [bestandsnaamZonderExtentie] import [functieNaam]"
from test_lib import test, report
from De_grootste_function import getal

expected = 'bijde getallen zijn eve groot' #resultaat
result = getal(2, 2) #roep hier je functie aan met 2 dezelfde getallen
test('TEST nr1=nr2', expected, result)

expected = "Maximum: 19 en minimum: 5" #resultaat
result = getal(19,5) #roep hier je functie aan waar nr1 groter is dan nr2
test('TEST nr1>nr2', expected, result)

expected = "Maximum: 34 en minimum: 4"
result = getal(4,34) #roep hier je functie aan  waar nr1 kleiner is dan nr2
test('TEST nr1<nr2', expected, result)

if __name__ == "__main__":
    report()
getal(1,5)