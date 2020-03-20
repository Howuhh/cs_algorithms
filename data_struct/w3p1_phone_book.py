import sys

from containers.map import DirectAccessMap


class MapHandler:
    def __init__(self, map):
        self.map = map

    def process(self, query):
        query_map = {
            "add": "update",
            "del": "remove",
            "find": "get",
        }
        command = query[0]
        key, *value = query[1:]
        getattr(MapHandler, query_map[command])(self, int(key), *value)

    def update(self, key, value):
        self.map.update(key, value)

    def remove(self, key, *args):
        self.map.remove(key)

    def get(self, key, *args):
        value = self.map.get(key)
        print(value if value else "not found")


def main():
    n = int(input())
    size = 10**7
    handler = MapHandler(DirectAccessMap(size))
    
    [handler.process(tup.split()) for tup in sys.stdin]


if __name__ == "__main__":
    main()