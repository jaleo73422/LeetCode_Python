class Solution:
    def rob(self, nums):
        dp = [0 for i in range(len(nums))]

        if len(nums) == 1:
            return nums[0]
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[len(nums) - 1]

# input
# nums = 

# test case 1
# Output: 4
# nums = [1, 2, 3, 1]

# test case 2
# Output: 12
nums = [2, 7, 9, 3, 1]

sol = Solution()

output = sol.rob(nums)
print(output)