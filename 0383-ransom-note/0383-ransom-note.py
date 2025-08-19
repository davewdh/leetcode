class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        aMap = {}
        for c in magazine:
            if aMap.get(c):
                aMap[c] += 1
            else:
                aMap[c] = 1
        
        for c in ransomNote:
            if aMap.get(c):
                if aMap[c] > 0:
                    aMap[c] -= 1
                else:
                    return False
            else:
                return False
        return True

