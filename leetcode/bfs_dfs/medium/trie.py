class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["*"] = "*"

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node:
                node = node[char]
            else:
                return False
        
        if "*" in node:
            return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char in node:
                node = node[char]
            else:
                return False
        return True