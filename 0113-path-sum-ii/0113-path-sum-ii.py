# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result=[]
        def fun(node,currentsum,path):
            if node is None:
                return
            currentsum+=node.val
            path.append(node.val)
            
            if node.left is None and node.right is None:
                if(currentsum==targetSum):
                    result.append(path.copy())
            fun(node.left,currentsum,path)
            fun(node.right,currentsum,path)
            path.pop()
        fun(root,0,[])
        return result

        