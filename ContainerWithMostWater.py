class Solution:
    def maxArea(self, height):
        L, R = 0, len(height) - 1
        max_amount = 0
        current_amount = 0

        while L < R:
            current_amount = (R - L) * min(height[L], height[R])
            max_amount = max(max_amount, current_amount)

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return max_amount

# input
# height = 

# test case 1
# Output: 49
# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# test case 2
# Output: 1
height = [1, 1]

sol = Solution()

output = sol.maxArea(height)
print(output)