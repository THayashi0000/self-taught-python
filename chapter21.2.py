class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]
    def size(self):
        return len(self.items)


stack = Stack()
list = [1, 2, 3, 4, 5]
reverse = []
for i in range(len(list)):
    stack.push(list[i])
for j in range(len(list)):
    reverse.append(stack.pop())
print(reverse)
