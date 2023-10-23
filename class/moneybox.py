from icecream import ic

class MoneyBox:
    def __init__(self, capacity, value = 0):
        self.capacity = capacity
        self.current = value
        # self
    def add(self, val):
        self.current += val
    def can_add(self, val):
        return self.capacity >= self.current + val
        # print(self.capacity -= val)

a = MoneyBox(8)
ic(a.capacity, a.current)
# a.capacity()
ic(a.can_add(9))
# a.add(9)
# ic(a.capacity)
ic(a.can_add(5))
a.add(5)
ic(a.current)
ic(a.can_add(1))
a.add(1)
ic(a.capacity, a.current)
b = MoneyBox(6)
# a.capacity
ic(b.capacity, b.current)
ic(b.can_add(7))
ic(b.can_add(6))
b.add(6)
ic(b.capacity, b.current)