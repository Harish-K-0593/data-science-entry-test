''' Task 1:
    # 1. Swap two values (only using x and y) with NO thrid helper variable
    # 2. Both inputs must be numeric (integer or float). If either one is not, return "-1"
    # 3. If both are numeric, print the swapped values
'''

# Defining the function swap with 2 parameters and setting the conditions that x & 7 must be either an integer or a float. To take note that Boolean Values are also read as integers in Python.
def swap(x,y):
    if isinstance (x, bool) or isinstance (y, bool) or not isinstance(x, (int, float)) or not isinstance (y, (int, float)): 
        return -1
    
    # The swap. The right-hand sided y,x creates a tuple of the current values.
    x, y = y, x
    
    # Formatted string allows anything inside the curly braces to to get evaluated as Python code and inserted into the f string.
    print(f"x = {x}, y = {y}")
    
# Test: Calling the function must return x = 1000 & y = 10.    
swap(10,1000)

# ------------------------------------------------------------------------------------------------------ #

''' Task 2: invoke (call/run/execute) the swap function using the following scenarios:
'''
        
print(swap("Apple",10)) 
# "Apple" is not numeric -> function returns -1

swap(9,17) 
# Both numeric -> prints "x = 17, y = 9"

