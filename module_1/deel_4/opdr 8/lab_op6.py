from test_lib import test, report
from calc_discount_functie import calc_discount, MONTH_DISCOUNT_PERC, month_discount_brands
print(month_discount_brands)

price=1249.0
expect_content=124.90
brand=input("welk merk wil je? ")
calculated_content=calc_discount(price, brand, month_discount_brands, 0)
name= f'TEST'
test(name, expect_content, calculated_content)
report()

price=5900.0
expect_content=590.00
brand=input("welk merk wil je ? ")
calculated_content=calc_discount(price, brand, month_discount_brands, 0)
name= f'TEST'
test(name, expect_content, calculated_content)
report()