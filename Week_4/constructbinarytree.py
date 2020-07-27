# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        length = len(inorder)
        return self.helper(inorder, postorder, 0, length-1, 0 , length-1)
    
    def helper(self, inorder, postorder, instart, inend, poststart, postend):
        if instart > inend:
            return None
        rootval = postorder[postend]
        root = TreeNode(rootval)
        
        rootindex = instart
        while rootindex<= inend:
            if inorder[rootindex]==rootval:
                break
            rootindex+=1
        lefttreesize = rootindex - instart
        righttreesize = inend - rootindex
        
        root.left = self.helper(inorder, postorder, instart, rootindex-1, poststart, poststart+lefttreesize-1)
        root.right = self.helper(inorder, postorder, rootindex+1, inend, postend-righttreesize, postend-1)
        
        return root
               
        