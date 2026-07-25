class Solution:
    def calculate(self, s: str) -> int:
        op="+"
        num=0
        s+="+"
        stack=[]
        for ch in s:
            if ch==" ":
                continue
            if ch.isdigit():
                num=num*10+int(ch)
            else:
                if op=="+":
                    stack.append(num)
                elif op=="-":
                    stack.append(-num)
                elif op=="*":
                    stack.append(int(stack.pop()*num))
                elif op=="/":
                    stack.append(int(stack.pop()/num))
                op=ch
                num=0
        return sum(stack)
                


        