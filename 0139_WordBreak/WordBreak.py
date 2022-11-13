class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for j in wordDict:
                if i + len(j) <= len(s) and s[i : i + len(j)] == j:
                    dp[i] = dp[i + len(j)]
                    
                if dp[i]:
                    break
        
        return dp[0]

# input
# s = 
# wordDict = 

# test case 1
# Output: true
# s = "leetcode"
# wordDict = ["leet","code"]

# test case 2
# Output: true
# s = "applepenapple"
# wordDict = ["apple","pen"]

# test case 3
# Output: false
# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]

# test case 4
# Output: true
# s = "leetleetar"
# wordDict = ["lee","leet","tar"]

# test case 5
# Output: true
# s = "a"
# wordDict = ["a"]

# test case 6
# Output: true
s = "aaaaaaa"
wordDict = ["aaaa","aaa"]

sol = Solution()

output = sol.wordBreak(s, wordDict)
print(output)