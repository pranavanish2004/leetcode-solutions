class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        i=0
        ans=0     
        for i in range(len(s)):   
            if i+1<len(s) and table[s[i]]<table[s[i+1]]:
                ans=ans-table[s[i]]
            else:
                ans+=table[s[i]]
        return ans
        