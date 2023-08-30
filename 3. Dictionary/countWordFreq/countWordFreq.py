# Define a function to count the frequency of words in a given list of words. 

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 

def countWordFrequency(array):
    dict = {}
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict

print(countWordFrequency(words)) 