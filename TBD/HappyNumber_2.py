class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n

        while slow != 1:
            slow = sum([int(i) ** 2 for i in str(slow)])

            fast = sum([int(i) ** 2 for i in str(fast)])
            fast = sum([int(i) ** 2 for i in str(fast)])

            if slow == fast and slow != 1:
                return False
            
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