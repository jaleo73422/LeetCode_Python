class Solution(object):
    def productExceptSelf(self, nums):
        zero_num = 0
        total = 1

        for i in nums:
            if i == 0:
                zero_num += 1
            else:
                total *= i

        if zero_num == 0:
            for i, v in enumerate(nums):
                nums[i] = int(total / v)
        elif zero_num == 1:
            for i, v in enumerate(nums):
                if v != 0:
                    nums[i] = 0
                else:
                    nums[i] = total
        else:
            for i in range(len(nums)):
                nums[i] = 0        
        
        return nums

# input
# nums = []

# test case 1
# Output: [24, 12, 8, 6]
# nums = [1, 2, 3, 4]

# test case 2
# Output: [0, 0, 9, 0, 0]
# nums = [-1, 1, 0, -3, 3]

# test case 3
# Output: [0, 0, 0]
nums = [0, 4, 0]

sol = Solution()

output = sol.productExceptSelf(nums)
print(output)