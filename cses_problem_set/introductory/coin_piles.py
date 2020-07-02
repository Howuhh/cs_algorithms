
def can_empty(a, b):
    return (a + b) % 3 == 0 and abs(a - b) <= min(a, b)

def main():
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        
        print("YES" if can_empty(a, b) else "NO")

if __name__ == "__main__":
    main()