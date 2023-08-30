# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.

input_tuple = ('Hello', 'World', 'from', 'Python')

def concatenateStrings(tuple):
    return ' '.join(tuple)

output_string = concatenateStrings(input_tuple)
print(output_string)  # Expected output: 'Hello World from Python'