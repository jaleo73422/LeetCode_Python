class Solution:
    def findMin(self, nums):
        L, R = 0, len(nums) - 1
        M = 0
        output = nums[0]

        while L < R:
            M = (L + R) // 2

            if nums[M] > nums[R]:
                L = M + 1
                output = min(nums[L], nums[M], output)
            else:
                R = M - 1
                output = min(nums[R], nums[M], output)

        return output

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