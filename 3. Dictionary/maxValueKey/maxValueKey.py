# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

my_dict = {'a': 5, 'b': 9, 'c': 2}

def maxValueKey(dict):
    return max(dict, key=dict.get)

print(maxValueKey(my_dict))