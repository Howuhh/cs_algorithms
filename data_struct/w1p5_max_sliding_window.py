from containers.stack import QueueWithStack


def window_max(w, arr):
    queue = QueueWithStack()
    max_values = []

    for value in arr:
        if queue.len() >= w:
            queue.popFront()

        queue.pushBack(value)
        
        if queue.len() == w:
            max_values.append(queue.max())

    return max_values  # O(n)


def main():
    n, arr = int(input()), [int(x) for x in input().split()]
    w_size = int(input())

    print(window_max(w_size, arr))


if __name__ == "__main__":
    main()