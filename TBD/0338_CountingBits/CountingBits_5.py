class Solution:
    def countBits(self, n):
        """
           0 1 1 0 1 1 = dp[i]
        => 0 1 1 0 1 0 = dp[i - (i & -i)]
        dp[i] = 1 + dp[i - (i & -i)]
        by BIT (Binary Indexed Tree)
        """
        dp = [0 for i in range(n + 1)]

        for i in range (1, n + 1):
            dp[i] = dp[i - (i & - i)] + 1

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