# Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 

def filterDict(dict, condition):
    return {k:v for k,v in dict.items() if condition(k,v)}

filtered_dict = filterDict(my_dict, lambda k, v: v % 2 == 0) 
print(filtered_dict)