def _children(node):
    left, right = 2*node + 1, 2*node + 2
    return left, right


def _parent(node):
    parent = (node - 1) // 2
    return parent


class Heap:
    def __init__(self, init_arr=None):
        if init_arr:
            self._heap = init_arr.copy()
            self._heapify(self._heap)
        else:
            self._heap = []
    
    @property
    def _last_idx(self):
        return len(self._heap) - 1
    
    @property
    def _top(self):
        try:
            top = self._heap[0]
        except IndexError:
            raise("Heap is empty")
        return top

    def _swap(self, node1, node2):
        self._heap[node1], self._heap[node2] = self._heap[node2], self._heap[node1]

    def _shift_up(self, node):
        parent = _parent(node)

        if parent > -1 and self._heap[parent] > self._heap[node]:
            self._swap(node, parent)
            self._shift_up(parent)

    def _shift_down(self, node):
        left, right = _children(node)
        size = len(self._heap)

        swap_node = node
        if left < size and self._heap[left] < self._heap[swap_node]:
            swap_node = left
        if right < size and self._heap[right] < self._heap[swap_node]:
            swap_node = right
        
        if swap_node != node:
            self._swap(node, swap_node)
            self._shift_down(swap_node)

    def _heapify(self, arr):
        "build heap inplace"
        for node in range(len(arr) // 2, -1, -1):
            self._shift_down(node)

    def heappush(self, key):
        self._heap.append(key)
        self._shift_up(self._last_idx)

    def heappop(self):
        self._swap(0, self._last_idx)
        
        value = self._heap.pop()
        self._shift_down(0)
        
        return value

    def top(self):
        return self._top

    def __len__(self):
        return len(self._heap)

    def __str__(self):
        return self._heap.__str__()

    
def heap_test():
    test = [6, 5, 4, 3, 2, 1]

    test_heap = Heap(test)
    heapq.heapify(test)

    assert test == test_heap._heap

    heapq.heappush(test, 1)
    test_heap.heappush(1)
    assert test == test_heap._heap
    print(test, test_heap._heap)
    assert heapq.heappop(test) == test_heap.heappop()
    assert heapq.heappop(test) == test_heap.heappop()
    assert heapq.heappop(test) == test_heap.heappop()
    print(test, test_heap._heap)


if __name__ == "__main__":
    heap_test()