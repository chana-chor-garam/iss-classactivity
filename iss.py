def is_narc(n):
    """Check if a number is narcissistic."""
    num_str = str(n)
    num_digits = len(num_str)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)  # Correct exponentiation
    
    return sum_of_powers == n  # Check if sum matches the original number

def print_narcis_numbers(start, end):
    """Print all narcissistic numbers in a given range."""
    for num in range(start, end + 1):
        if is_narc(num):  # Correct function call
            print(num)

# Correct function call
print_narcis_numbers(1000, 5000)
