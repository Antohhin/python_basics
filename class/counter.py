class Counter:
    def __init__(self):
        self.counter = 0
    def inc(self):
        self.counter+=1
    
x = Counter()
print(x.counter)
x.inc
print(x.counter)
# print(Counter.counter)