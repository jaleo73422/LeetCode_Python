class Solution:
    def combinationSum(self, candidates, target):
        """
        case 1:
        Output: [[2, 2, 3], [7]]
        candidates = [2, 3, 6, 7]
        tarrget = 7

        all_combination[0] = target(1) = []
        all_combination[1] = target(2) = [2]
        all_combination[2] = target(3) = [3]
        all_combination[3] = target(4) = [2, 2]
        all_combination[4] = target(5) = [2, 3]
        all_combination[5] = target(6) = [2, 2, 2], [3, 3], [6]
        all_combination[6] = target(7) = [2, 2, 3], [7]
        """
        all_combination = [[] for i in range(target)]

        for i in range(target):
            L = 0
            temp = []

            if (i + 1) in candidates:
                all_combination[i].append([i + 1])

            while L <= (i + 1) // 2 :

                if i == 0:
                    break

                if all_combination[L] != [] and all_combination[i - L - 1] != []:
                    for j in all_combination[L]:
                        for k in all_combination[i - L - 1]:
                            temp = sorted(j + k)

                            if temp not in all_combination[i]:
                                all_combination[i].append(temp)

                L += 1
            
        return all_combination[target - 1]

# input
# candidates = 
# target = 

# test case 1
# Output: [[2, 2, 3], [7]]
# candidates = [2, 3, 6, 7]
# target = 7

# test case 2
# Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
# candidates = [2, 3, 5]
# target = 8

# test case 3
# Output: []
candidates = [2]
target = 1


sol = Solution()

output = sol.combinationSum(candidates, target)
print(output)