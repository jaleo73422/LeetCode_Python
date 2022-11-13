class Solution:
    def search(self, nums, target):
        L, R = 0, len(nums) - 1
        
        while L <= R:
            M = (L + R) // 2

            if nums[M] == target:
                return M
            
            if nums[M] >= nums[L]:
                if target < nums[M] and target >= nums[L]:
                    R = M - 1
                else:
                    L = M + 1
            else:
                if target > nums[M] and target <= nums[R]:
                    L = M + 1
                else:
                    R = M - 1
            
        return -1

# input
# nums = []
# target =

# test case 1
# Output: 4
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

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
# nums = [1, 3, 5]
# target = 3

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