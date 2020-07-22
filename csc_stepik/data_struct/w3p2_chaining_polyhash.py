import sys

from containers.map import ChainHashMap


class StreamHandler:
    def __init__(self, hash_map: ChainHashMap):
        self.map = hash_map

    def handle(self, command):
        commands_map = {"del": "_del"}
        name, key = command.split()

        handler = getattr(StreamHandler, commands_map.get(name, name))
        handler(self, key)

    def add(self, key):
        self.map[key] = key

    def _del(self, key):
        del self.map[key]

    def find(self, key):
        print("yes" if self.map[key] else "no")

    def check(self, i):
        values = self.map.table[int(i)]
        if values:
            print(" ".join(s for s in values))


def main():
    m, n = int(next(sys.stdin)), next(sys.stdin)
    handler = StreamHandler(ChainHashMap(size=m))

    for command in sys.stdin:
        handler.handle(command)
        
if __name__ == "__main__":
    main()