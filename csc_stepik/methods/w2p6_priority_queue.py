import math
import sys


# http://neerc.ifmo.ru/wiki/index.php?title=%D0%94%D0%B2%D0%BE%D0%B8%D1%87%D0%BD%D0%B0%D1%8F_%D0%BA%D1%83%D1%87%D0%B0
# https://habr.com/ru/post/112222/
class MaxHeap:
    def __init__(self):
        self.heap = []
    
    @property
    def last_idx(self):
        return len(self.heap) - 1

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _parent(self, i: int) -> int:
        assert i >= 0
        return math.floor((i - 1) / 2)

    def _children(self, i: int) -> tuple:
        left, right = (2*i + 1, 2*i + 2)

        if left == self.last_idx:
            return (left, left)
        elif left > self.last_idx:
            return None

        return left, right

    def _shift_up(self, i):
        parent = self._parent(i)

        if (self.heap[i] > self.heap[parent]) and parent != -1:
            self._swap(i, parent)
            self._shift_up(parent)

    def _shift_down(self, i):
        if self._children(i):
            left, right = self._children(i)

            child = max(((self.heap[left], left), (self.heap[right], right)))
            if (self.heap[i] < child[0]):
                self._swap(i, child[1])
                self._shift_down(child[1])

    def push(self, item):
        self.heap.append(item)
        self._shift_up(self.last_idx)

    def pop(self):
        self._swap(0, self.last_idx)

        item = self.heap.pop()
        self._shift_down(0)

        return item

    def print(self, heap=None, i=0, d=0):
        if heap is None:
            heap = self.heap

        if i >= len(self.heap):
            return
        
        l, r = (2*i + 1, 2*i + 2)
        self.print(heap, r, d=d+1)
        print("   "*d + str(heap[i]))
        self.print(heap, l, d=d+1)


def main():
    heap = MaxHeap()

    instr = (op for op in sys.stdin)
    n = next(instr)

    for op in instr:
        if op.startswith("ExtractMax"):
            hmax = heap.pop()
            print(hmax)
        else:
            new = int(op.split()[1])
            print(f"INSERT {new}")
            heap.push(new)
        heap.print()
        print("-"*20)


def test():
    heap = MaxHeap()
    # heap.heap = [29, 19, 20, 5, 12, 10, 12, 3, 1, 9, 8, 6]
    # heap.heap = [200, 5, 10]

    # assert heap._parent(0) == -1
    # assert heap._parent(1) == 0
    # assert heap._parent(5) == 2
    # assert heap._parent(10) == 4

    # assert heap._children(0) == (1, 2)
    # assert heap._children(4) == (9, 10)
    # assert heap._children(3) == (7, 8)

    # heap.push(200)
    # heap.print()
    # print("-"*30)

    # heap.push(5)
    # heap.print()
    # print("-"*30)

    # heap.push(10)
    # heap.print()
    # print("-"*30)
   
    # heap.push(500)
    # heap.print()
    # print("-"*30)


    # heap.print()
    # print("-"*20)

    # heap.push(30)

    # heap.print()
    # print("-"*20)

    # hmax = heap.pop()
    # print("Max", hmax)
    # heap.print()
    # print("-"*20)


    # hmax = heap.pop()
    # print("Max", hmax)
    # heap.print()
    # print("-"*20)

    # hmax = heap.pop()
    # print("Max", hmax)
    # heap.print()


if __name__ == "__main__":
    main()
    # test()
