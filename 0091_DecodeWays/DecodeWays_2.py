class Solution:
    def numDecodings(self, s):
        dp = {len(s): 1}

        def dfs(i):
            if i in dp: return dp[i]
            if s[i] == "0":  return 0

            res = dfs(i + 1)

            if (i + 1) != len(s) and int(s[i] + s[i + 1]) <= 26 and int(s[i]) != 0:
                res += dfs(i + 2)
            
            dp[i] = res

            return res
        
        return dfs(0)

# input
# s = 

# test case 1
# Output: 2
# s = "12"

# test case 2
# Output: 3
# s = "226"

# test case 3
# Output: 0
# s = "06"

# test case 4
# Output: 1
# s = "10"

# test case 5
# Output: 1
s = "2101"

sol = Solution()

output = sol.numDecodings(s)
print(output)