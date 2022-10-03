class Solution(object):
    def containsDuplicate(self, nums):
        nums = sorted(nums)

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False

# input
# nums = []

# test case 1
# Output: true
# nums = [1, 2, 2, 1]

# test case 2
# Output: false
# nums = [1, 2, 3, 4]

# test case 3
# Output: true
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

sol = Solution()

output = sol.containsDuplicate(nums)
print(output)