# asked in interview


class Stack:
    def __init__(self):
        self.items = []
        self.min_items = []

    def push(self, item):
        self.items.append(item)

        if self.min_items:
            if self.min_items[-1] > item:
                self.min_items.append(item)
            else:
                self.min_items.append(self.min_items[-1])
        else:
             self.min_items.append(item)
    
    def pop(self):   
        if self.items and self.min_items:
            self.min_items.pop()
            return self.items.pop()
        else:
            print('List is empty')
            return None
        
    def get_min(self):
        return self.min_items[-1]
    

    
d1 = Stack()

d1.push(10)
print(d1.get_min())
d1.push(5)
print(d1.get_min())
d1.push(4)
print(d1.get_min())
d1.push(8)
print(d1.get_min())
d1.push(1)
print(d1.get_min())

d1.pop()
print(d1.get_min())
d1.pop()
print(d1.get_min())






