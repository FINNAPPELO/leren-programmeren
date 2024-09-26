
month_discount_brands = ['Vespa','Kymco','Yamama']
price = 1249.00
MONTH_DISCOUNT_PERC = 10
def calc_discount(price: float, brand: str, month_discount_brands: str,  discound: float ) -> float:
    if brand in month_discount_brands:
        discound = price/100*MONTH_DISCOUNT_PERC
        return discound
    else:
        return discound