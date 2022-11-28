# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        new_map, visit = {}, []
        
        if node == None: return None
        
        def copy_val(node):
            if node in new_map: return 
            
            new_map[node] = Node(node.val)
            
            for i in node.neighbors:
                copy_val(i)
        
        def copy_nei(node):
            if node.val not in visit:
                tem = []
                visit.append(node.val)
                
                for i in node.neighbors:
                    copy_nei(i)
                    tem.append(new_map[i])
                
                new_map[node].neighbors = tem
            else:  return
            
        copy_val(node)
        copy_nei(node)        
        
        return new_map[node]

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
