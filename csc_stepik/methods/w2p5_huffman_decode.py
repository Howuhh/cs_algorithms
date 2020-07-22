import heapq
from collections import deque


class Node:
    def __init__(self, left, right, id=None):
        self.left = left
        self.right = right
        self.id = id

        self.char = None

    def code(self, codes: dict, path: str=None):
        if path is None:
            path = ""

        self.left.code(codes, path + "0")
        self.right.code(codes, path + "1")

    def decode(self, encoded: deque):
        code = encoded.popleft()  # O(1)

        if code == "0":
            char = self.left.decode(encoded)
        else:
            char = self.right.decode(encoded)

        return char

    def __str__(self):
        return f"Node ({self.id})"


class Leaf:
    def __init__(self, char):
        self.char = char

    def code(self, codes, path=None):
        codes[self.char] = path or "0"

    def decode(self, encoded: deque):
        return self.char

    def __str__(self):
        return f"Leaf ({self.char})"


def build_tree(codes: list) -> dict:
    heap = [(-len(code), code, Leaf(letter)) for letter, code in codes.items()]
    heapq.heapify(heap)

    node_id = len(heap)
    while len(heap) > 1:
        len1, code1, left = heapq.heappop(heap)
        len2, code2, right = heapq.heappop(heap)
        
        # print(f"MERGE --- (left: {len1}, {code1}, {left}) || (right: {len2}, {code2}, {right}) ---")
        heapq.heappush(heap, (-len(code2[:-1]), code2[:-1], Node(left, right, node_id)))
        node_id -= 1

    root = heapq.heappop(heap)[2]
    return root


def decode_huffman(string, code_map):
    root = build_tree(code_map)

    decoded_string = ""
    encoded = deque(string)

    while encoded:
        if root.char:
            decoded_string += root.decode(encoded)
            encoded.popleft()
        else:
            decoded_string += root.decode(encoded)

    return decoded_string


def main():
    k, _ = map(int, input().split())
    code_map = {}

    for i in range(k):
        letter, code = input().split(":")
        code_map[letter] = code.strip()

    string = input()
    decoded_string = decode_huffman(string, code_map)
    print(decoded_string)


if __name__ == "__main__":
    main()



# def decode_huffman(string, code_map):
#     root = build_tree(code_map)
#     decoded_string = ""

#     if root.char:
#         for char in string:
#             decoded_string += root.char
#         return decoded_string

#     node = root
#     for char in string:
#         node = node.left if char == "0" else node.right

#         if node.char:
#             decoded_string += node.char
#             node = root

#     return decoded_string