class Solution(object):
    def twoSum(self, nums, target):
        dic_hashmap = {}
        
        for i, v in enumerate(nums):
            another = target - v

            if another in dic_hashmap:
                return [dic_hashmap[another], i]

            dic_hashmap[nums[i]] = i

# input
# nums = []
# target = 0

# test case 1
# Output: [0, 1]
# nums = [3, 2, 4]
# target = 6

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