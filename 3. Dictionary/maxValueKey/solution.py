def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)

# Call the built-in max() function with the dictionary my_dict as its first argument and key=my_dict.get as its second argument.

# The max() function iterates through the keys in the dictionary and compares the values associated with each key using the get() method. The key parameter specifies a custom function to extract a comparison key from each dictionary key. In this case, the get() method returns the value associated with each key, so the max() function compares the values of the dictionary.

# The time complexity of the max() function is O(n), where n is the number of elements in the dictionary my_dict. The max() function iterates through all the keys in the dictionary once, and the get() method has an average time complexity of O(1).

# Return the key with the highest value found by the max() function.