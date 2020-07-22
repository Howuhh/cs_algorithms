# simple naive approach? like insertion sort

def nearest_left(nums):
    res = [0] * len(nums)

    stack = []

    for i in reversed(range(len(nums))):

        while stack and nums[i] < nums[stack[-1]]:
            index = stack.pop()
            res[index] = i + 1 # 1 based answer (not just i)
        stack.append(i)

    return res


def nearest_left_wiki(nums):
    res = [0] * len(nums)

    stack = []
    for i, num in enumerate(nums):
        # keep smalest in stack, pop until the head is first value < num
        while stack and num <= nums[stack[-1]]:
            stack.pop()
            
        if stack:
            res[i] = stack[-1] + 1
        stack.append(i)

    return res



def main():
    n = input()
    nums = [int(i) for i in input().split()]

    print(*nearest_left(nums))
    print(*nearest_left_wiki(nums))


if __name__ == "__main__":
    main()