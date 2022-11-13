class Solution(object):
    def twoSum(self, nums, target):
        answer = []
        
        for i in range(len(nums) - 1):
            for j in range(len(nums)):
                if j > i:
                    if nums[i] + nums[j] == target:
                        answer.append(i)
                        answer.append(j)

                        return answer

# input
# nums = []
# target = 0

# test case 1
# Output: [0, 1]
# nums = [2, 7, 11, 15]
# target = 9

# test case 2
# Output: [1, 2]
# nums = [3, 2, 4]
# target = 6

# test case 3
# Output: [1, 2]
nums = [3, 2, 4]
target = 6

sol = Solution()

output = sol.twoSum(nums, target)
print(output)