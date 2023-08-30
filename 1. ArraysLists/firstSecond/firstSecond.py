# Given a list, write a function to get first, second best scores from the list.

# List may contain duplicates.

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

def firstSecond(list):
    list.sort(reverse=True)
    return list[0], list[1]

print(firstSecond(myList)) # 90 87