class Solution:
    def findMin(self, nums):
        L = 0
        R = len(nums) - 1
        min_value = nums[0]

        while L <= R:
            if nums[L] < nums[R]:
                min_value = min(min_value, nums[L])
                break
            
            M = (L + R) // 2
            min_value = min(min_value, nums[M])

            if nums[M] >= nums[L]:
                L = M + 1
            else:
                R = M - 1

        return min_value

# input
# nums = []

# test case 1
# Output: 1
# nums = [3, 4, 5, 1, 2]

# test case 2
# Output: 0
# nums = [4, 5, 6, 7, 0, 1, 2]

# test case 3
# Output: 11
# nums = [11, 13, 15, 17]

# test case 4
# Output: 1
# nums = [2, 1]

# test case 5
# Output: 1
nums = [8, 9, 1, 2, 3, 4, 5, 6, 7]

sol = Solution()

output = sol.findMin(nums)
print(output)