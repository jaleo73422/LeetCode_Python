class Solution:
    def uniquePaths(self, m, n):
        side = max(m, n)
        dp = [[1 for i in range(side)] for i in range(side)] 
        
        for i in range(side * 2 - 1):
            for j in range(side):
                if j <= 0 or j >= m or i - j <= 0 or i - j >= n:
                    continue

                dp[j][i - j] = dp[j - 1][i - j] + dp[j][i - j - 1]

        return dp[m - 1][n - 1]

# input
# m = 
# n = 

# test case 1
# Output: 28
m = 3
n = 7

# test case 2
# Output: 3
# m = 3
# n = 2

sol = Solution()

output = sol.uniquePaths(m, n)
print(output)