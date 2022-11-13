class Solution:
    def lengthOfLIS(self, nums):
        def find_index(nums, target):
            left, right = 0, len(nums) - 1

            while left + 1 < right:
                mid = (left + right) // 2
                
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid

            return right
        
        sort = [float('inf')] * (len(nums) + 1)

        for num in nums:
            index = find_index(sort, num)
            sort[index] = num

        ans = 0

        for num in sort:
            if num != float('inf'):
               ans += 1

        return ans

# input
# nums =  

# test case 1
# Output: 4
# nums = [10, 9, 2, 5, 3, 7, 101, 18]

# test case 2
# Output: 4
nums = [0, 1, 0, 3, 2, 3]

# test case 3
# Output: 1
# nums = [7, 7, 7, 7, 7, 7, 7]

# test case 4
# Output: 3
# nums = [10, 9, 2, 5, 1, 4, 101, 18, 6]

sol = Solution()

output = sol.lengthOfLIS(nums)
print(output)