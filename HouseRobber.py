class Solution:
    def rob(self, nums):
        all_combination = [0 for i in range(len(nums))]

        if len(nums) == 1:
            return nums[0]
        
        all_combination[0] = nums[0]
        all_combination[1] = nums[1]
        
        for i in range(2, len(nums)):
            all_combination[i] = nums[i] + max(all_combination[0 : i - 1])

        return max(all_combination)

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