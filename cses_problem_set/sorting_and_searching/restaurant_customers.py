import sys
# import time


def max_people(times):
    count, max_count = 0, 0

    for time in times:
        count = count + time[1]
        
        if count > max_count:
            max_count = count
        # max_count = max(count, max_count)

    return max_count


def main():
    # s1 = time.time()
    n = int(sys.stdin.readline())
    times = []
    
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        times.append((int(a), 1))
        times.append((int(b), -1))
    
    times.sort()

    print(max_people(times))
    # print(time.time() - s1)


if __name__ == "__main__":
    main()