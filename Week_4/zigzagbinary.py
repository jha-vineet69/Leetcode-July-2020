# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return root
        result = [[]]
        self.dfs(root, 0, result)
        return result
    
    def dfs(self, root, level, result):
        if root == None:
            return
        if len(result) == level:
            result.append([])
        if level%2 == 0:
            result[level].append(root.val)
        else:
            result[level].insert(0, root.val)
        
        self.dfs(root.left, level+1, result)
        self.dfs(root.right, level+1, result)
            
        