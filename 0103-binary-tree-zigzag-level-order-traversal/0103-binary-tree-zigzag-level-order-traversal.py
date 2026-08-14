class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        queue=deque()
        if root is None:
            return []
        queue.append(root)
        level_num=0
        while(queue):
            size=len(queue)
            level=[]
            for i in range(size):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            if level_num%2==1:
                level=level[::-1]

            ans.append(level)

            level_num+=1

        return ans