class Solution:
    def longestCommonSubsequence(self, text1, text2):
        # wromg (?)
        # dp = [[0 for j in range(len(text2) + 1)]] * (len(text1) + 1)
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]
        
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
                    
        return dp[0][0]

# input
# text1 = 
# text2 = 

# test case 1
# Output: 3
# text1 = "abcde"
# text2 = "ace"

# test case 2
# Output: 3
# text1 = "abc"
# text2 = "abc"

# test case 3
# Output: 1
# text1 = "bsbininm"
# text2 = "jmjkbkjkv"

# test case 4
# Output: 2
# text1 = "oxcpqrsvwf"
# text2 = "shmtulqrypy"

# test case 5
# Output: 5
text1 = "abcba"
text2 = "abcbcba"

sol = Solution()

output = sol.longestCommonSubsequence(text1, text2)
print(output)