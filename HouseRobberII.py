class Solution:
    def rob(self, nums):
        return max(nums[0], self.route(nums[1 : ]), self.route(nums[ : -1]))

    def route(self, house):
        L, M = 0, 0

        for i in house:
            tem = max(L + i, M)
            L = M
            M = tem

        return M

# input
# nums = 

# test case 1
# Output: 3
nums = [2, 3, 2]

# test case 2
# Output: 4
# nums = [1, 2, 3, 1]

# test case 3
# Output:3
# nums=[2, 1, 1, 2]

sol = Solution()

output = sol.rob(nums)
print(output)