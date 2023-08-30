def remove_duplicates(lst):
    unique_lst = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst
 
my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]

# Create an empty list unique_lst to store the unique elements, and an empty set seen to keep track of the elements already processed.

# Iterate through the input list lst using a for loop.

# For each item in lst, check if it is not in seen. If it's not in seen, append it to unique_lst and add it to the seen set.

# Return the unique_lst containing the unique elements from the input list lst.