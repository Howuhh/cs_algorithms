from math import inf


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, key):
        self.stack.append(key)

    def pop(self):
        if self.empty():
            return None
        return self.stack.pop()

    def top(self):
        if self.empty():
            return None
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return " ".join(f"{el}" for el in self.stack)


class MaxStack(Stack):
    def __init__(self):
        super().__init__()

        self.max_stack = []

    def push(self, key):
        self.stack.append(key)

        curr_max = -inf if not self.max_stack else self.max_stack[-1]
        self.max_stack.append(max(curr_max, key))

    def pop(self):
        if self.empty():
            return None
        self.max_stack.pop()

        return self.stack.pop()

    def max(self):
        return self.max_stack[-1]


# much simpler implementation
class MinMaxStack:
    def __init__(self):
        self.stack = []

    def push(self, key):
        if not self.stack:
            self.stack.append((key, key, key))
        else:
            self.stack.append((
                key, 
                max(key, self.stack[-1][1]), 
                min(key, self.stack[-1][2])
            ))

    def pop(self):
        if self.stack:
            return self.stack.pop()[0]
        return None

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        return None
    
    def max(self):
        if self.stack:
            return self.stack[-1][1]
        return -inf

    def min(self):
        if self.stack:
            return self.stack[-1][2]
        return inf

    def len(self):
        return len(self.stack)

    def empty(self):
        return not bool(self.stack)