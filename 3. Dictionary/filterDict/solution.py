def filter_dict(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(k, v)}

# Use dictionary comprehension to create a new dictionary by iterating through the key-value pairs in the input dictionary my_dict using the items() method. The items() method returns an iterable that produces key-value pairs as tuples.

# For each key-value pair (k, v) from the input dictionary, the dictionary comprehension checks if the condition is met by calling the condition(k, v) function. The condition function takes a key and a value as arguments and returns a boolean value.

# If the condition is met, the dictionary comprehension creates a new entry in the filtered dictionary with the same key-value pair. The syntax is {k: v for k, v in my_dict.items() if condition(k, v)}.

# The time complexity of this operation is O(n), where n is the number of elements in the dictionary my_dict. The dictionary comprehension iterates through all the key-value pairs in the input dictionary once.

# Return the new dictionary containing the filtered key-value pairs.