def generate_fibonacci(n):

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_list = [0, 1]
    for i in range(2, n):
        next_fib = fib_list[i-1] + fib_list[i-2]
        fib_list.append(next_fib)
    return fib_list

def calculate_golden_ratio(last, second_last):
    
    if second_last == 0:
        return 0  
    return last / second_last


def main():
    num_terms = 10
    
    fib_sequence = generate_fibonacci(num_terms)
    
    print(", ".join(map(str, fib_sequence)))
    
    if len(fib_sequence) >= 2:
        golden_ratio = calculate_golden_ratio(fib_sequence[-1], fib_sequence[-2])
        print(f"Gulden snede: {golden_ratio}")
    else:
        print("Niet genoeg getallen om gulden snede te berekenen.")

if __name__ == "__main__":
    main()