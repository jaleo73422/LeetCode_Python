class Solution:
    def canJump(self, nums):
        final = 0

        for i in range(len(nums) - 1):
            final = max(final, i + nums[i])

            if final == i:  return False
        
        return final >= len(nums) - 1

# input
# nums = 

# test case 1
# Output: true
# nums = [2, 3, 1, 1, 4]

# test case 2
# Output: false
# nums = [3, 2, 1, 0, 4]

# test case 3
# Output: false
nums = [0, 2, 3]

sol = Solution()

output = sol.canJump(nums)
print(output)