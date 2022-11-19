class Solution(object):
    def maxProfit(self, prices):
        output = 0
        tem_min = prices[0]

        for i in prices:
            if i < tem_min:
                tem_min = i
            
            output = max(output, i - tem_min)

        return output

# input
# prices = []

# test case 1
# Output: 5
# prices = [7, 1, 5, 3, 6, 4]

# test case 2
# Output: 0
# prices = [7, 6, 4, 3, 1]

# test case 3
# Output: 1
# prices = [2, 2, 1, 0, 1]

# test case 4
# Output: 2
# prices = [2, 1, 2, 1, 0, 1, 2]

# test case 5
# Output: 4
prices = [3, 2, 6, 5, 0, 3]

# test case 6
# Output: 2
# prices = [7, 2, 4, 1]

sol = Solution()

output = sol.maxProfit(prices)
print(output)