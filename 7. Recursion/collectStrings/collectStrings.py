# Write a function called collectStrings which accepts an object and returns an array of all the values in the object that have a typeof string.

obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

def collectStrings(obj):
    result = []
    for key in obj:
        if type(obj[key]) is str:
            result.append(obj[key])
        elif type(obj[key]) is dict:
            result += collectStrings(obj[key])
    return result

 
print(collectStrings(obj)) # ['foo', 'bar', 'baz']