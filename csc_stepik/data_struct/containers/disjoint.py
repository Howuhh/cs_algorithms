

class UnionFind:
    def __init__(self, N, size=None):
        self.parent = [i for i in range(N)]
        self.size = size if size else [1] * N
        self.max = max(self.size)

    def Union(self, a, b):
        parent_a = self.Find(a)
        parent_b = self.Find(b)

        if parent_a != parent_b:
            # just always union by left
            self.parent[parent_b] = parent_a
            
            # update talbe sizes
            self.size[parent_a] += self.size[parent_b]
            self.size[parent_b] = 0

            # update max value
            self.max = max(self.max, self.size[parent_a])

    def Find(self, a):
        # path compression -> flattens the tree
        # more on https://en.wikipedia.org/wiki/Disjoint-set_data_structure
        if a != self.parent[a]:
            self.parent[a] = self.Find(self.parent[a])

        return self.parent[a]


def test():
    N = 8

    union = UnionFind(N)
    union.Union(0, 1)
    
    union.Union(3, 4)
    union.Union(4, 7)

    union.Union(0, 3)

    assert union.Find(4) == union.Find(1)
    assert union.Find(6) != union.Find(5)
    assert union.max == 5

    print(union.parent)
    # print(union.size)


if __name__ == "__main__":
    test()