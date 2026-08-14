class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=deque()
        ans=[]
        if root is None:
            return []
        queue.append(root)
        while queue:
            size=len(queue)
            level=[]
            for i in range(size):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level[-1])
        return ans
        