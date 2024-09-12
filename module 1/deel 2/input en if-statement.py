a = int(input("vul getal 1 in : "))
b = int(input("vul getal 2 in : "))
if a>b:
    max =a
    min = b
    print(f"a is het grootste getaal {max}")
elif a<b:
    min=a
    max = b 
    print(f"a is het klijnste getal {min}")
else:
    print("a en b zijn de zelfte waarde ")