class Solution:
    def rob(self, nums):
        dp = [[0 for j in range(len(nums))] for i in range(len(nums))]

        if len(nums) == 1:  return nums[0]
        
        if len(nums) == 2:  return max(nums[0], nums[1])

        for i in range(len(nums)):
            dp[i][i] = nums[i]

            """
            nums = [1, 2, 3, 1]

             (i) 0 1 2 3
            (j)
             0   1 X X X
             1   A 2 X X
             2   B A 3 X
             3   C B A 1

            i = 1 => (0, 1) (1, 2) (2, 3)
            i = 2 => (0, 2) (1, 3)
            i = 3 => (0, 3)
            """
        for distance in range(1, len(nums)):
            for j in range(len(nums) - distance):
                if distance < 2:
                    dp[j][j + distance] = max(nums[j], nums[j + 1])
                else:
                    dp[j][j + distance] = max(nums[j] + dp[j + 2][j + distance], dp[j + 1][j + distance])

        return max(dp[1][len(nums) - 1], nums[0] + dp[2][len(nums) - 2])

# input
# nums = 

# test case 1
# Output: 3
# nums = [2, 3, 2]

# test case 2
# Output: 4
# nums = [1, 2, 3, 1]

# test case 3
# Output:3
nums=[2, 1, 1, 2]

sol = Solution()

output = sol.rob(nums)
print(output)