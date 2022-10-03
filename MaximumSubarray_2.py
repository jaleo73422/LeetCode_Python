class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = 0

        for i in nums:
            if current_sum < 0:
                current_sum = 0
            
            current_sum += i

            max_sum = max(max_sum, current_sum)

        return max_sum

# input
# nums = []

# test case 1
# Output: 6
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# test case 2
# Output: 1
# nums = [1]

# test case 3
# Output: 23
# nums = [5, 4, -1, 7, 8]

# test case 4
# Output: -1
nums = [-2, -1]

# test case 5
# Output: -1
nums = [-1, -2]

sol = Solution()

output = sol.maxSubArray(nums)
print(output)