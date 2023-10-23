"My example"
from icecream import ic

class AddNums:
    def __init__(self, val=0):
        self.val = val
    def add(self, val):
        self.val += val
    def print_val(self):
        print(self.val)
    
a = AddNums()
ic(type(a))
b = AddNums(2)
c = AddNums(4)
a.add(2)
b.add(3)

a.print_val()
b.print_val()
c.print_val()