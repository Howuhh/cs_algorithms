from .stack import MinMaxStack


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

        self._front, self._back = -1, -1

    def pushBack(self, key):
        if (self._back + 1) % self.size == self._front:
            raise IndexError("queue is full")

        # empty queue
        if self._front == -1:
            self._front = 0
            self._back = 0
        else:
            self._back = (self._back + 1) % self.size
        
        self._len = self._len + 1
        self.queue[self._back] = key
            
    def popFront(self):
        if self._front == -1:
            raise IndexError("queue is empty")
        
        # one element -> to the empty queue 
        if self._back == self._front:
            value = self.queue[self._front]
            self.queue[self._front] = None

            self._back = -1
            self._front = -1
            self._len = 0
        else:
            value = self.queue[self._front]
            self.queue[self._front] = None

            self._len = self._len - 1
            self._front = (self._front + 1) % self.size

        return value

    def back(self):
        return self.queue[self._back]

    def front(self):
        return self.queue[self._front]

    def len(self):
        return self._len

    def empty(self):
        return self._len == 0

    def __str__(self):
        return "||" + "-".join(str(el) for el in self.queue) + "||"


def queue_test():
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


if __name__ == "__main__":
    queue_test()