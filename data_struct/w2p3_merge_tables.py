import sys

from containers.disjoint import UnionFind


def main():
    n, m = map(int, input().split())
    table_sizes = [int(t) for t in input().split()]

    db_union = UnionFind(n, table_sizes)

    reader = (map(int, tup.split()) for tup in sys.stdin)
    for dest, source in reader:
        print(f"UNION({dest}, {source})")
        db_union.Union(dest - 1, source - 1)
        print(db_union.max)


if __name__ == "__main__":
    main()