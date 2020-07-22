import heapq

from containers.heapq import Heap


def main_heapq():
    n, m = map(int, input().split())
    proc_times = (int(t) for t in input().split())

    cpu_heap = [(0, cpu) for cpu in range(n)]
    heapq.heapify(cpu_heap)

    for proc in proc_times:
        time, cpu = heapq.heappop(cpu_heap)
        print(cpu, time)
        heapq.heappush(cpu_heap, (time + proc, cpu))


def main():
    n, m = map(int, input().split())
    proc_times = (int(t) for t in input().split())

    cpu_heap = Heap([(0, cpu) for cpu in range(n)])

    for proc in proc_times:
        time, cpu = cpu_heap.heappop()
        print(cpu, time)
        
        cpu_heap.heappush((time + proc, cpu))


if __name__ == "__main__":
    main()