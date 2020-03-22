# just for fun, not an optimal solution, O(n^2)!!
import sys
from math import inf


class BSTree:
    def __init__(self, adjency, values):
        self.adjency = adjency
        self.value = values

        self._max = [None] * len(values)
        self._min = [None] * len(values)

    def children(self, node):
        return self.adjency[node]

    def max(self, node):
        if node != -1: 
            if not self._max[node]:
                left, right = self.children(node)
                self._max[node] = max(
                    self.value[node], 
                    self.max(left), 
                    self.max(right)
                )
            return self._max[node]
        return -inf

    def min(self, node):
        if node != -1: 
            if not self._min[node]:
                left, right = self.children(node)
                self._min[node] = min(
                    self.value[node], 
                    self.min(left), 
                    self.min(right)
                )
            return self._min[node]
        return inf

    def _check_node(self, node):
        left, right = self.children(node)
        root_value = self.value[node]

        left_value = -inf if left == -1 else self.value[left]
        right_value = inf if right == -1 else self.value[right]

        left_max, right_min = self.max(left), self.min(right)
    
        if (left_value < root_value <= right_value) and (left_max < root_value <= right_min):
            return True
        return False

    def check_tree(self):        
        for node in range(len(self.value)):
            check = self._check_node(node)
            if not check:
                return False
        return True

def main():
    n = int(input())
    sys.setrecursionlimit(1000 + n)
    adjency, values = [None] * n, [None] * n

    for i in range(n):
        value, left, right = map(int, input().split())
        values[i], adjency[i] = value, [left, right]
    tree = BSTree(adjency, values)

    print("CORRECT" if tree.check_tree() else "INCORRECT")
    

if __name__ == "__main__":
    main()