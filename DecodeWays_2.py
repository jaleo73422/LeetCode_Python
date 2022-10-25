class Solution:
    def numDecodings(self, s):
        dp = [0 for i in range(len(s) + 1)]
        dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) == 0:
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if i + 1 != len(s) and int(s[i] + s[i + 1]) <= 26 and int(s[i]) != 0:
                dp[i] += dp[i + 2]

        return dp[0]

# input
# s = 

# test case 1
# Output: 2
# s = "12"

# test case 2
# Output: 3
s = "226"

# test case 3
# Output: 0
# s = "06"

# test case 4
# Output: 1
# s = "10"

sol = Solution()

output = sol.numDecodings(s)
print(output)