from collections import Counter

def palindrome_reorder(string):
    counts = {}

    for char in string:
        counts[char] = counts.get(char, 0) + 1

    odds = [num % 2 == 1 for num in counts.values()]
    if sum(odds) > 1:
        return "NO SOLUTION"

    left, right, center = "", "", ""
    for letter, count in counts.items():
        if count % 2 == 1:
            center = letter # * count
            # for test 9, wierd test with one V in center kek, thats not right
            count -= 1
            
        left = left + letter * (count // 2)
        right = letter * (count // 2) + right 

    return left + center + right


def main():
    string = input()

    palindrome = palindrome_reorder(string)
    print(palindrome)

if __name__ == "__main__":
    main()