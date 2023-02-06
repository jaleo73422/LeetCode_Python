class Solution:
    def canFinish(self, numCourses, prerequisites):


        return True

# input
# numCourses = 
# prerequisites = 

# test case 1
# Output: True
# numCourses = 2
# prerequisit [[1, 0]]

# test case 2
# Output: False
# numCourses = 2
# prerequisites = [[1, 0], [0, 1]]

# test case 3
# Output: False
# numCourses = 20
# prerequisites = [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]

# test case 4
# Output: False
numCourses = 3
prerequisites = [[1, 0], [0, 2], [2, 1]]

sol = Solution()

output = sol.canFinish(numCourses, prerequisites)
print(output)