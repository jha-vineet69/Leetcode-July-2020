# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1:
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root==None:
            return 0
        ans=0
        q=collections.deque()
        q.append([root,0])

        while q:
            level=[]
            n=len(q)
            wide=q[-1][1]-q[0][1]+1
            ans=max(ans, wide)
            for _ in range(n):
                t=q.popleft()
                if t[0].left:
                    level.append([t[0].left, 2*t[1]])
                if t[0].right:
                    level.append([t[0].right, 2*t[1]+1])
            q.extend(level)
        return ans

#Approach 2:
class Solution:
    def widthOfBinaryTree(self, root):
        queue = [(root, 0, 0)]
        cur_depth = left = ans = 0
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth+1, pos*2))
                queue.append((node.right, depth+1, pos*2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)

        return ans
        