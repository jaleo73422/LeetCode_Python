class Solution:
    def countBits(self, n):
        """
        0 -> 0000 => 0 = dp[0]
        1 -> 0001 => 1 + dp[n - 1] = 1
        2 -> 0010 => 1 + dp[n - 2] = 1
        3 -> 0011 => 1 + dp[n - 2] = 2
        4 -> 0100 => 1 + dp[n - 4] = 1
        5 -> 0101 => 1 + dp[n - 4] = 2
        6 -> 0110 => 1 + dp[n - 4] = 2
        7 -> 0111 => 1 + dp[n - 4] = 3
        8 -> 1000 => 1 + dp[n - 8] = 1
        """
        output = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if i == offset * 2:
                offset = i

            output[i] = 1 + output[i - offset]
        
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