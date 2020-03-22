# https://medium.com/@dimko1/%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B-%D0%BE%D0%B1%D1%85%D0%BE%D0%B4-%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%B0-ed54848c2d47

class Tree:
    def __init__(self, adjency, values):
        self.adjency = adjency
        self.value = values

    def children(self, node):
        return self.adjency[node]

    def traverse(self, node, kind):
        walker = getattr(Tree, kind)
        walker(self, node)
        print()

    def pre_order(self, node):
        if node != -1:
            left, right = self.children(node)

            print(self.value[node], end=" ")
            self.pre_order(left)
            self.pre_order(right)

    def in_order(self, node):
        if node != -1:
            left, right = self.children(node)

            self.in_order(left)
            print(self.value[node], end=" ")
            self.in_order(right)

    def post_order(self, node):
        if node != -1:
            left, right = self.children(node)

            self.post_order(left)
            self.post_order(right)
            print(self.value[node], end=" ")


def main():
    n = int(input())
    adjency, values = [None] * n, [None] * n

    for i in range(n):
        value, left, right = map(int, input().split())
        values[i], adjency[i] = value, [left, right]

    tree = Tree(adjency, values)
    
    for kind in ("in_order", "pre_order", "post_order"):
        tree.traverse(0, kind)


if __name__ == "__main__":
    main()