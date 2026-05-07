''' Task 1: Create a funtion that updates a dictionary (dct) with a new key-value pair. 
    Conditions: 
    1. If the key already exists in the dct, print the original value, then update its value
    2. Return the updated dictionary.
'''

# Defining the function with 3 parameters (dct, key, value)
def update_dictionary(dct, key, value):

    # Set the conditions to ensure that dct is a dict and nothing else.
        if not isinstance (dct, dict):
                return -1
        
        # Check if key already exists in dct
        if key in dct: 
                print(f'Original value: {dct[key]}')
                
                # Override or add new entry to dct
                dct[key] = value

        return dct

''' Task 2: Invoke the function "update_dictionary" using the following scenarios:
    - {}, "name", "Alice"
    - {"age": 25}, "age", 26
'''
print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))