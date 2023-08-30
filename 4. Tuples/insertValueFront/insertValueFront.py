# Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.

input_tuple = (2, 3, 4)
value_to_insert = 1

def insertValueFront(tuple, value):
    return (value,) + tuple

output_tuple = insertValueFront(input_tuple, value_to_insert)
print(output_tuple)  # Expected output: (1, 2, 3, 4)