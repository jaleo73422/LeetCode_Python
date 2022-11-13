class Solution:
    def reverseBits(self, n):
        """
         1 =>  1
        <0>   <0>

         1   1  =>  1 + 2 * (1)
        <1> <0>    <0>      <1>
        
         1   1   1   =>  1 + 2 * (1 + 2)
        <2> <1> <0>     <0>      <1> <2>
        
         1   1   1   1  =>  1 + 2 * (1 + 2 * (1 + 2))
        <3> <2> <1> <0>    <0>      <1>      <2> <3>
        """
        res = 0
        
        while n:
            res =  2 * ((n % 10) + res)
            n //= 10
                
        return int(res / 2)

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