class Solution:
    def missingNumber(self, nums):
        """
        1) n ^ 0 = n
        2) n ^ n = 0
        3) n1 ^ n2 ^ n3 = n3 ^ n1 ^ n2
        """
        ans = len(nums)
        
        for i in range(len(nums)):
            ans ^= (i ^ nums[i])
        
        return ans

# input
# nums =  

# test case 1
# Output: 2
# nums = [3, 0, 1]

# test case 2
# Output: 2
# nums = [0, 1]

# test case 3
# Output: 8
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

sol = Solution()

output = sol.missingNumber(nums)
print(output)