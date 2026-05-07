''' Task 1: Create a function that finds the first negative number in a list (lst).
    Conditions: 
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
'''

# Defining the function with one parameter (lst)
def find_first_negative(lst):

    # Set the conditions to ensure that lst is a list and nothing else.
        if not isinstance (lst, list):
                return -1
        # initialise the index counter at 0 which the while loop will use to iterate through the list
        i = 0
        
        # use while loop to continue iterating throught lst
        while i < len(lst):

            # Check item at the current index and if it's less than 0 (i.e., a negative number), return that number immediately
            if lst [i] < 0:
                return lst[i]
                
            # Move to the next index if current index is not a negataive number
            i += 1
        return "No negatives"

'''Task 2: Invoke the function "find_first_negative" using the following scenario:
    - [3, 5, -1, 7, -2, 8]
    - [2, 10, 7, 0]
'''
print(find_first_negative([3, 5, -1, 7, -2, 8]))  
print(find_first_negative([2, 10, 7, 0]))

