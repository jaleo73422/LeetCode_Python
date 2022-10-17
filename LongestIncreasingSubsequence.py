class Solution:
    def lengthOfLIS(self, nums):
        """
        Each element of all_combination is the smallest element in nums 
        that satisfies the length of the LTS represented by this index.
        The output is the largest index not equal to the initial value.
        """
        all_combination = [max(nums) + 1] * len(nums)
        all_combination[0] = nums[0]
        ans = 0

        for i in range(1, len(nums)):
            for j in range(len(all_combination) - 1, -1, -1):
                if nums[i] > all_combination[j]:
                    if all_combination[j + 1] > nums[i]:
                        all_combination[j + 1] = nums[i]
                    
                        ans = max(ans, j + 1)
                        break
            
            all_combination[0] = min(all_combination[0], nums[i])
                
        return ans + 1

# input
# nums = 

# test case 1
# Output: 4
# nums = [10, 9, 2, 5, 3, 7, 101, 18]

# test case 2
# Output: 4
# nums = [0, 1, 0, 3, 2, 3]

# test case 3
# Output: 1
nums = [7, 7, 7, 7, 7, 7, 7]

sol = Solution()

output = sol.lengthOfLIS(nums)
print(output)