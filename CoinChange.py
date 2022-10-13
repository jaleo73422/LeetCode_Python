class Solution:
    def coinChange(self, coins, amount):
        all_combination = [amount + 1] * (amount + 1)
        all_combination[0] = 0

        for i in range(1, amount + 1):
            for j in coins:
                if i - j >= 0:
                    all_combination[i] = min(all_combination[i], 1 + all_combination[i - j])

        if all_combination[amount] != amount + 1:
            return all_combination[amount]
        else: 
            return -1

# input
# coins = 
# amount = 

# test case 1
# Output: 3
coins = [1, 2, 5]
amount = 11

# test case 2
# Output: -1
# coins = [2]
# amount = 3

# test case 3
# Output: 0
# coins = [1]
# amount = 0

# test case 4
# Output: 2
# coins = [1, 3, 4, 5]
# amount = 7

sol = Solution()

output = sol.coinChange(coins, amount)
print(output)