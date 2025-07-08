
import functions 
from calculations import calculations  
from test_lib import test, report  

test("Addition", functions.addition(5, 3), calculations["addition"](5, 3))

test("Addition with negative", functions.addition(10, -2), calculations["addition"](10, -2))

test("Subtraction", functions.subtraction(9, 4), calculations["subtraction"](9, 4))

test("Subtraction with negative", functions.subtraction(5, 10), calculations["subtraction"](5, 10))

test("Multiplication", functions.multiplication(7, 3), calculations["multiplication"](7, 3))

test("Multiplication with negative", functions.multiplication(-2, 6), calculations["multiplication"](-2, 6))

test("Division", functions.division(10, 2), calculations["division"](10, 2))

test("Division by zero", functions.division(5, 0), calculations["division"](5, 0)) 
report()
