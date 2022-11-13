class Solution:
    def search(self, nums, target):
        min_index = nums.index(min(nums))
        L, R = 0, 0

        if target == nums[0]:
            return 0
        elif target == nums[len(nums) - 1]:
            return len(nums) - 1
        elif target == nums[min_index]:
            return min_index
        elif target < nums[len(nums) - 1]:
            L, R = min_index, len(nums) - 1
        elif target > nums[0]:
            L, R = 0, min_index
        else:
            return -1
        
        while L <= R:
            M = (L + R) // 2

            if target < nums[M]:
                R = M - 1
            elif target > nums[M]:
                L = M + 1
            else:
                return M
        
        return -1

# input
# nums = []
# target =

# test case 1
# Output: 4
# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 0

# test case 2
# Output: -1
# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 3

# test case 3
# Output: -1
# nums = [1]
# target = 0

# test case 4
# Output: 1
nums = [1, 3, 5]
target = 3

# test case 5
# Output: 0
# nums = [1]
# target = 1

# test case 6
# Output: 4
# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 0

sol = Solution()

output = sol.search(nums, target)
print(output)