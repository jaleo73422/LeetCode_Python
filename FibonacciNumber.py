class Solution:
    def fib(self, n):
        way = [0, 1]
        now = 2

        while len(way) <= n:
            way.append(way[now - 1] + way[now - 2])
            now += 1

        return way[n]

# input
# n =  

# test case 1
# Output: 1
# n = 2

# test case 2
# Output: 2
n = 3

sol = Solution()

output = sol.fib(n)
print(output)