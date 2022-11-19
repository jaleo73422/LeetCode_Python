class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

# input
# nums = []

# test case 1
# Output: [24, 12, 8, 6]
nums = [1, 2, 3, 4]

# test case 2
# Output: [0, 0, 9, 0, 0]
# nums = [-1, 1, 0, -3, 3]

# test case 3
# Output: [0, 0, 0]
# nums = [0, 4, 0]

sol = Solution()

output = sol.productExceptSelf(nums)
print(output)