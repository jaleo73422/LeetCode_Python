class Solution(object):
    def maxProduct(self, nums):
        """
        X X X X i X X
        dp[i] = max(dp[i - 1] * nums[i], dp[i - 1], num[i])
        """
        dp_min = [1 for i in range(len(nums))]
        dp_max = [1 for i in range(len(nums))]

        dp_min[0] = nums[0]
        dp_max[0] = nums[0]

        max_output = nums[0]

        for i in range(1, len(nums)):
            # if there is 0 in nums, max_product = nums[i]
            dp_min[i] = min(dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i], nums[i])
            dp_max[i] = max(dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i], nums[i])

            max_output = max(dp_max[i], max_output)

        return max_output

# input
# nums = []

# test case 1
# # Output: 6
# nums = [2, 3, -2, 4]

# test case 2
# Output: 0
# nums = [-2, 0, -1]

# test case 3
# Output: -2
# nums = [-2]

# test case 4
# Output: 24
# nums = [2, -5, -2, -4, 3]

# test case 5
# Output: 0
# nums = [-2, 0]

# test case 6
# Output: 2
nums = [-5, 0, 2]

sol = Solution()

output = sol.maxProduct(nums)
print(output)