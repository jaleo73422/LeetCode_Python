class Solution:
    def uniquePaths(self, m, n):
        dp = [1 for i in range(n)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[n - 1]

# input
# m = 
# n = 

# test case 1
# Output: 28
# m = 3
# n = 7

# test case 2
# Output: 3
m = 3
n = 2

sol = Solution()

output = sol.uniquePaths(m, n)
print(output)