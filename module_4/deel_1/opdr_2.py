def hello_function(getal: int) -> str:
    result = ""
    for i in range(1, getal + 1):
        result += f"Hello from function town {i}!\n"
    return result



print(hello_function(3))
print(" ")
print(hello_function(7))
