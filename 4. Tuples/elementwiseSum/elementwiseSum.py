# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

def tupleElementwiseSum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))

output_tuple = tupleElementwiseSum(tuple1, tuple2)
print(output_tuple)  # Expected output: (5, 7, 9)