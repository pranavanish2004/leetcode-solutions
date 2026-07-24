class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dici={}
        stack=[]
        visited=set()#because there should be no duplicates
        for i in range(len(s)):
            val=s[i]
            if val in dici:
                dici[val]=dici[val]+1
            else:
                dici[val]=1
        for ch in s:
            dici[ch]-=1
            if ch in visited:
                continue
            while(stack and stack[-1]>ch and dici[stack[-1]]>0):
                visited.remove(stack.pop())
            stack.append(ch)
            visited.add(ch)
        return "".join(stack)

        