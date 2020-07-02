# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root == None: return result
        Q = []
        Q.append(root)
        
        while len(Q) > 0:
            nodes = []
            for i in range(len(Q)):
                node = Q.pop(0)
                nodes.append(node.val)
                if node.left!= None: Q.append(node.left)
                if node.right!= None: Q.append(node.right)
            result.append(nodes)
        return reversed(result)
        