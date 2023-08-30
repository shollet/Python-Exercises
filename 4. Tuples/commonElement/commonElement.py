# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

def commonElements(tuple1, tuple2):
    return tuple(i for i in tuple1 if i in tuple2)


output_tuple = commonElements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)