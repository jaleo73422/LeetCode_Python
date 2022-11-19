class Solution:
    def reverseBits(self, n):
        res = 0
        i = 0

        if(n == 0):  return 0
        
        while i < 32:
            res <<= 1

            if((n & 1) == 1):  res += 1

            n >>= 1
            i += 1
        
        return res

# input
# n =  

# test case 1
# Output: 964176192 (00111001011110000010100101000000)
# n = 00000010100101000001111010011100

# test case 2
# Output: 3221225471 (10111111111111111111111111111111)
n = 11111111111111111111111111111101

sol = Solution()

output = sol.reverseBits(n)
print(output)