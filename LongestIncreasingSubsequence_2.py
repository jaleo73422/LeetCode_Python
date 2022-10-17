class Solution:
    def lengthOfLIS(self, nums):
        """
        The index of LIS is the starting point of LTS.
        The element of LIS is the length of LTS.
        """
        LIS = [1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
  
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

sol = Solution()

output = sol.lengthOfLIS(nums)
print(output)