# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

def getDiagonal(tup):
    result = []
    for i in range(len(tup)):
        result.append(tup[i][i])
    return tuple(result)

output_tuple = getDiagonal(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9)