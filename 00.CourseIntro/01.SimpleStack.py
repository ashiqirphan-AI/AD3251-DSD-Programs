class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0

# Create a stack object
stack = Stack()

# Perform stack operations
stack.push(10)
stack.push(20)
stack.push(30)
#stack.push(40)

print(stack.pop())  # Output: 30
print(stack.pop())  # Output: 20
print(stack.is_empty())  # Output: False

stack.push(40)
print(stack.pop())  # Output: 40

print(stack.is_empty())  # Output: True
