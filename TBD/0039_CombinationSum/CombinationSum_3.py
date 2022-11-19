class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())

                return

            if i >= len(candidates) or total > target: return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)

        return res

# input
# candidates = 
# target = 

# test case 1
# Output: [[2, 2, 3], [7]]
candidates = [2, 3, 6, 7]
target = 7

# test case 2
# Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
# candidates = [2, 3, 5]
# target = 8

# test case 3
# Output: []
# candidates = [2]
# target = 1

sol = Solution()

output = sol.combinationSum(candidates, target)
print(output)