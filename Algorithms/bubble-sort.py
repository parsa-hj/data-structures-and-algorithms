#Bubble sort algorithm implementation in python

#Bubble sort works by repeatedly swapping the adjacent elements if they are in the wrong order.

#This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

#Time complexity: O(N^2)  Quadratic time

def bubble_sort(list):
    #Keeps track of the rightmost index that hasn't been sorted
    unsorted_until_index = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True    #We'll assume the array is sorted until we encounter a swap
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:    #Compare each pare of adjacent values
                list[i], list[i+1] = list[i+1], list[i]    #Swap them if they are out of order
                sorted = False    #Change to false if we made a swap
        unsorted_until_index -= 1    #Decrement because the value that is all the way to the right is sorted

    return list


#Test array
test_array = [65,55,45,35,25,10]

#Function call
print(bubble_sort(test_array))