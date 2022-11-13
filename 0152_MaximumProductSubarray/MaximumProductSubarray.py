class Solution(object):
    def maxProduct(self, nums):
        min_product = 1
        max_product = 1
        tem_max = 0
        tem_min = 0
        fin_max = min(nums)

        for i in nums:
            # if there is 0 in nums, max_product = i
            tem_max = max(max_product * i, min_product * i, i)
            tem_min = min(max_product * i, min_product * i, i)
            max_product = tem_max
            min_product = tem_min

            fin_max = max(fin_max, max_product)

        return fin_max

# input
# nums = []

# test case 1
# Output: 6
nums = [2, 3, -2, 4]

# test case 2
# Output: 0
# nums = [-2, 0, -1]

# test case 3
# Output: -2
# nums = [-2]

# test case 4
# Output: 24
# nums = [2, -5, -2, -4, 3]

# test case 5
# Output: 0
# nums = [-2, 0]

# test case 6
# Output: 2
# nums = [-5, 0, 2]

sol = Solution()

output = sol.maxProduct(nums)
print(output)