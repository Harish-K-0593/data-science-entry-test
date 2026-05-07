''' Task 1: Create a function that reverses a given string (s)
    - s MUST be a string
    - return the reversed strins
'''

def string_reverse(s):
    if not isinstance(s, str):
        return -1
    
    # Slice notation to reverse the string. We have to recall every single character from the lst character [-1]. Recall slicing range/sequence [start:stop:step]
    return s[::-1]


''' Task 2: Invoke the function "string_reverse" using the following scenarios:
    - "Hello World"
    - "Python"
'''
print(string_reverse("Hello World")) 
print(string_reverse("Python"))








