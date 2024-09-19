num1 = int(input("vul getal 1 in : "))
num2 = int(input("vul getal 2 in : "))
if num1>num2:
    max =num1
    min = num2
    print(f"a is het grootste getaal {max}")
    print(f"Het minimum is:{min}")
    print(f"Het maximum is:{max}")
elif num1<num2:
    min=num1
    max = num2 
    print(f"a is het klijnste getal {min}")
    print(f"Het minimum is:{min}")
    print(f"Het maximum is:{max}")
else:
    min = num1
    max = num2
    print("a en b zijn de zelfte waarde ")
    print(f"Het minimum is:{min}")
    print(f"Het maximum is:{max}")