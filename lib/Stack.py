class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return False if self.items else True

    def push(self, item):
        if not self.full():
            self.items.append(item)
        # raise NameError("Stack is already full!")

    def pop(self):
        if self.items:
            return self.items.pop(-1)
        return None
        # raise Error("Stack is already empty!")

    def peek(self):
        if self.items:
            return self.items[-1]
        else: 
            raise Error("Stack is empty!")
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.size() == self.limit

    def search(self, target):
        if target not in self.items:
            return -1
        for i in range(self.size()):
            if self.items[-(i+1)] == target:
                return i