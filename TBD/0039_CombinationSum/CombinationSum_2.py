class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(num, cur):
            cursum = sum(cur)
        
            if cursum == target:
                res.append(cur.copy())

                return
        
            if num >= len(candidates) or cursum > target:
                return False
            
            for i in range(num, len(candidates)):
                backtrack(i, cur + [candidates[i]])
            
        backtrack(0, [])
        
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