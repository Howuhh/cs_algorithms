import sys


# TODO: TIMELIMIT (well, no ideas)
def room_allocation(n_cust, times):
    max_rooms, booked, last = 0, 0, 0

    res, rooms = [0] * n_cust, [0] * n_cust

    for time, out, idx in times:
        if out == 1:
            # free the room
            rooms[last] = res[idx]
            last += 1
       
        elif booked == last:
            max_rooms += 1
            
            res[idx] = max_rooms
        else:            
            res[idx] = rooms[booked]

            booked += 1

    return max_rooms, res
    

def main():
    n = int(sys.stdin.readline())

    times = []
    for idx in range(n):
        s, e = sys.stdin.readline().split()
        
        times.append([int(s), -1, idx])
        times.append([int(e), 1, idx])

    times.sort()

    count, rooms = room_allocation(n, times)

    print(count)
    print(*rooms)


if __name__ == "__main__":
    main()