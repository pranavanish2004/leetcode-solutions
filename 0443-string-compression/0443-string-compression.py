class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        j=0
        while(i<len(chars)):
            ch=chars[i]
            cnt=0
            while(i<len(chars) and chars[i]==ch):
                i+=1
                cnt+=1
            chars[j]=ch
            j+=1
            if cnt>1:
                for x in str(cnt):
                    chars[j]=x
                    j+=1
        return j
        