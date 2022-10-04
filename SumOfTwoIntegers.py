class Solution:
    def getSum(self, a, b):
        mask = 0xffffffff

        while b != 0:
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = tmp & mask

        if a > mask // 2:
            return ~(a ^ mask)
        else:
            return a

# input
# a = 
# b = 

# test case 1
# Output: 3
a = 1
b = 2

# test case 2
# Output: 5
# a = 2
# b = 3

sol = Solution()

output = sol.getSum(a, b)
print(output)