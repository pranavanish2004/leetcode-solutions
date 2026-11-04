class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dici={}
        for val in strs:
            key="".join(sorted(val))
            
            if key not in dici:
                dici[key]=[]
            dici[key].append(val)
        return list(dici.values())
            
        