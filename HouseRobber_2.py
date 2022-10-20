class Solution:
    def rob(self, nums):
        """
        n1 n2 n3 ... nn-1 nn nn+1 ...
        L = sum(n1 : nn-1)
        M = nn
        R = nn+1
        => L M R
        output = max(L + R, M)
        """
        L, M = 0, 0

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