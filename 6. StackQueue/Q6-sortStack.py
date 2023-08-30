# Sort a stack with the smallest on top using only a single temporary stack.

def sort_stack(stack):
    # TODO

class Stack():
  def __init__(self):
    self.top = None
  
  def __str__(self):
    return str(self.top)
  
  def push(self, item):
    self.top = current(item, self.top)
  
  def pop(self):
    if not self.top:
      return None
    item = self.top
    self.top = self.top.next
    return item.data

class current():
  def __init__(self, data=None, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    return str(self and self.data) + ',' + str(self and self.next)