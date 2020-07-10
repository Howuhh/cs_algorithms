

def min_gondolas(weights, max_w): # O(n) two pointers approach
    count = 0

    left, right = 0, len(weights) - 1
    while left <= right:
        if weights[left] + weights[right] <= max_w:
            left += 1
        
        right -= 1            
        count += 1

    return count


def main():
    n, x = map(int, input().split())
    weights = [int(i) for i in input().split()]

    print(min_gondolas(sorted(weights), x))


if __name__ == "__main__":
    main()