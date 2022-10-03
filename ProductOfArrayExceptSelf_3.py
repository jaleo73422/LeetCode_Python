class Solution(object):
    def productExceptSelf(self, nums):
        """
        perfix:  1  1  2  6 24          1  1  2  6
        input:      1  2  3  4     =>   1  2  3  4
        postfix:   24 24 12  4  1      24 12  4  1
        oitput:                        24 12  8  6
        """
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        answer = [0] * len(nums)

        tem_pre = 1
        for i in range(len(nums)):
            prefix[i] = tem_pre
            tem_pre *= nums[i]
        
        tem_post = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = tem_post
            tem_post *= nums[i]
            answer[i] = prefix[i] * postfix[i]

        return answer

# input
# nums = []

# test case 1
# Output: [24, 12, 8, 6]
nums = [1, 2, 3, 4]

# test case 2
# Output: [0, 0, 9, 0, 0]
# nums = [-1, 1, 0, -3, 3]

# test case 3
# Output: [0, 0, 0]
# nums = [0, 4, 0]

sol = Solution()

output = sol.productExceptSelf(nums)
print(output)