class Solution:
    def countBits(self, n):
        output = []
        
        for i in range(n + 1):
            count = 0

            while i:
                if i % 2 == 1:  count += 1

                i //= 2

            output.append(count)
            
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