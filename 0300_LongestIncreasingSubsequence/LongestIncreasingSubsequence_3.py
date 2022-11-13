class Solution:
    def lengthOfLIS(self, nums):
        LIS = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):            
            for j in range(0, i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)

        return max(LIS)

# input
# nums =  

# test case 1
# Output: 4
# nums = [10, 9, 2, 5, 3, 7, 101, 18]

# test case 2
# Output: 4
nums = [0, 1, 0, 3, 2, 3]

# test case 3
# Output: 1
# nums = [7, 7, 7, 7, 7, 7, 7]

# test case 4
# Output: 3
# nums = [10, 9, 2, 5, 1, 4, 101, 18, 6]

sol = Solution()

output = sol.lengthOfLIS(nums)
print(output)