def middle(lst):
    # Return a new list containing all elements from the original list, excluding the first and last elements
    return lst[1:-1]
 
my_list = [1, 2, 3, 4]
 
print(middle(my_list))  # Output: [2, 3]



# def middle(lst):
# This line defines a function called middle that takes a single argument, a list named lst.

# return lst[1:-1]
# This line returns a new list that is a slice of the original list lst. The slice starts at index 1 (the second element) and goes up to (but does not include) the last element. This effectively removes the first and last elements from the list.