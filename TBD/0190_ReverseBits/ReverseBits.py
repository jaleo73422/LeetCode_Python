class Solution:
    def reverseBits(self, n):
        output = 0
        
        for i in range(32):
            # bit = (n >> i) & 1
            # output |= (bit << (31 - i))
            output |= (((n >> i) & 1) << (31 - i))
                
        return output

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