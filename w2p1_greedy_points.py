from utils import to_int


# сортируем по правым концам, берем первой конец отрезка,
# все пересекающиеся отрезки пропускаем т.к. их мы уже покрыли точкой
def get_covering_set(intervals: list) -> list:
    sorted_int = sorted(intervals, key=lambda tup: tup[1])  # O(nlog(n))
    
    points = [sorted_int[0][1]]

    for l, r in sorted_int[1:]:  # O(n)
        if l > points[-1]:
            points.append(r)

    return len(points), points  # O(nlogn) + O(n) = O(nlogn)


if __name__ == "__main__":
    n = int(input())
    intervals = [to_int(input().split()) for _ in range(n)]

    n, points = get_covering_set(intervals)

    print(n)
    print(*points)
