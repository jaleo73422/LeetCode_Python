class Solution:
    def rob(self, nums):
        dp = [0 for i in range(len(nums))]
        me = [0 for i in range(len(nums))]

        if(len(nums) == 1):
            return max(nums[0], 0)

        dp[0] = max(nums[0], 0)
        dp[1] = max(dp[0], nums[1])


        for i in range(0, 2):
            if(dp[i] == nums[i]):
                me[i] = 1
            else:
                me[i] = 0

        for i in range(2, len(nums)):    
            #    [1, 2, 3, 1]
            # dp [1, 2]
            if me[i - 1] == 1:
                if nums[i] > 0:
                    dp[i] = dp[i - 2] + nums[i]
                    me[i] = 1
                else:
                    dp[i] = dp[i - 2]
            else:
                if nums[i] > 0:
                    dp[i] = dp[i - 1] + nums[i]
                    me[i] = 1
                else:
                    dp[i] = dp[i - 1]

            dp[i] = max(dp[i], dp[i - 1])

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