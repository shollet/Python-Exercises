# Write a recursive function called reverse which accepts a string and returns a new string in reverse.

def reverse(strng):
    if len(strng) in [0,1]:
        return strng
    return strng[-1] + reverse(strng[:-1])

print(reverse('python')) # 'nohtyp'
print(reverse('appmillers')) # 'srellimppa'