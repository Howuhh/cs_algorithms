import sys

from containers.stack import MinMaxStack


def main():
    stack = MinMaxStack()
    q = int(input())

    for _ in range(q):
        query = sys.stdin.readline().strip()

        if query == "pop":
            stack.pop()
        elif query == "max":
            print("max: ", stack.max())
        elif query == "min":
            print("min: ", stack.min())
        else:
            push = int(query.split()[1])
            stack.push(push)


if __name__ == "__main__":
    main()