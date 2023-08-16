#doctest: python -m doctest -v filename

def is_even_odd(number):
    '''
    >>>
    
    '''
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

def is_perfect(number):
    if number <= 0:
        return False
    divisors = [1]
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors.extend([i, number//i])
    return sum(divisors) == number

def is_armstrong(number):
    num_str = str(number)
    power = len(num_str)
    total = sum(int(digit)**power for digit in num_str)
    return total == number
'''

# Test cases
def test_functions():
    test_numbers = [2, 7, 11, 121, 12321, 28, 6, 496, 153]
    
    for num in test_numbers:
        print(f"Number: {num}")
        print("Even/Odd:", is_even_odd(num))
        print("Prime:", is_prime(num))
        print("Palindrome:", is_palindrome(num))
        print("Perfect:", is_perfect(num))
        print("Armstrong:", is_armstrong(num))
        print("=" * 30)

test_functions()
'''