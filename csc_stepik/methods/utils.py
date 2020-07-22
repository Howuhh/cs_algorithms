

def to_int(lst: list) -> list:
    return list(map(int, lst))


class PQueue:
    # очередь с приоритетом
    def __init__(self, lst):
        self.n = len(lst)
        self.queue = lst  # O(n)

    def insert(self, item):  # O(n)
        self.queue.insert(0, item)

    def extract_min(self, key=None):  # O(n)
        if not key:
            key = lambda x: x
        
        index, min_ = -1, +inf
        for i, el in enumerate(self.queue):
            if key(el) <= min_:
                index, min_ = i, key(el)

        return self.queue.pop(index)