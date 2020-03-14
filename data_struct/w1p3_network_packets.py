from containers import QueueWithArray
from collections import namedtuple

packet_info = namedtuple("packet_info", ["id", "end_time"])

class Buffer:
    pass



def main():
    qsize, n = map(int, input().split())
    buffer = QueueWithArray(size=qsize)

    process_start, prev_end = [None] * n, []

    for p_id in range(n):
        arrive_t, process_t = map(int, input().split())


if __name__ == "__main__":
    main()