def reverse_dict(my_dict):
    return {v: k for k, v in my_dict.items()}

# Use dictionary comprehension to create a new dictionary by iterating through the key-value pairs in the input dictionary my_dict using the items() method. The items() method returns an iterable that produces key-value pairs as tuples.

# For each key-value pair (k, v) from the input dictionary, the dictionary comprehension creates a new entry in the reversed dictionary with the value v as the key and the key k as the value. The syntax is {v: k for k, v in my_dict.items()}.

# The time complexity of this operation is O(n), where n is the number of elements in the dictionary my_dict The dictionary comprehension iterates through all the key-value pairs in the input dictionary once.

# Return the new dictionary with the reversed key-value pairs.