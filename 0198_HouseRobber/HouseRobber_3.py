class Solution:
    def rob(self, nums):
        L, M = 0, 0

        # [L, M, i, i + 1, ...]
        for i in nums:
            tem = max(L + i, M)
            L = M  # next round
            M = tem

        return M

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