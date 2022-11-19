class Solution:
    def countBits(self, n):
        output = []
    
        for i in range(n + 1):
            res = 0
        
            while i:
                res += (i & 1)
                i >>= 1
        
            output.append(res)
    
        return output

# input
# n =  

# test case 1
# Output: [0, 1, 1]
# n = 2

# test case 2
# Output: [0, 1, 1, 2, 1, 2]
n = 5

sol = Solution()

output = sol.countBits(n)
print(output)