# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clone = {}
        
        def dfs(node):
            if node in clone:  return clone[node]
            
            tem = Node(node.val)
            clone[node] = tem
            
            for i in node.neighbors:
                tem.neighbors.append(dfs(i))
            
            return tem
        
        return dfs(node) if node else None

# input
# adjList =  

# test case 1
# Output: [[2, 4], [1, 3], [2, 4], [1, 3]]
# adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]

b = Node(2)
c = Node(3)
d = Node(4)
adjList = Node(1)
b.neighbors = [adjList, c]
c.neighbors = [b, d]
d.neighbors = [adjList, c]
adjList.neighbors = [b, c]

# test case 2
# Output: [[]]
# adjList = [[]]

# adjList = Node(1)

# test case 3
# Output: []
# adjList = []

# adjList = Node()

sol = Solution()

output = sol.cloneGraph(adjList)
print(output)
