import heapq


# likely will not work, so what about heaps? - not work!
def max_films(times, k):
    heap = []

    count = 0
    for start, end in times:
        # print(heap)
        if heap and start >= heap[0]:
            # print(heap)
            pop_end = heapq.heappop(heap)
            # print(f"Remove: {(pop_end)}", count)
            
        # print(heap)
        if len(heap) < k:
            heapq.heappush(heap, end)
            count += 1
            # print(f"Add: {(start, end)}", count)
    
    return count


def main():
    n, k = map(int, input().split())
    times = []

    for i in range(n):
        s, e = map(int, input().split())
        times.append((s, e))

    times.sort(key=lambda tup: tup[1])
    print(times)
    print(max_films(times, k))


if __name__ == "__main__":
    main()