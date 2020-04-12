
def read_back(string):
    hash_count, acc = 0, ""
    for char in reversed(string):
        if char == "#":
            hash_count += 1
        elif hash_count:
            hash_count -= 1
        else:
            acc = char + acc
    return acc

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # should be simpler two pointers solution!
        return read_back(S) == read_back(T)