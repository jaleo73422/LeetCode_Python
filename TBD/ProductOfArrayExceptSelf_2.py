class Solution(object):
    def productExceptSelf(self, nums):
        """
        perfix:  1  1  2  6 24          1  1  2  6
        input:      1  2  3  4     =>   1  2  3  4
        postfix:   24 24 12  4  1      24 12  4  1
        oitput:                        24 12  8  6
        """
        length = len(nums)
        prefix = [nums[0]] * length
        postfix = [nums[length - 1]] * length
        answer = [1] * length

        for i in range(length - 1):
            prefix[i + 1] = prefix[i] * nums[i + 1]

        for i in range(length - 1, 0, -1):
            postfix[i - 1] = postfix[i] * nums[i - 1]

        for i in range(length):
            if i == 0:
                answer[i] = postfix[1]
            elif i == length - 1:
                answer[i] = prefix[length - 2]
            else:
                answer[i] = prefix[i - 1] * postfix[i + 1]
        
        return answer

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