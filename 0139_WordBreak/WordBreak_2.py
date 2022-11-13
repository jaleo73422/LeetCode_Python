class Solution:
    def wordBreak(self, s, wordDict):
        class TrieNode(object):
            def __init__(self):
                self.children = []  # will be of size = 26
                self.isLeaf = False
 
            def getNode(self):
                p = TrieNode()  # new trie node
                p.children = []

                for i in range(26):
                    p.children.append(None)
                
                p.isLeaf = False
                
                return p
 
            def insert(self, root, key):
                key = str(key)
                pCrawl = root
                
                for i in key:
                    index = ord(i) - 97
                
                    if(pCrawl.children[index] == None):
                        # node has to be initialised
                        pCrawl.children[index] = self.getNode()
                
                    pCrawl = pCrawl.children[index]
                
                pCrawl.isLeaf = True  # marking end of word
 
            def search(self, root, key):
                # print("Searching %s" %key) #DEBUG
                pCrawl = root
                
                for i in key:
                    index = ord(i) - 97
                
                    if(pCrawl.children[index] == None):
                        return False

                    pCrawl = pCrawl.children[index]
                
                if(pCrawl and pCrawl.isLeaf):
                    return True
 
        def checkWordBreak(strr, root):            
            if(len(strr) == 0):
                return True
            
            for i in range(1, len(strr) + 1):
                if(root.search(root, strr[ : i]) and checkWordBreak(strr[i : ], root)):
                    return True

            return False
 
        """IMPLEMENT SOLUTION"""
        root = TrieNode().getNode()

        for i in wordDict:
            root.insert(root, i)
        
        out = checkWordBreak(s, root)
        
        if(out):
            return True
        else:
            return False

# input
# s = 
# wordDict = 

# test case 1
# Output: true
s = "leetcode"
wordDict = ["leet","code"]

# test case 2
# Output: true
# s = "applepenapple"
# wordDict = ["apple","pen"]

# test case 3
# Output: false
# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]

# test case 4
# Output: true
# s = "leetleetar"
# wordDict = ["lee","leet","tar"]

# test case 5
# Output: true
# s = "a"
# wordDict = ["a"]

# test case 6
# Output: true
# s = "aaaaaaa"
# wordDict = ["aaaa","aaa"]

sol = Solution()

output = sol.wordBreak(s, wordDict)
print(output)