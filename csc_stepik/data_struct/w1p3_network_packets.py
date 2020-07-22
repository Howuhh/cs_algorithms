import sys

from containers.queue import QueueWithArray
from collections import namedtuple

packet_info = namedtuple("packet_info", ["id", "arrive_t", "process_t"])


class Buffer:
    def __init__(self, size):
        self._buffer = QueueWithArray(size)
        self._size = size
        self._log = []

        self._clock = 0

    def add_packet(self, packet):
        if self.check(packet.arrive_t):
            self.push(packet)
            print(self._log[-1])
        else:
            print(-1)

    def check(self, arrive_time):
        if self._buffer.empty():
            return True
        
        while (self._buffer.front() is not None) and (self._buffer.front() <= arrive_time):
            self._buffer.popFront()

        if self._buffer.len() < self._size:
            return True

        return False

    def push(self, packet):
        if self._buffer.empty():
            start_time = packet.arrive_t
            end_time = packet.arrive_t + packet.process_t
        else:
            start_time = self._clock
            end_time = self._clock + packet.process_t
        
        self._log.append(start_time)
        self._buffer.pushBack(end_time)
        self._clock = end_time

    def __str__(self):
        return self._buffer.__str__()


def main_class():
    qsize, n = map(int, input().split())
    buffer = Buffer(qsize)

    for p_id in range(n):
        arrive_t, process_t = map(int, input().split())
        buffer.add_packet(packet_info(p_id, arrive_t, process_t))


def main_simple():
    reader = (map(int, tup.split()) for tup in sys.stdin)
    qsize, n = next(reader)

    buffer, prev = QueueWithArray(qsize), 0
    for arrive, process in reader:
        while not buffer.empty() and buffer.front() <= arrive:
            buffer.popFront()

        if buffer.len() < qsize:
            if not buffer.empty():
                arrive = max(arrive, prev)

            buffer.pushBack(arrive + process)
            prev = arrive + process
            print(arrive)
        else:
            print(-1)


if __name__ == "__main__":
    main_simple()