a = int(input("vul getal 1 in : "))
b = int(input("vul getal 2 in : "))
if a>b:
    max =a
    min = b
    print(f"a is het grootste getaal {max}")
    print(f"Het minimum is:{min}")
    print(f"Het maximum is:{max}")
elif a<b:
    min=a
    max = b 
    print(f"a is het klijnste getal {min}")
    print(f"Het minimum is:{min}")
    print(f"Het maximum is:{max}")
else:
    min = a
    max = b
    print("a en b zijn de zelfte waarde ")
    print(f"Het minimum is:{min}")
    print(f"Het maximum is:{max}")