# Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def mergeDicts(dict1, dict2):
    merged = dict1.copy()
    for item in dict2:
        if item in merged:
            merged[item] += dict2.get(item)
        else:
            merged[item] = dict2.get(item)
    return merged


print(mergeDicts(dict1, dict2))