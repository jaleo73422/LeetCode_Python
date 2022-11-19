class Solution:
    def singleNumber(self, nums):
        output = []

        for i in nums:
            if i in output:
                output.remove(i)
            else:
                output.append(i)

        return output[0]

# input
# nums = 

# test case 1
# Output: 1
nums = [2, 2, 1]

# test case 2
# Output: 4
# nums = [4, 1, 2, 1, 2]

# test case 3
# Output: 1
# nums = [1]

sol = Solution()

output = sol.singleNumber(nums)
print(output)