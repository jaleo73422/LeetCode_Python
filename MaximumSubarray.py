class Solution:
    def maxSubArray(self, nums):
        """
        X X now next X X
        case1: sum < 0 => start from next
        case2: sum > 0 and next <= 0 => update max_sum and keep going
        case3: sum > 0 and next > 0 => keep going
        """
        now_num = 0
        max_sum = min(nums)
        current_sum = nums[0]

        while now_num != len(nums) - 1:
            max_sum = max(max_sum, current_sum)

            if current_sum < 0:
                now_num += 1
                current_sum = nums[now_num]
            else:
                current_sum += nums[now_num + 1]
                now_num += 1

        max_sum = max(max_sum, current_sum)

        return max_sum

# input
# nums = []

# test case 1
# Output: 6
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# test case 2
# Output: 1
# nums = [1]

# test case 3
# Output: 23
# nums = [5, 4, -1, 7, 8]

# test case 4
# Output: -1
nums = [-2, -1]

# test case 5
# Output: -1
nums = [-1, -2]

sol = Solution()

output = sol.maxSubArray(nums)
print(output)