from bisect import bisect_left

# would work only with std::set
# def traffic_lights(length, lights):  # O(n^2)
#     points = [0, length]
#     lengths = [length]

#     for light in lights:
#         split = bisect_left(points, light)

#         points.insert(split, light)

#         left, right = points[split - 1], points[split + 1]

#         lengths.remove(right - left)
#         lengths.append(light - left)
#         lengths.append(right - light)

#         print(max(lengths), end=" ")


# move backward: 
# 0 2 3 6 8 -> 0 3 6 8 -> 0 3 8 -> 0 8
def traffic_lights(points, x):
    splits = [0] + sorted(points) + [x, -1]  # -1 just for easy indexing

    bounds = {}
    for i in range(len(splits) - 1):
        bounds[splits[i]] = [splits[i - 1], splits[i + 1]]

    max_length = max(splits[i + 1] - splits[i] for i in range(len(splits) - 1))

    max_lengths = []
    for p in reversed(points):
        max_lengths.append(max_length)

        l, r = bounds.pop(p)
        max_length = max(max_length, r - l)

        # change bounds 0 3 6 -> 0 6
        bounds[r][0] = l
        bounds[l][1] = r

    return max_lengths


def main():
    x, n = map(int, input().split())

    splits = [int(i) for i in input().split()]

    print(*traffic_lights(splits, x)[::-1])


if __name__ == "__main__":
    main()