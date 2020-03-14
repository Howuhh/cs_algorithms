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
    

class QueueWithStack:
    def __init__(self):
        self.push_stack = MinMaxStack()
        self.pop_stack = MinMaxStack()

    def pushBack(self, key):
        self.push_stack.push(key)        

    def popFront(self):
        if self.pop_stack.empty():
            while not self.push_stack.empty():
                self.pop_stack.push(self.push_stack.pop())

        return self.pop_stack.pop()

    def min(self):
        return min(self.push_stack.min(), self.pop_stack.min())

    def max(self):
        return max(self.push_stack.max(), self.pop_stack.max())

    def len(self):
        return self.push_stack.len() + self.pop_stack.len()

    def empty(self):
        return not (bool(self.push_stack) or bool(self.pop_stack))


class QueueWithArray:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * self.size
        self._len = 0

        self.front, self.back = -1, -1

    def pushBack(self, key):
        if (self.back + 1) % self.size == self.front:
            raise IndexError("queue is full")

        # empty queue
        if self.front == -1:
            self.front = 0
            self.back = 0
        else:
            self.back = (self.back + 1) % self.size
        
        self._len = self._len + 1
        self.queue[self.back] = key
            
    def popFront(self):
        if self.front == -1:
            raise IndexError("queue is empty")
        
        # one element -> to the empty queue 
        if self.back == self.front:
            value = self.queue[self.front]
            self.queue[self.front] = None

            self.back = -1
            self.front = -1
            self._len = 0
        else:
            value = self.queue[self.front]
            self.queue[self.front] = None

            self._len = self._len - 1
            self.front = (self.front + 1) % self.size

        return value

    def getBack(self):
        return self.queue[self.back]

    def getFront(self):
        return self.queue[self.front]

    def len(self):
        return self._len

    def empty(self):
        return self._len == 0

    def __str__(self):
        return  "||" + "-".join(str(el) for el in self.queue) + "||"


if __name__ == "__main__":
    testq = QueueWithArray(size=4)

    print(testq, testq.len())
    testq.pushBack(1)
    print(testq, testq.len())

    testq.pushBack(2)
    print(testq, testq.len())

    testq.pushBack(3)
    print(testq, testq.len())

    testq.pushBack(4)
    print(testq, testq.len())

    testq.popFront()
    print(testq, testq.len())

    testq.pushBack(5)
    print(testq, testq.len())