class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for i in nums:
            if i != 0:
                nums[l] = i
                l += 1
            
        for i in range(l, len(nums)):
            nums[i] = 0
            
        return nums

# input
# nums = 

# test case 1
# Output: [1, 3, 12, 0, 0]
nums = [0, 1, 0, 3, 12]

# test case 2
# Output: [0]
# nums = [0]

sol = Solution()

output = sol.moveZeroes(nums)
print(output)