import sys

from containers.disjoint import UnionFind


def main():
    n, e, d = map(int, input().split())
    system = UnionFind(n)

    reader = (map(int, tup.split()) for tup in sys.stdin)

    is_true_system = True
    for idx, (x1, x2) in enumerate(reader):
        if idx >= e:
            if system.Find(x1 - 1) == system.Find(x2 - 1):
                is_true_system = False
        else:
            system.Union(x1 - 1, x2 - 1)
            
    print(int(is_true_system))


if __name__ == "__main__":
    main()