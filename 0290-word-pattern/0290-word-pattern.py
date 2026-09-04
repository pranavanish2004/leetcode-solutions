class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        dici={}
        dici2={}
        if len(pattern)!=len(words):
            return False
        for i in range(len(pattern)):
            ch=pattern[i]
            word=words[i]
            if ch in dici:
                if dici[ch]!=word:
                    return False
            if word in dici2:
                if dici2[word]!=ch:
                    return False
            dici[ch]=word
            dici2[word]=ch
        return True

        