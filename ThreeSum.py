class Solution:
    def threeSum(self, nums):
        twosum = []
        duplicate = []
        answer = []

        for i in nums:
            twosum.append(0 - i)
        
        for i, v in enumerate(twosum):
            for j, w in enumerate(nums):
                if j <= i:
                    continue

                if v - w in nums[j + 1 : len(nums)]:
                    tem_ans = sorted([nums[i], w, v - w])

                    duplicate.append(v)

                    if tem_ans in answer:
                        continue

                    answer.append(tem_ans)
                    
        return answer

# input
# nums = []

# test case 1
# Output: [-1, -1, 2], [-1, 0, 1]
# nums = [-1, 0, 1, 2, -1, -4]

# test case 2
# Output: []
# nums = [0, 1, 1]

# test case 3
# Output: [0, 0, 0]
# nums = [0, 0, 0]

# test case 4
# Output: [-2, 0, 2]
nums = [-2, 0, 0, 2, 2]

# test case 5
# Output: [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
# nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]

# test case 6
# Output: [[-1, -1, 2], [-1, 0, 1]]
nums = [-1, 0, 1, 2, -1, -4]

sol = Solution()

output = sol.threeSum(nums)
print(output)