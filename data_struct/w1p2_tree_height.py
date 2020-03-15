import sys

from containers import QueueWithArray


def children(node, adjency):
    children_ = adjency[node] if adjency[node] else []
    return children_

# deque instead my implementation also good
def tree_height_queue(root, adjency):
    queue = QueueWithArray(size=len(adjency))
    queue.pushBack(root)

    height = 0
    while not queue.empty():  # O(n)
        height = height + 1

        nodes = queue.len()
        while nodes > 0:  # O(2^height) - ?
            parent = queue.popFront()

            for child in children(parent, adjency):  # O(1)
                queue.pushBack(child)
            nodes = nodes - 1

    return height

# not optimal
def tree_height(root, adjency):

    def _tree_height(node):
        height = 1

        for child in children(node, adjency):
            if child:
                height = max(height, 1 + _tree_height(child))

        return height

    return _tree_height(root)


def process_tree(arr_tree):
    root = None
    adjency = [[] for _ in range(len(arr_tree))]  # O(n)
    
    for node in range(len(arr_tree)):  # O(n)
        parent = arr_tree[node]
        if parent == -1:
            root = node
        else:
            adjency[parent].append(node)
    return root, adjency


def main():
    n = int(sys.stdin.readline())
    raw_tree = [int(el) for el in sys.stdin.readline().split()]

    root, adjency = process_tree(raw_tree)
    print(tree_height(root, adjency))
    print(tree_height_queue(root, adjency))

if __name__ == "__main__":
    main()