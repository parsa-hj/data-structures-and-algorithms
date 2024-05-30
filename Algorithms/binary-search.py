#Binary search algorithm implementation in python

#In this approach, the element is always searched in the middle of a portion of an array.

#Binary search only works with ordered arrays

#Time complexity: O(log n)  Increases one step each time data is doubled

def binary_search(array,search_value):
    #lower_bound is the first value in the array, while upper_bound is the last value
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        #Find the midpoint between the upper and lower bounds
        midpoint = (lower_bound + upper_bound) // 2

        value_at_midpoint = array[midpoint]

        #If the value of the midpoint is the one we are looking for, return it's index
        if search_value == value_at_midpoint:
            return midpoint
        #If not change the lower and upper bounds based on whether we need to guess higher or lower
        elif search_value < value_at_midpoint:
            upper_bound = midpoint - 1
        elif search_value > value_at_midpoint:
            lower_bound = midpoint + 1

    #If we reach here, then the element was not present
    return -1
    

#Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
#Function call
result = binary_search(arr, x)