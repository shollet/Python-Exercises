def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result

# Create a copy of dict1 named result. This ensures that the original dict1 is not modified during the process. The copy() method takes O(n) time complexity, where n is the number of elements in dict1. The space complexity is also O(n) as a new dictionary is created with the same number of elements as dict1.

# Iterate through the key-value pairs of dict2 using a for loop. This loop runs for m iterations, where m is the number of elements in dict2. For each key-value pair:

# a. Use the get() method to retrieve the current value associated with the key in the result dictionary. If the key is not present in result, get() returns the default value (0).

# b. Add the value from dict2 to the current value (or 0, if the key is not in result) and update the result dictionary with the new value for the key. The get() and update operations take O(1) average time complexity.

# Return the merged dictionary result.