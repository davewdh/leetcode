class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        aSet = set()
        ans = set()
        for i in range(len(s) - 9):
            temp = s[i:i+10] 
            if temp in aSet:
                ans.add(temp)
            aSet.add(temp)
        return list(ans)