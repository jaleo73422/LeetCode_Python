class Solution:
    def threeSum(self, nums):
        answer = []
        frist = []
        second = []

        nums.sort()

        for i in range(len(nums) - 2): 
            L, R = i + 1, len(nums) - 1
            second = []

            if nums[i] in frist:
                continue

            while L < R:
                if nums[L] in second:
                    L += 1
                    continue
                
                if  nums[L] + nums[R] == -nums[i]:
                    if [nums[i], nums[L], nums[R]] not in answer :
                        answer.append(sorted([nums[i], nums[L], nums[R]]))
                        frist.append(nums[i])
                        second.append(nums[L])
                    
                    L += 1
                elif nums[L] + nums[R] < -nums[i]:
                    L += 1
                else:
                    R -= 1
                    
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
# nums = [-2, 0, 0, 2, 2]

# test case 5
# Output: [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
# nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]

# test case 6
# Output: [[-1, -1, 2], [-1, 0, 1]]
nums = [-1, 0, 1, 2, -1, -4]

sol = Solution()

output = sol.threeSum(nums)
print(output)