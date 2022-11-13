class Solution:
    def getSum(self, a, b):
        mask = 0xffffffff # 0xFFFFFFFF

        while b != 0:
            tmp = (a & b) << 1
            a = (a ^ b) & mask # addition without carry (uncarried sum)
            b = tmp & mask # only carry

        if a > (mask // 2): # if a is negative in 32 bits sense
            return ~(a ^ mask)
        else:
            return a

        """ another solution
        if (a >> 31) & 1:
            a = a & mask
            
            return ~(a ^ mask)
        """

# input
a = -12
b = -8

# test case 1
# Output: 3
# a = 1
# b = 2

# test case 2
# Output: 5
# a = 2
# b = 3

sol = Solution()

output = sol.getSum(a, b)
print(output)