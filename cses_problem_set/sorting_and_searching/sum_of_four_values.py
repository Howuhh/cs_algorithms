
def four_sum(nums, target):

    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            two_target = target - nums[i][0] - nums[j][0]

            left, right = j + 1, len(nums) - 1
            while left < right:
                two_sum = nums[left][0] + nums[right][0]

                if two_sum == two_target:
                    return [nums[i][1] + 1, nums[j][1] + 1, nums[left][1] + 1, nums[right][1] + 1]
                elif two_sum < two_target:
                    left = left + 1
                else:
                    right = right - 1
    return ["IMPOSSIBLE"]


def main():
    n, target = map(int, input().split())
    nums = [(int(i), idx) for idx, i in enumerate(input().split())]
    nums.sort()

    print(*four_sum(nums, target))


if __name__ == "__main__":
    main()

# NOT WORKING
# def four_sum_notwork(nums, target):

#     four_left, four_right = 0, len(nums) - 1
#     while four_left < four_right:
#         two_target = target - nums[four_left][0] - nums[four_right][0]

#         best_sum = 0

#         two_left, two_right = four_left + 1, four_right - 1    
#         while two_left < two_right:
#             two_sum = nums[two_left][0] + nums[two_right][0]

#             best_sum = max(best_sum, two_sum + nums[four_left][0] + nums[four_right][0])

#             if two_sum == two_target:
#                 # print(nums[four_left], nums[two_left], nums[two_right], nums[four_right])
#                 return [
#                     nums[four_left][1] + 1, 
#                     nums[two_left][1] + 1, 
#                     nums[two_right][1] + 1, 
#                     nums[four_right][1] + 1
#                     ]
#             elif two_sum < two_target:
#                 two_left = two_left + 1
#             else:
#                 two_right = two_right - 1

#         if best_sum < target:
#             four_left = four_left + 1
#         else:
#             four_right = four_right - 1
        
#     return ["IMPOSSIBLE"]




