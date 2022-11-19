class Solution:
    def countBits(self, n):
        dp = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            dp[i] = dp[i & (i - 1)] + 1

        return dp

# input
# n =  

# test case 1
# Output: [0, 1, 1]
# n = 2

# test case 2
# Output: [0, 1, 1, 2, 1, 2]
n = 5

sol = Solution()

output = sol.countBits(n)
print(output)