class Solution:
    def isHappy(self, n):
        cycle = [4, 16, 20, 37, 42, 58, 89, 145]
        
        while n != 1:
            if n in cycle:
                return False
            
            n = sum([int(i) ** 2 for i in str(n)])
            
        return True

# input
# n = 

# test case 1
# Output: ture
n = 19

# test case 2
# Output: false
# n = 2

sol = Solution()

output = sol.isHappy(n)
print(output)