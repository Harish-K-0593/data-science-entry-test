''' Task 1: Create a function that searches for all occurances of a value (find_val) in a given list (lst) and replaces them with another value (replace val).

    - 1st must be a list
    - Return the modified list
'''



# Defining the function with 3 parameters: lst to search, value to find, and value to replace
def find_and_replace(lst, find_val, replace_val):
    
    # Set the conditions to ensure that lst is a list and nothing else.
    if not isinstance (lst, list):
        return -1
    
    # iterate throught the list and get the position i and the value at theat position on each iteration.
    # To use enumerate(lst) to produce (index, value) pairs as we go

    for i, value in enumerate(lst):
        
        # If the current value equals what we're looking for, we use the index i to write replace_val back to that exact position in the list.
        if value == find_val:
            lst[i] = replace_val

    return lst


''' Task 2: Invoke the function "find_and_replace" using the following scenarios:
    - [1, 2, 3, 4, 2, 2], 2, 5
    - ["apple", "banana", "apple"], "apple", "orange"
'''
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
