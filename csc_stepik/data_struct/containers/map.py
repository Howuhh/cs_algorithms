from collections import deque


class DirectAccessMap:
    def __init__(self, size):
        # simple direct access table
        self.table = [None] * size
        self.size = size

    def _index(self, key):
        return key % self.size

    def update(self, key, value):
        self.table[self._index(key)] = value

    def get(self, key, *args):
        return self.table[self._index(key)]

    def remove(self, key, *args):
        self.table[self._index(key)] = None


def poly_hash(S, p=1000000007, a=263):
    hash_value = 0
    for i in range(len(S)):
        hash_value += ((ord(S[i]) % p) * (a**i % p))

    return hash_value % p


class ChainHashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _index(self, key): 
        return poly_hash(key) % self.size

    def __setitem__(self, key, value):
        index = self._index(key)

        if self.table[index]:
            if value not in self.table[index]:
                self.table[index].appendleft(value)
        else:
            self.table[index] = deque([value])

    def __getitem__(self, key):
        index = self._index(key)

        if self.table[index]:
            for value in self.table[index]:
                if value == key:
                    return value

    def __delitem__(self, key):
        index = self._index(key)

        if self.table[index]:
            for idx, value in enumerate(self.table[index]):
                if value == key:
                    del self.table[index][idx]
                    break

    def __str__(self):
        return " ".join(s.__str__() for s in self.table if s)


def test():
    test_map = ChainHashMap(256)

    test_map["string"] = "string"
    print(test_map["string"])
    del test_map["string"]

    print(test_map)


if __name__ == "__main__":
    test()