# Write a function called stringifyNumbers which takes in an object and finds all of the values which are numbers and converts them to strings. Recursion would be a great way to solve this!

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

def stringifyNumbers(obj):
    newObj = obj
    for key in newObj:
        if type(newObj[key]) is int:
            newObj[key] = str(newObj[key])
        elif type(newObj[key]) is dict:
            newObj[key] = stringifyNumbers(newObj[key])
    return newObj

 
print(stringifyNumbers(obj))
 
{'num': '1', 
 'test': [], 
 'data': {'val': '4', 
          'info': {'isRight': True, 'random': '66'}
          }
}