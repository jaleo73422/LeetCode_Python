class Solution(object):
    def containsDuplicate(self, nums):
        num_set = set()

        for i in nums:
            if i in num_set:
                return True

            num_set.add(i)

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