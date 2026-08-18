# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def fun(node,currentsum):
            if node is None:
                return 0
            currentsum=currentsum*10+node.val
            if node.left is None and node.right is None:
                return currentsum
            return fun(node.left,currentsum)+fun(node.right,currentsum)
        return fun(root,0)

        