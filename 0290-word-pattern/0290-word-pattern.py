class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        aMap = {}
        aList = s.split(" ")
        if len(aList) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in aMap:
                if aList[i] != aMap.get(pattern[i]):
                    return False
            else:
                if aList[i] in aMap.values():
                    return False
                aMap[pattern[i]] = aList[i]
        return True
            