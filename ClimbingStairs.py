class Solution:
    def climbStairs(self, n):
        way = [1, 2]
        now = 2

        while len(way) < n:
            way.append(way[now - 1] + way[now - 2])
            now += 1

        return way[n - 1]

# input
# n =  

# test case 1
# Output: 2
# n = 2

# test case 2
# Output: 3
n = 3

sol = Solution()

output = sol.climbStairs(n)
print(output)