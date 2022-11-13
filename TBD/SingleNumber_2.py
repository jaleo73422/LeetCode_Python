class Solution:
    def singleNumber(self, nums):
        temp = 0

        for i in nums:
            temp ^= i

        return temp

# input
# nums = 

# test case 1
# Output: 1
# nums = [2, 2, 1]

# test case 2
# Output: 4
# nums = [4, 1, 2, 1, 2]

# test case 3
# Output: 1
nums = [1]

sol = Solution()

output = sol.singleNumber(nums)
print(output)