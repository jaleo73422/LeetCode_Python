class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0

        while (r < len(nums)):
            if nums[r] == 0:
                r += 1
            else:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp

                l += 1
                r += 1
        
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