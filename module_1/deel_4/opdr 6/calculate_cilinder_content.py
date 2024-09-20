
import math

def calculate_cilinder_content(diameter:float, hight:float ):
    return round((diameter/2)*(diameter/2)*math.pi*hight,1)
print(calculate_cilinder_content(8,5))