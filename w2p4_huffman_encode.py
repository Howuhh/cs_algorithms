import heapq
from collections import Counter, deque

from w2p5_huffman_decode import Node, Leaf



def encode_huffman(string: str) -> dict:
    heap = [(freq, i, Leaf(char)) for i, (char, freq) in enumerate(Counter(string).items())]  # O(n)
    heapq.heapify(heap)

    while len(heap) > 1:  # O(n)
        freq1, i1, left = heapq.heappop(heap)  # O(logn)
        freq2, i2, right = heapq.heappop(heap)  # O(logn)

        heapq.heappush(heap, (freq1 + freq2, i1 + i2, Node(left, right))) 
    
    codes = {}
    root = heapq.heappop(heap)[2] 
    root.code(codes) # O(n)

    return codes, root  # O(n)* O(logn) = O(nlogn)


def decode_huffman(root, string):
    decoded_string = ""
    encoded = deque(string)

    while encoded: # O(n)
        if root.char:
            decoded_string += root.decode(encoded)
            encoded.popleft()
        else:
            decoded_string += root.decode(encoded)

    return decoded_string


def main(string=None):
    if not string:
        string = input()

    codes, root = encode_huffman(string)
    encoded_string = "".join([codes[letter] for letter in string])

    print(len(codes), len(encoded_string))

    for code in codes:
        print(f"{code}: {codes[code]}")

    print(encoded_string)


def test():
    string = "wronganswer"
    print(string)
    codes, root = encode_huffman(string)
    encoded_string = "".join([codes[letter] for letter in string])
    print(encoded_string)

    new_string = decode_huffman(root, encoded_string)
    print(new_string)


if __name__ == "__main__":
    main()
    # test()




































# if __name__ == "__main__":
#     code = input()

#     letter_freq = Counter(code)
    
#     freq = list(letter_freq.values())
#     letters = dict(zip(letter_freq.keys(), range(len(freq))))
#     encoding_tree = build_huffman_tree(freq)

#     encoded_str = "".join([encoding_tree[letters[letter]] for letter in code])

#     print(f"{len(letter_freq)} {len(encoded_str)}")

#     for letter in letters:
#         print(f"{letter}: {encoding_tree[letters[letter]]}")

#     print(encoded_str)



# def traverse_tree(dict_tree, n, root, path=None, labels=None):
#     # tree example: {4: (3, 2), 5: (1, 4), 6: (0, 5)}
#     if labels is None:
#         labels = {}
    
#     if path is None:
#         path = ""
    
#     if root <= n:
#         labels[root] = path
#         return None
    
#     left, right = dict_tree[root][0], dict_tree[root][1]
    
#     traverse_tree(dict_tree, n, left, path=path+"0", labels=labels)
#     traverse_tree(dict_tree, n, right, path=path+"1", labels=labels)
    
#     return labels
 

# def build_huffman_tree(freq):
#     """Кодирование Хаффмана"""
#     if len(freq) == 1:
#         return {0: "0"}

#     tree_index = {}
#     zip_freq = list(zip(range(len(freq)), freq))

#     queue = PQueue(zip_freq)
#     for k in range(queue.n, 2*queue.n - 1):
#         min1 = queue.extract_min(key=lambda tup: tup[1])
#         min2 = queue.extract_min(key=lambda tup: tup[1]) 

#         # freq.append(min1[1] + min2[1])

#         tree_index[k] = (min1[0], min2[0])  # node: (left, right)

#         queue.insert((k, freq[-1]))

#     return traverse_tree(tree_index, queue.n - 1, queue.n*2 - 2) 

