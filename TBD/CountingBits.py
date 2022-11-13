class Solution:
    def countBits(self, n):
        now = 0
        count = 0
        output = []
        
        while now <= n:
            tem = now
            count = 0

            while tem >= 1:
                print(tem)
                if tem % 2 == 1:
                    count += 1

                tem //= 2

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