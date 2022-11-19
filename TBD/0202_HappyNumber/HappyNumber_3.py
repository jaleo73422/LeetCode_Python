class Solution:
    def isHappy(self, n):
        cycle = []

        while n not in cycle:
            cycle.append(n)
            n = sum([int(i) ** 2 for i in str(n)])
            
        return True if n == 1 else False

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