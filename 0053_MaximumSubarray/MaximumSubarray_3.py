class Solution:
    def maxSubArray(self, nums):
        """
        X [X X i] X X X
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        """
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]

        max_output = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

            max_output = max(dp[i], max_output)

        return max_output

# input
# nums = []

# test case 1
# Output: 6
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# test case 2
# Output: 1
# nums = [1]

# test case 3
# Output: 23
# nums = [5, 4, -1, 7, 8]

# test case 4
# Output: -1
# nums = [-2, -1]

# test case 5
# Output: -1
# nums = [-1, -2]

sol = Solution()

output = sol.maxSubArray(nums)
print(output)