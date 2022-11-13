class Solution:
    def countBits(self, n):
        now = 1
        count = 0
        output = [0]
        
        while now <= n:
            tem = now
            count = 0

            while tem:
                tem &= tem - 1
                
                count += 1

            output.append(count)
            now += 1
            
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