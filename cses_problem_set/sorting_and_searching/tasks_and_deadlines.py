
def max_reward(tasks):
    prev_time = 0

    reward = 0
    for duration, deadline in tasks:
        finish_time = prev_time + duration
        reward += deadline - finish_time

        prev_time = finish_time
    
    return reward 


def main():
    n = int(input())
    tasks = []

    for _ in range(n):
        s, d = map(int, input().split())
        tasks.append((s, d))

    tasks.sort()

    print(max_reward(tasks))


if __name__ == "__main__":
    main()