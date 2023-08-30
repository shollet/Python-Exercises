# Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.

my_dict = {'a': 1, 'b': 2, 'c': 3}

def reverseDict(dict):
    result = {}
    for key,value in dict.items():
        result[value] = key
    return result

print(reverseDict(my_dict))