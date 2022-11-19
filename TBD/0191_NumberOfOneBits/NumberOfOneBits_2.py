class Solution:
    def hammingWeight(self, n):
        count = 0

        while n:
            n &= n - 1
            
            count += 1

        return count

# input
# n =  

# test case 1
# Output: 3
# n = 10000000000000000000000000001001

# test case 2
# Output: 1
# n = 10000000000000000000000000000000

# test case 3
# Output: 31
# n = 11111111111111111111111111111101

# test case 4
# Output: 4
n = 10000000000000000000000000001011

sol = Solution()

output = sol.hammingWeight(n)
print(output)