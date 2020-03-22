

class BSTree:
    def __init__(self, adjency, values):
        self.adjency = adjency
        self.value = values

    def children(self, node):
        return self.adjency[node]
    
    def in_order(self, node):
        if node != -1:
            left, right = self.children(node)
            return self.in_order(left) + [self.value[node]] + self.in_order(right)
        else:
            return []

    def check_tree(self):
        if self.adjency:
            path = self.in_order(0)
        else:
            path = []
        print(path)
        for i in range(len(path) - 1):
            if path[i] >= path[i + 1]:
                return False
        return True


def main():
    n = int(input())
    adjency, values = [None] * n, [None] * n

    for i in range(n):
        value, left, right = map(int, input().split())
        values[i], adjency[i] = value, [left, right]
    tree = BSTree(adjency, values)

    print("CORRECT" if tree.check_tree() else "INCORRECT")
    

if __name__ == "__main__":
    main()