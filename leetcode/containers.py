from math import inf

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, key):
        if not self.stack:
            self.stack.append((key, key))
        else:
            self.stack.append((key, min(key, self.stack[-1][1])))

    def pop(self):
        return None if not self.stack else self.stack.pop()[0]

    def min(self):
        return inf if not self.stack else self.stack[-1][1]

    def __bool__(self):
        return bool(self.stack)


class MinQueue:
    def __init__(self):
        self._push_stack = MinStack()
        self._pop_stack = MinStack()

    def pushBack(self, key):
        self._push_stack.push(key)

    def popFront(self):
        if not self._pop_stack:
            while self._push_stack:
                self._pop_stack.push(self._push_stack.pop())
        
        return self._pop_stack.pop()

    def min(self):
        return min(self._pop_stack.min(), self._push_stack.min())

    def __len__(self):
        return len(self._push_stack.stack) + len(self._pop_stack.stack)