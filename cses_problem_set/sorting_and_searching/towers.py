from bisect import bisect_right


def min_towers(cubes):  # nlogn
    towers = []

    for cube in cubes: # n
        idx = bisect_right(towers, cube) # logn

        if idx >= len(towers):
            towers.append(cube)
        else:
            towers[idx] = cube

    return len(towers)


def main():
    n = input()
    cubes = [int(i) for i in input().split()]

    print(min_towers(cubes))


if __name__ == "__main__":
    main()