''' Task 1: Create a function to check if the number (num) is divisible by another number (divisor).
        - Both num and divisor must be numeric.
        - Return True if num is divisible by divisor, False otherwise.'''

# Defining the function that takes two parameters
def check_divisibility(num, divisor):
    
    # To guard against using bool values as either the num or divisor parameter
    if isinstance(num, bool) or isinstance (divisor, bool):
        return False
    
    # Numeric guard (i.e., num and divisor must be either an int or a float)
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return False
    
    # The zero guard because any number divided by 0 will result in a ZeroDivisionError
    if divisor == 0: 
        return False
    
    return num % divisor == 0

''' Task 2: Invoke the function "check_divisibility" using the following scenarios:
        - 10, 2
        - 7, 3'''

print(check_divisibility(10, 2))
print(check_divisibility(7, 3))
