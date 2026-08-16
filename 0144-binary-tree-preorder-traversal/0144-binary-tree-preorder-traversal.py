# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preorder(Node):
            if Node is None:
                return

            result.append(Node.val)
            preorder(Node.left)
            preorder(Node.right)

        preorder(root)

        return result
        